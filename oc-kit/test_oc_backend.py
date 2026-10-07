"""Backend selection tests; no real GPU access or tuning writes."""
import tempfile
import unittest
from pathlib import Path

import oc_backend as oc


class BackendTests(unittest.TestCase):
    def make_sysfs(self, vendor, device="0xe20b", driver="xe"):
        root = Path(tempfile.mkdtemp())
        device_dir = root / "class/drm/card0/device"
        device_dir.mkdir(parents=True)
        (device_dir / "vendor").write_text(vendor)
        (device_dir / "device").write_text(device)
        driver_dir = root / "drivers" / driver
        driver_dir.mkdir(parents=True)
        (device_dir / "driver").symlink_to(driver_dir)
        return root

    def test_detects_intel(self):
        info = oc.detect_gpu(self.make_sysfs("0x8086"))
        self.assertEqual(info["backend"], "intel")
        self.assertEqual(info["selected"]["driver"], "xe")

    def test_detects_nvidia_and_amd(self):
        self.assertEqual(oc.detect_gpu(self.make_sysfs("0x10de", "0x1f08", "nvidia"))["backend"], "nvidia")
        self.assertEqual(oc.detect_gpu(self.make_sysfs("0x1002", "0x73bf", "amdgpu"))["backend"], "amd")

    def test_unknown_vendor_is_safe(self):
        info = oc.detect_gpu(self.make_sysfs("0x1234", "0x5678", "unknown"))
        self.assertEqual(info["backend"], "other")
        self.assertFalse(oc.preflight(info, "other")["capabilities"]["tuning"])

    def test_override_is_explicit(self):
        info = {"backend": "other"}
        self.assertEqual(oc.choose_backend(info, "amd"), "amd")
        with self.assertRaises(ValueError):
            oc.choose_backend(info, "rocm")


if __name__ == "__main__":
    unittest.main()
