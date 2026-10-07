#!/usr/bin/env python3
"""NVTOP is the host GPU monitor; telemetry is also captured by the runner."""
import os
import shutil
import sys

if __name__ == "__main__":
    if not shutil.which("nvtop"):
        sys.exit("NVTOP is not installed (Debian package: nvtop)")
    os.execvp("nvtop", ["nvtop", *sys.argv[1:]])
