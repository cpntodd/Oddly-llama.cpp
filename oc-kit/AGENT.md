# oc-kit: Intel Arc B580 / Xe host port

Host profile: Intel Arc B580 (PCI 0000:09:00.0), Linux xe driver, Ryzen 5 2600
(6 cores / 12 threads). **NVTOP is the GPU monitoring application.**

Read README.md before using the runner. User performs the full performance and
stability tests; do not launch sweeps just to verify edits.

## Design and scope

- `gpu-push.py` delegates to `oc_intel.py`; `gpu-tune.sh` is a convenience entry.
- `--all-models` reads all existing `.gguf` paths in model entries from
  `presets.ini` under `--models-root`, then runs each model independently with
  isolated results and a batch summary. It does not scan projector/image folders.
- `watch.py` launches NVTOP. Machine telemetry comes from Xe sysfs/hwmon, not
  screen scraping NVTOP or using NVIDIA tools.
- Default `run` tests CPU thread counts and microbatch sizes, measuring pp512 and
  tg128 at 4096-token depth. It keeps q8_0 KV and flash attention fixed.
- Optional `--frequency` raises the render GT minimum frequency in 150 MHz steps
  within the current maximum, rp0 and rpa limits. Original minimum is restored.
- This host currently exposes 400–2850 MHz bounds, with 1200 MHz minimum and
  2850 MHz maximum configured. Frequency floors are not NVIDIA V/F offsets.
  No memory offsets, voltage writes, power changes, BIOS modifications or boot
  persistence are implemented. Report no speedup without measured results.
- Use the existing matched oneAPI/Level Zero launcher and local library path.
  Do not replace or rebuild the user's known-good runtime.
- `prepare` links a local perplexity executable against the existing
  `libllama-perplexity-impl.so`; the earlier review mistook a missing executable
  for an unavailable correctness workload. It also creates a fixed stress corpus.

## Correctness and safety

- Require full GPU offload, successful exit of both tools, finite benchmark/PPL
  values, and three identical baseline perplexities before testing candidates.
- Exact printed PPL matching is a regression screen, not proof against every
  numerical error. The synthetic corpus is not a quality benchmark. Kernel or
  thermal failures abort; do not loosen checks to make a test pass.
- Poll all exposed temperature sensors; abort at 80 C or 5 C below a sensor's
  critical threshold, whichever is lower. Missing telemetry fails closed.
- Check new Xe/DRM errors using a kernel journal cursor. sudo is used for journal
  access, credential refresh and optional bounded sysfs writes. Models run as
  the invoking user. Never stop/kill unrelated GPU processes or services.
- Store results atomically only after the soak. `finally` restores the original
  frequency floor on normal exit, failure, Ctrl-C or SIGTERM. SIGKILL/power loss
  cannot run cleanup: retain recovery snapshot for `reset`.
- Resume requires matching model metadata/header, shared libraries, corpus and
  workload settings. It rechecks the baseline and candidates, not blindly skips.
- Original NVIDIA code is preserved under `legacy/` for reference only.

## Validation

`python3 -m unittest -v test_oc_intel.py`

`python3 gpu-push.py prepare`

`python3 gpu-push.py preflight`

`python3 gpu-push.py run --dry-run`

These checks do not constitute live inference, overclock stability or measured
performance proof. Use the user's run logs for those claims.
