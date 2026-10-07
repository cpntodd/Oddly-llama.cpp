#!/usr/bin/env python3
"""GPU detection and backend dispatch for OC-Kit."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

VENDORS = {
    "0x10de": "nvidia",
    "0x1002": "amd",
    "0x8086": "intel",
}


def _read(path):
    try:
        return Path(path).read_text().strip()
    except OSError:
        return ""


def detect_gpu(sysfs=Path("/sys")):
    """Return one stable GPU description without changing system state."""
    cards = []
    for vendor_path in sorted((sysfs / "class/drm").glob("card[0-9]*/device/vendor")):
        card = vendor_path.parent.parent.name
        device = vendor_path.parent
        vendor_id = _read(vendor_path).lower()
        driver_path = device / "driver"
        driver = driver_path.resolve().name if driver_path.exists() else "unknown"
        item = {
            "card": card,
            "vendor_id": vendor_id or "unknown",
            "vendor": VENDORS.get(vendor_id, "other"),
            "device_id": _read(device / "device") or "unknown",
            "driver": driver,
        }
        cards.append(item)

    if cards:
        preferred = next((item for item in cards if item["vendor"] in VENDORS.values()), cards[0])
        return {"backend": preferred["vendor"], "selected": preferred, "cards": cards,
                "source": "sysfs"}

    if shutil.which("nvidia-smi"):
        return {"backend": "nvidia", "selected": {"vendor": "nvidia"}, "cards": [],
                "source": "nvidia-smi"}
    if shutil.which("rocminfo") or shutil.which("rocm-smi"):
        return {"backend": "amd", "selected": {"vendor": "amd"}, "cards": [],
                "source": "rocm"}
    return {"backend": "other", "selected": {"vendor": "other"}, "cards": [],
            "source": "fallback"}


def choose_backend(info, override="auto"):
    if override != "auto":
        if override not in ("intel", "nvidia", "amd", "other"):
            raise ValueError(f"unknown backend {override}")
        return override
    return info["backend"]


def preflight(info, backend):
    implementation = {
        "intel": "oc_intel.py (Xe/SYCL runner)",
        "nvidia": "legacy/gpu-push-nvidia.py (NVML offset runner)",
        "amd": "generic monitor-only backend (no safe AMD clock writer bundled)",
        "other": "generic monitor-only backend (no vendor clock writer bundled)",
    }[backend]
    return {
        "backend": backend,
        "implementation": implementation,
        "gpu": info,
        "nvtop": shutil.which("nvtop"),
        "capabilities": {
            "tuning": backend in ("intel", "nvidia"),
            "monitoring": bool(shutil.which("nvtop")),
            "model_sweep": backend == "intel",
        },
    }


def _legacy_path():
    return Path(__file__).resolve().parent / "legacy/gpu-push-nvidia.py"


def _run_legacy(argv):
    return subprocess.run([sys.executable, str(_legacy_path()), *argv]).returncode


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    override = "auto"
    if "--backend" in argv:
        index = argv.index("--backend")
        if index + 1 >= len(argv):
            raise SystemExit("--backend requires intel, nvidia, amd, other or auto")
        override = argv[index + 1]
        del argv[index:index + 2]

    info = detect_gpu()
    backend = choose_backend(info, override)
    mode = next((arg for arg in argv if not arg.startswith("-")), "preflight")
    dry_run = "--dry-run" in argv

    if mode == "detect":
        print(json.dumps(preflight(info, backend), indent=2))
        return

    if backend == "intel":
        from oc_intel import main as intel_main
        sys.argv = [sys.argv[0], *argv]
        intel_main()
        return

    if mode in ("detect", "preflight") or dry_run:
        print(json.dumps(preflight(info, backend), indent=2))
        if backend in ("amd", "other") and mode not in ("detect", "preflight"):
            raise SystemExit("No safe tuning backend is available for this GPU; monitoring/preflight only")
        return

    if backend == "nvidia":
        if "--all-models" in argv:
            raise SystemExit("--all-models is currently supported by the Intel runner only")
        raise SystemExit(_run_legacy(argv))

    raise SystemExit("No safe tuning backend is available for this GPU; use preflight or NVTOP")


if __name__ == "__main__":
    main()
