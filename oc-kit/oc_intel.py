"""Xe/Arc performance experiments; Python stdlib only. No NVIDIA interfaces."""
import argparse
import copy
import configparser
import fcntl
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import shlex
import shutil
import signal
import statistics
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = next((candidate for candidate in (
    HERE.parent,
    HERE.parent / "Oddly-llama.cpp/llama.cpp",
) if (candidate / "build-intel-all").is_dir()), HERE.parent)
DEFAULT_MODELS_ROOT = next((candidate for candidate in (
    HERE.parents[2] / "Models",
    HERE.parent.parent / "Models",
    HERE.parent / "Models",
) if candidate.is_dir()), HERE.parent.parent / "Models")
DEFAULT_PRESETS = DEFAULT_MODELS_ROOT / "presets.ini"
ERROR_RE = re.compile(r"(?:xe|drm|i915).*(?:hang|reset|fault|wedg|timed? ?out|error)", re.I)


def readint(path):
    return int(Path(path).read_text().strip())


def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as out:
        json.dump(data, out, indent=2)
        out.write("\n")
        out.flush()
        os.fsync(out.fileno())
        tmp = out.name
    os.replace(tmp, path)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as inp:
        for block in iter(lambda: inp.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


class Xe:
    def __init__(self, card):
        if not re.fullmatch(r"card[0-9]+", card):
            raise ValueError("--card must be a DRM card name, e.g. card0")
        self.device = (Path("/sys/class/drm") / card / "device").resolve(strict=True)
        if (self.device / "vendor").read_text().strip() != "0x8086":
            raise ValueError("Selected device is not Intel")
        if (self.device / "driver").resolve().name != "xe":
            raise ValueError("This port requires the Intel xe driver")
        intel_cards = [p for p in Path("/sys/class/drm").glob("card[0-9]*/device/vendor")
                       if p.read_text().strip() == "0x8086"]
        if len(intel_cards) != 1:
            raise ValueError("This host profile requires one Intel GPU to map the selected card to SYCL0")
        self.freq = self.device / "tile0/gt0/freq0"
        self.temps = sorted(self.device.glob("hwmon/hwmon*/temp*_input"))
        if not self.temps:
            raise ValueError("No GPU temperature sensors; refusing unmonitored tests")

    def identity(self):
        return {"pci": self.device.name, "device": (self.device / "device").read_text().strip()}

    def limits(self):
        return {key: readint(self.freq / key) for key in
                ("min_freq", "max_freq", "rpn_freq", "rp0_freq", "rpa_freq")}

    def sample(self, ceiling):
        temps = {}
        for path in self.temps:
            value = readint(path) / 1000
            crit = path.with_name(path.name.replace("_input", "_crit"))
            limit = min(ceiling, readint(crit) / 1000 - 5) if crit.exists() else ceiling
            if not 0 <= value < limit:
                raise RuntimeError(f"Temperature guard: {path.name}={value} C, limit={limit} C")
            temps[path.name] = value
        result = {"temperature_max_c": max(temps.values()),
                "actual_mhz": readint(self.freq / "act_freq"),
                "requested_mhz": readint(self.freq / "cur_freq")}
        for path in self.device.glob("hwmon/hwmon*/energy*_input"):
            result[path.stem + "_uj"] = readint(path)
        for path in self.device.glob("hwmon/hwmon*/power*_cap"):
            result[path.stem + "_watts"] = readint(path) / 1000000
        return result

    def set_floor(self, value):
        limits = self.limits()
        if not limits["rpn_freq"] <= value <= min(limits["max_freq"], limits["rp0_freq"], limits["rpa_freq"]):
            raise ValueError(f"Frequency floor {value} MHz is outside current driver bounds")
        subprocess.run(["sudo", "-n", "tee", str(self.freq / "min_freq")],
                       input=str(value) + "\n", text=True, stdout=subprocess.DEVNULL, check=True)
        if readint(self.freq / "min_freq") != value:
            raise RuntimeError("Driver did not accept the requested frequency floor")


class KernelLog:
    def __init__(self):
        self.prefix = []
        initial = self.query()
        if not initial:
            subprocess.run(["sudo", "-v"], check=True)
            self.prefix = ["sudo", "-n"]
            initial = self.query()
        if not initial:
            raise RuntimeError("Kernel journal is unavailable; cannot check GPU errors")
        self.cursor = initial[-1]["__CURSOR"]

    def query(self, cursor=None):
        cmd = self.prefix + ["journalctl", "-k", "-b", "--no-pager", "-o", "json"]
        cmd += ["--after-cursor", cursor] if cursor else ["-n", "1"]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if p.returncode:
            raise RuntimeError("Cannot read kernel journal: " + p.stderr.strip())
        return [json.loads(line) for line in p.stdout.splitlines() if line.startswith("{")]

    def check(self):
        rows = self.query(self.cursor)
        if rows:
            self.cursor = rows[-1]["__CURSOR"]
        errors = [r.get("MESSAGE", "") for r in rows if ERROR_RE.search(str(r.get("MESSAGE", "")))]
        if errors:
            raise RuntimeError("GPU kernel error: " + str(errors[-1]))


def runtime(args):
    root = args.root.resolve()
    bindir = root / "build-intel-all/bin"
    env = {k: v for k, v in os.environ.items() if not k.startswith("LLAMA_ARG_")}
    env["LD_LIBRARY_PATH"] = str(bindir) + ":" + env.get("LD_LIBRARY_PATH", "")
    # The checked-in build has a stale absolute backend runpath; force plugins
    # to come from the active build instead of a relocated checkout.
    env["GGML_BACKEND_PATH"] = str(bindir / "libggml-sycl.so")
    for key, value in {"GGML_SYCL_PTQ1_T2": "ffn", "GGML_SYCL_T2_W8A8_MIN": "0",
                       "GGML_SYCL_FA_ONEDNN_MAX_KV": "98304"}.items():
        env.setdefault(key, value)
    return bindir, [str(root / "scripts/run-sycl-level-zero.sh")], env


def prepare(args):
    bindir, wrapper, env = runtime(args)
    dest = HERE / "bin/llama-perplexity"
    dest.parent.mkdir(exist_ok=True)
    subprocess.run(["g++", str(HERE / "perplexity-main.cpp"), "-o", str(dest),
                    "-L" + str(bindir), "-Wl,--allow-shlib-undefined",
                    "-l:libllama-perplexity-impl.so"], check=True)
    # Backend discovery uses the executable directory for the built-in fallback
    # loaders. Keep these links inside oc-kit so the relocated build's stale
    # backend runpath cannot hide the CPU loader from the standalone tool.
    for name in ("libggml-sycl.so", "libggml-cpu.so"):
        link = dest.parent / name
        target = bindir / name
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(target)
    subprocess.run(wrapper + [str(dest), "--help"], env=env,
                   stdout=subprocess.DEVNULL, check=True, timeout=60)
    corpus = HERE / "corpus.txt"
    if not corpus.exists():
        # Deterministic stress corpus, not a model-quality evaluation dataset.
        paragraph = ("A computer processes instructions and stores information in memory. "
                     "Engineers measure speed by repeating the same experiment under controlled conditions. "
                     "A reliable result must preserve numerical correctness as well as performance. "
                     "The river flows from the mountains through the valley to the sea. "
                     "During the evening the air cools and the stars become visible.\n")
        corpus.write_text(paragraph * 2048)
    print(f"Prepared {dest} and {corpus}. No model loaded or GPU settings changed.")


def resolve_model(args):
    if args.model:
        model = args.model.expanduser().resolve()
    else:
        text = args.presets.read_text()
        config = configparser.ConfigParser(interpolation=None)
        config.read_string(text[text.index("["):])
        model = Path(config[args.alias]["model"])
    if not model.is_file():
        raise ValueError(f"Missing model: {model}")
    return model


def model_slug(model):
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", model.stem).strip("-.")
    return slug[:80] or "model"


def model_catalog(args):
    """Return existing preset GGUFs under the configured Models directory."""
    root = args.models_root.expanduser().resolve(strict=True)
    text = args.presets.expanduser().read_text()
    config = configparser.ConfigParser(interpolation=None)
    config.read_string(text[text.index("["):])
    found = {}
    for alias in config.sections():
        value = config[alias].get("model", "").strip()
        if not value:
            continue
        model = Path(value).expanduser().resolve()
        try:
            model.relative_to(root)
        except ValueError:
            continue
        if model.is_file() and model.suffix.lower() == ".gguf":
            found.setdefault(model, []).append(alias)
    return [{"model": model, "aliases": aliases, "alias": aliases[0],
             "slug": model_slug(model)} for model, aliases in sorted(found.items(), key=lambda x: str(x[0]))]


def tool_commands(args, model, threads, ubatch):
    bindir, wrapper, env = runtime(args)
    common = ["-m", str(model), "-ngl", "99", "-dev", "SYCL0", "-t", str(threads),
              "-b", "512", "-ub", str(ubatch), "-ctk", args.kv, "-ctv", args.kv,
              "-fa", "on", "--load-mode", "mmap"]
    bench = wrapper + [str(bindir / "llama-bench")] + common + [
        "-p", "512", "-n", "128", "-d", str(args.context), "-r", "3", "-o", "json", "-v"]
    ppl = wrapper + [str(HERE / "bin/llama-perplexity")] + common + [
        "-f", str(args.corpus), "-c", str(args.context), "--chunks", str(args.chunks)]
    return bench, ppl, env


def parse_bench(text):
    rows = json.loads(text)
    def speed(kind):
        vals = [float(r["avg_ts"]) for r in rows if int(r[kind]) > 0]
        if len(vals) != 1 or not math.isfinite(vals[0]) or vals[0] <= 0:
            raise ValueError("Benchmark output missing one valid result per pp/tg test")
        return vals[0]
    return {"pp": speed("n_prompt"), "tg": speed("n_gen")}


def parse_ppl(text):
    values = re.findall(r"Final estimate: PPL = ([0-9]+(?:\.[0-9]+)?)", text)
    if len(values) != 1 or not math.isfinite(float(values[0])) or float(values[0]) <= 0:
        raise ValueError("Missing valid final perplexity estimate")
    return values[0]


def stop_child(p):
    if p.poll() is None:
        os.killpg(p.pid, signal.SIGTERM)
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            p.wait()


class Runner:
    def __init__(self, args, xe, model, journal, directory):
        self.args, self.xe, self.model = args, xe, model
        self.journal, self.directory = journal, directory
        self.counter = 0

    def execute(self, command, env, label):
        outpath = self.directory / f"{self.counter:03d}-{label}.out"
        errpath = outpath.with_suffix(".err")
        start = time.monotonic()
        self.xe.sample(self.args.temp_limit)
        with outpath.open("w") as out, errpath.open("w") as err:
            p = subprocess.Popen(command, env=env, stdout=out, stderr=err, start_new_session=True)
            try:
                last_refresh = start
                while p.poll() is None:
                    sample = self.xe.sample(self.args.temp_limit)
                    with (self.directory / "telemetry.jsonl").open("a") as log:
                        log.write(json.dumps({"time": time.time(), "test": self.counter, **sample}) + "\n")
                    self.journal.check()
                    now = time.monotonic()
                    if now - start > self.args.timeout:
                        raise RuntimeError(f"Workload timed out: {label}")
                    if now - last_refresh > 30:
                        subprocess.run(["sudo", "-n", "-v"], stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True)
                        last_refresh = now
                    time.sleep(1)
                if p.returncode != 0:
                    raise RuntimeError(f"{label} exited {p.returncode}; see {errpath}")
                self.xe.sample(self.args.temp_limit)
                self.journal.check()
            finally:
                stop_child(p)
        return outpath.read_text(), errpath.read_text()

    def test(self, settings, baseline_ppl=None):
        self.counter += 1
        print(f"TEST {self.counter}: {settings}", flush=True)
        bench, ppl, env = tool_commands(self.args, self.model, settings["threads"], settings["ubatch"])
        out, err = self.execute(bench, env, "bench")
        if not re.search(r"offloaded (\d+)/\1 layers to GPU", err):
            raise RuntimeError("Could not confirm full GPU offload; see benchmark stderr")
        speed = parse_bench(out)
        out, err = self.execute(ppl, env, "ppl")
        chunks = re.search(r"(?:calculating perplexity|computing) over (\d+) chunks", out + err)
        if not chunks or int(chunks[1]) != self.args.chunks:
            raise RuntimeError("Perplexity did not evaluate the requested chunks; corpus may be too short")
        value = parse_ppl(out + err)
        result = {**settings, **speed, "ppl": value,
                  "pass": baseline_ppl is None or value == baseline_ppl}
        with (self.directory / "trials.jsonl").open("a") as log:
            log.write(json.dumps(result) + "\n")
        print(json.dumps(result), flush=True)
        return result


def active_servers():
    return subprocess.run(["pgrep", "-x", "llama-server"], capture_output=True, text=True).stdout.strip()


def fingerprint(args, model, xe):
    bindir, _, env = runtime(args)
    with model.open("rb") as inp:
        header = hashlib.sha256(inp.read(1024 * 1024)).hexdigest()
    return {"gpu": xe.identity(), "kernel": os.uname().release,
            "frequency_limits": xe.limits(),
            "model": str(model), "model_size": model.stat().st_size,
            "model_mtime_ns": model.stat().st_mtime_ns, "model_header": header,
            "corpus": digest(args.corpus), "context": args.context, "chunks": args.chunks,
            "kv": args.kv, "runtime": {k: v for k, v in env.items() if k.startswith(("GGML_", "SYCL_", "ZE_"))},
            "binaries": {p.name: digest(p) for p in sorted(bindir.glob("*.so*")) if p.is_file()},
            "bench": digest(bindir / "llama-bench"),
            "ppl_launcher": digest(HERE / "bin/llama-perplexity")}


def restore(xe, path):
    data = json.loads(path.read_text())
    if data["gpu"] != xe.identity():
        raise ValueError("Recovery snapshot is for a different GPU")
    if data["boot"] != Path("/proc/sys/kernel/random/boot_id").read_text().strip():
        path.rename(path.with_suffix(".previous-boot.json"))
        print("Archived snapshot from previous boot; current GPU settings left unchanged.")
        return
    xe.set_floor(data["min_freq"])
    path.unlink()


def tune(args, xe, model):
    if active_servers():
        raise RuntimeError("llama-server is running. Stop it yourself before testing; no services were stopped.")
    recovery = HERE / "results" / f"restore-{args.card}.json"
    if recovery.exists():
        raise RuntimeError("Unfinished hardware experiment: run reset first (see README for reboot recovery)")
    journal = KernelLog()
    subprocess.run(["sudo", "-v"], check=True)
    identity = fingerprint(args, model, xe)
    directory = args.results / time.strftime("run-%Y%m%d-%H%M%S")
    directory.mkdir()
    atomic_json(directory / "environment.json", identity)
    runner = Runner(args, xe, model, journal, directory)
    limits = xe.limits()
    initial = {"threads": 6, "ubatch": 256, "min_freq": limits["min_freq"]}
    baseline = [runner.test(initial) for _ in range(3)]
    if len({r["ppl"] for r in baseline}) != 1:
        raise RuntimeError("Stock perplexity is nondeterministic; aborting before any hardware writes")
    ppl = baseline[0]["ppl"]
    base_tg = statistics.median(r["tg"] for r in baseline)
    best = {**initial, "tg": base_tg, "pp": statistics.median(r["pp"] for r in baseline), "ppl": ppl}
    if args.mode == "baseline":
        atomic_json(directory / "baseline.json", best)
        print(f"Baseline saved: {directory}. No tuning applied.")
        return {"status": "baseline", "model": str(model), "run": str(directory),
                "baseline": str(directory / "baseline.json")}
    candidates = [dict(threads=t, ubatch=u, min_freq=limits["min_freq"])
                  for t, u in itertools.product(args.threads, args.ubatches)]
    if args.resume:
        old = json.loads((args.results / "best.json").read_text())
        if old["fingerprint"] != identity:
            raise ValueError("Saved result has a different model/build/corpus/configuration; run without --resume")
        candidate = {k: old["best"][k] for k in initial}
        if candidate["min_freq"] != initial["min_freq"] and not args.frequency:
            raise ValueError("Saved result uses frequency control; pass --frequency or start a fresh run")
        candidates.insert(0, candidate)
    if args.frequency:
        atomic_json(recovery, {"gpu": xe.identity(), "boot": Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                               "min_freq": limits["min_freq"]})
    try:
        for settings in candidates:
            if settings == initial:
                continue
            if args.frequency:
                xe.set_floor(settings["min_freq"])
            trial = runner.test(settings, ppl)
            if trial["pass"] and trial["tg"] > best["tg"] * 1.02:
                best = trial
        if args.frequency:
            ceiling = min(limits["max_freq"], limits["rp0_freq"], limits["rpa_freq"])
            for floor in range(limits["min_freq"] + args.freq_step, ceiling + 1, args.freq_step):
                xe.set_floor(floor)
                trial = runner.test({**{k: best[k] for k in initial}, "min_freq": floor}, ppl)
                if not trial["pass"] or trial["tg"] < base_tg * .93:
                    break
                if trial["tg"] > best["tg"] * 1.02:
                    best = trial
            xe.set_floor(best["min_freq"])
        end = time.monotonic() + args.soak * 60
        soak = []
        while time.monotonic() < end:
            trial = runner.test({k: best[k] for k in initial}, ppl)
            if not trial["pass"] or trial["tg"] < best["tg"] * .93:
                raise RuntimeError("Selected settings failed soak; no recommendation saved")
            soak.append(trial["tg"])
        best["tg"] = statistics.median(soak)
        record = {"fingerprint": identity, "best": best, "baseline_tg": base_tg,
                  "measured_gain_percent": 100 * (best["tg"] / base_tg - 1),
                  "soak_minutes": args.soak, "run": str(directory)}
        atomic_json(directory / "result.json", record)
        atomic_json(args.results / "best.json", record)
        print(f"Result saved: {args.results / 'best.json'}; measured gain {record['measured_gain_percent']:.1f}%")
        print(f"Suggested llama.cpp flags: -t {best['threads']} -tb {best['threads']} -b 512 -ub {best['ubatch']} -fa on -ctk {args.kv} -ctv {args.kv}")
        return {"status": "completed", "model": str(model), "run": str(directory),
                "best": str(args.results / "best.json"), "record": record}
    finally:
        if args.frequency and recovery.exists():
            restore(xe, recovery)
            print("Original GPU frequency floor restored.")


def positive(value):
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return n


def run_all(args, xe):
    entries = model_catalog(args)
    if not entries:
        raise ValueError(f"No existing GGUF model entries found under {args.models_root}")
    batch = args.results / f"all-models-{time.strftime('%Y%m%d-%H%M%S')}"
    batch.mkdir(parents=True, exist_ok=False)
    summary = {"models_root": str(args.models_root.resolve()), "presets": str(args.presets.resolve()),
               "mode": args.mode, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
               "models": []}
    atomic_json(batch / "catalog.json", [{"alias": e["alias"], "aliases": e["aliases"],
                                          "model": str(e["model"]), "slug": e["slug"]} for e in entries])
    for entry in entries:
        model_args = copy.copy(args)
        model_args.model = entry["model"]
        model_args.alias = entry["alias"]
        model_args.results = batch / entry["slug"]
        model_args.results.mkdir()
        print(f"MODEL {entry['alias']}: {entry['model']}", flush=True)
        try:
            result = tune(model_args, xe, entry["model"])
            summary["models"].append({"alias": entry["alias"], "aliases": entry["aliases"],
                                      "model": str(entry["model"]), **(result or {"status": "unknown"})})
        except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError, KeyboardInterrupt) as exc:
            summary["models"].append({"alias": entry["alias"], "aliases": entry["aliases"],
                                      "model": str(entry["model"]), "status": "failed", "error": str(exc)})
            print(f"MODEL {entry['alias']} FAILED: {exc}", file=sys.stderr, flush=True)
            if isinstance(exc, KeyboardInterrupt):
                raise
    summary["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    summary["completed"] = sum(row["status"] in ("baseline", "completed") for row in summary["models"])
    summary["failed"] = sum(row["status"] == "failed" for row in summary["models"])
    atomic_json(batch / "summary.json", summary)
    print(f"All-model summary saved: {batch / 'summary.json'}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=["prepare", "preflight", "baseline", "run", "reset", "apply"], nargs="?", default="preflight")
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    p.add_argument("--card", default="card0")
    p.add_argument("--presets", type=Path, default=DEFAULT_PRESETS)
    p.add_argument("--models-root", type=Path, default=DEFAULT_MODELS_ROOT)
    p.add_argument("--alias", default="qwen-coder-7b")
    p.add_argument("--model", type=Path)
    p.add_argument("--corpus", type=Path, default=HERE / "corpus.txt")
    p.add_argument("--results", type=Path, default=HERE / "results")
    p.add_argument("--context", type=positive, default=4096)
    p.add_argument("--chunks", type=positive, default=4)
    p.add_argument("--kv", choices=["f16", "q8_0"], default="q8_0")
    p.add_argument("--threads", nargs="+", type=positive, default=[6, 4, 8, 12])
    p.add_argument("--ubatches", nargs="+", type=positive, choices=[128, 256, 512], default=[256, 128, 512])
    p.add_argument("--soak", type=positive, default=10, help="minimum soak duration in minutes")
    p.add_argument("--timeout", type=positive, default=900, help="seconds per subprocess")
    p.add_argument("--temp-limit", type=positive, default=80)
    p.add_argument("--frequency", action="store_true", help="also sweep Xe minimum frequency within existing maximum; requires sudo")
    p.add_argument("--freq-step", type=positive, default=150)
    p.add_argument("--resume", action="store_true", help="retest previous recommendation, then retest candidates")
    p.add_argument("--all-models", action="store_true", help="run independently for every existing preset GGUF under --models-root")
    p.add_argument("--dry-run", action="store_true", help="show commands only; no sudo, workload or GPU writes")
    args = p.parse_args()
    if args.dry_run and args.mode not in ("preflight", "baseline", "run"):
        p.error("--dry-run is only valid with preflight, baseline or run")
    if args.temp_limit > 80:
        p.error("--temp-limit must be <= 80 C for this host profile")
    if args.context < 512:
        p.error("--context must be >= 512")
    if args.all_models and args.model:
        p.error("--all-models cannot be combined with --model")
    if args.all_models and args.mode not in ("baseline", "run"):
        p.error("--all-models is only valid with baseline or run")
    if os.geteuid() == 0 and args.mode in ("baseline", "run") and not args.dry_run:
        p.error("Run as your normal user; the runner requests sudo only for privileged operations")
    try:
        if args.mode == "prepare":
            prepare(args)
            return
        xe = Xe(args.card)
        if args.all_models:
            if args.dry_run:
                for entry in model_catalog(args):
                    print(f"{entry['alias']}\t{entry['model']}")
                return
            args.results.mkdir(parents=True, exist_ok=True)
            with (HERE / f".{args.card}.lock").open("w") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                run_all(args, xe)
            return
        if args.mode == "apply":
            record = json.loads((args.results / "best.json").read_text())
            if fingerprint(args, resolve_model(args), xe) != record["fingerprint"]:
                raise ValueError("Saved recommendation does not match this model/build/configuration")
            best = record["best"]
            print(f"-t {best['threads']} -tb {best['threads']} -b 512 -ub {best['ubatch']} -fa on -ctk {args.kv} -ctv {args.kv}")
            print(f"Tested GPU minimum: {best['min_freq']} MHz. apply only prints recommendations; it changes no settings.")
            return
        if args.mode == "reset":
            with (HERE / f".{args.card}.lock").open("w") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                path = HERE / "results" / f"restore-{args.card}.json"
                if not path.exists():
                    print("No pending frequency changes to restore.")
                    return
                subprocess.run(["sudo", "-v"], check=True)
                restore(xe, path)
                print("Recovery complete.")
            return
        model = resolve_model(args)
        bench, ppl, env = tool_commands(args, model, 6, 256)
        if args.dry_run:
            print("\n".join(shlex.join(cmd) for cmd in (bench, ppl)))
            return
        for path in [Path(bench[0]), Path(bench[1]), Path(ppl[1]), args.corpus]:
            if not path.is_file():
                raise ValueError(f"Missing {path}; run python3 gpu-push.py prepare")
        if args.mode == "preflight":
            for command in (bench[:2], ppl[:2]):
                subprocess.run(command + ["--help"], env=env, check=True, timeout=60,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(json.dumps({"gpu": xe.identity(), "frequency_mhz": xe.limits(),
                              "telemetry": xe.sample(args.temp_limit), "model": str(model),
                              "nvtop": shutil.which("nvtop"), "active_llama_server_pids": active_servers(),
                              "kernel_log": "sudo access checked when baseline/run starts",
                              "memory_overclock": "unsupported", "power_changes": "disabled: no advertised cap bounds"}, indent=2))
            return
        args.results.mkdir(parents=True, exist_ok=True)
        with (HERE / f".{args.card}.lock").open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
            tune(args, xe, model)
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError, KeyboardInterrupt) as exc:
        print(f"STOP: {exc or 'interrupted'}", file=sys.stderr)
        sys.exit(1)
