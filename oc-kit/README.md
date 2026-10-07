# OC-Kit with automatic GPU backend selection

The single `gpu-push.py` entry point detects the GPU through Linux DRM/sysfs
and selects the matching backend. Intel uses the full Xe/SYCL runner. NVIDIA
uses the preserved NVML legacy runner. AMD and other GPUs use a monitor-only,
fail-closed backend until a safe vendor-specific tuning implementation is
added; they never receive Intel or NVIDIA clock writes.

This port uses the existing Oddly-llama.cpp Intel SYCL build. **NVTOP monitors
the GPU.** It measures runtime settings and optionally tests bounded Xe core
frequency floors. It does not expose NVIDIA-style memory/core offsets.

Current host: Ryzen 5 2600, Arc B580, Xe driver. The configured GPU maximum is
already 2850 MHz, equal to the reported ceiling. A higher minimum may or may not
improve performance; the kit must measure this. No speedup is promised.

## Run it

Close GPU-heavy applications and stop your model server yourself before testing.
Keep the normal desktop and NVTOP running. The script does not stop services.
Run as your normal user, not `sudo python3 ...`. It requests sudo for kernel
journal access and, only with `--frequency`, sysfs writes.

```bash
cd /mnt/Data/Projects/Oddly-llama.cpp/llama.cpp/oc-kit
python3 gpu-push.py preflight
```

To inspect detection without any model or GPU operation:

```bash
python3 gpu-push.py detect
```

You can override detection for testing with `--backend intel`, `--backend
nvidia`, `--backend amd`, or `--backend other`. The override does not bypass
backend safety checks.

Preparation has already been performed on this host. After moving the kit or
changing the llama.cpp build, prepare again:

```bash
python3 gpu-push.py prepare
```

This links `bin/llama-perplexity` against the existing implementation library
and creates `corpus.txt` if absent. No downloads or llama.cpp source edits.

In a second terminal:

```bash
nvtop
# Equivalent: python3 /mnt/Data/Projects/Oddly-llama.cpp/llama.cpp/oc-kit/watch.py
```

Start with the three-run stock baseline. This changes no GPU settings:

```bash
python3 gpu-push.py baseline
```

If it passes, run software tuning and a ten-minute minimum soak:

```bash
python3 gpu-push.py run
```

To process every existing GGUF model represented by `presets.ini` under the
Models directory, run the same workflow sequentially for each model:

```bash
python3 gpu-push.py run --all-models
```

The catalogue is taken from model entries in `/mnt/Data/Projects/Models/presets.ini`.
Missing files, projector files and GGUFs outside `--models-root` are skipped.
Each model receives its own baseline, candidate sweep, correctness checks, soak,
`best.json`, and directory. The batch writes `catalog.json` and `summary.json`
under `results/all-models-<timestamp>/`; one failed model is recorded and does
not erase another model's result.

Preview the discovered catalogue without running inference:

```bash
python3 gpu-push.py run --all-models --dry-run
```

This is a long-running operation. With the default candidate matrix and soak,
the total time grows roughly with the number of models. Use `--soak 2`, a smaller
`--threads`/`--ubatches` list, or `baseline --all-models` for a first pass.

Default: `qwen-coder-7b` from `/mnt/Data/Projects/Models/presets.ini`, full
SYCL0 offload, 4096-token context/depth, q8_0 K/V, flash attention on, batch 512.
Tests threads 6/4/8/12 and microbatches 256/128/512. Each candidate runs a
three-repetition pp512/tg128 benchmark plus four perplexity chunks. This can
take considerably longer than the final ten-minute soak; allow an extended run.
Candidate selection targets decode speed; prompt speed is also recorded.

Optional combined software and GPU frequency-floor experiment:

```bash
python3 gpu-push.py run --frequency
```

This raises `tile0/gt0/freq0/min_freq` in 150 MHz steps within the driver's
existing maximum. It does not change the maximum, memory clock, voltage or
power limit. GPU settings restore on completion, failure or Ctrl-C. Save work
before the hardware experiment: a driver hang can still require rebooting.

For a smaller first software sweep (still includes baseline and soak):

```bash
python3 gpu-push.py run --threads 6 4 --ubatches 256 --soak 2
```

Other supported options:

```bash
python3 gpu-push.py run --dry-run
python3 gpu-push.py run --alias qwen3.5-9b
python3 gpu-push.py run --model '/absolute/path/model.gguf'
python3 gpu-push.py run --kv f16
python3 gpu-push.py run --resume
```

Use a model that fits fully into 12 GB VRAM with its KV cache. This profile
supports a single Intel GPU mapped to SYCL0. Defaults suit the dense 7B model;
other architectures may need a different context or KV type. Three unequal
stock PPL values stop the run before any hardware writes. Exact PPL comparisons
may reject harmless numerical differences from changing microbatch size; such
a rejection does not establish hardware instability.

## Results and applying them

Every run has a timestamped directory under `results/` with raw stdout/stderr,
`telemetry.jsonl`, `trials.jsonl`, and environment fingerprints. Only a passing
soak produces `results/best.json` and a per-run `result.json`. Baseline-only runs
produce `baseline.json` instead. Previous per-run results remain available.

```bash
python3 -m json.tool results/best.json
python3 gpu-push.py apply
```

`apply` validates the saved fingerprint and **prints recommended llama.cpp
flags only**. Add those to your own per-model configuration after reviewing the
results. It does not edit `presets.ini`, change clocks, start a server or install
a boot service. A result tested with a raised frequency minimum is conditional
on that setting; applying only its software flags may not reproduce its speed.

`--resume` revalidates the saved candidate and retests the sweep against a fresh
baseline. It requires the same model/build/corpus/context/KV settings; a changed
environment needs a fresh run. Add `--frequency` if the saved result used a
different GPU minimum. A new result replaces best.json only after passing soak.

The bundled repeated prose corpus is a deterministic **stress check**, not a
model quality dataset or exhaustive corruption detector. For representative
quality checking, supply a fixed local corpus with `--corpus /path/text.txt`.
It needs enough tokens for `--chunks 4 --context 4096` (at least 16384 tokens).
A passing short soak is evidence only for that workload and duration.

## Recovery

If a process was forcibly killed, run:

```bash
python3 gpu-push.py reset
```

This restores the original floor from `results/restore-card0.json`, validates
the GPU identity and removes the snapshot only after successful restoration.
A snapshot from another boot is archived instead of replaying stale settings.
No snapshot means no pending changes. The per-card lock prevents simultaneous
runs or resets. Recovery files stay in the kit's results directory even when
`--results` directs experiment logs elsewhere.

If preflight fails, keep its exact error. If a workload fails, inspect the
latest `*-bench.err` or `*-ppl.err`. Do not disable thermal/journal checks. A
missing sudo timestamp or kernel log access is an error, not a passing test.

## Implementation references

- [Xe frequency API](https://docs.kernel.org/gpu/xe/xe_gt_freq.html): min/max
  requests are bounded frequency policy controls; firmware decides actual clocks.
- Historical NVIDIA scripts and guide are preserved in `legacy/`.
- Developer contract: `AGENT.md`; tests: `python3 -m unittest -v test_oc_intel.py`.
