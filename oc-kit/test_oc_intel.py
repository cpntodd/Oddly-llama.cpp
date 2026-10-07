"""Guard and orchestration tests; no real GPU writes or model inference."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch, Mock

import oc_intel as oc


class ParsingTests(unittest.TestCase):
    def test_model_catalog_uses_existing_preset_ggufs_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "Models"
            root.mkdir()
            (root / "A.gguf").write_bytes(b"a")
            (root / "missing.gguf").write_bytes(b"")
            presets = Path(tmp) / "presets.ini"
            presets.write_text("[*]\n\n[a]\nmodel = " + str(root / "A.gguf") +
                               "\n[b]\nmodel = " + str(root / "missing.gguf") +
                               "\n[c]\nmodel = /outside/projector.gguf\n")
            args = argparse.Namespace(models_root=root, presets=presets)
            entries = oc.model_catalog(args)
            self.assertEqual(len(entries), 2)
            self.assertEqual(entries[0]["model"], root / "A.gguf")

    def test_model_slug_is_safe_and_bounded(self):
        self.assertEqual(oc.model_slug(Path("/x/model with spaces.gguf")), "model-with-spaces")
        self.assertLessEqual(len(oc.model_slug(Path("/x/" + "a" * 100 + ".gguf"))), 80)

    def test_bench_fields_and_nonfinite_rejection(self):
        rows = [{"n_prompt": 512, "n_gen": 0, "avg_ts": 123.4},
                {"n_prompt": 0, "n_gen": 128, "avg_ts": 45.6}]
        self.assertEqual(oc.parse_bench(json.dumps(rows)), {"pp": 123.4, "tg": 45.6})
        rows[1]["avg_ts"] = float("nan")
        with self.assertRaises(ValueError):
            oc.parse_bench(json.dumps(rows))

    def test_ppl_preserves_digits_and_rejects_missing(self):
        self.assertEqual(oc.parse_ppl("Final estimate: PPL = 8.123400 +/- 0.3"), "8.123400")
        for text in ["PPL = 8.123", "Final estimate: PPL = nan", "Final estimate: PPL = 0"]:
            with self.assertRaises(ValueError):
                oc.parse_ppl(text)

    def test_positive_sweep_parameters(self):
        for val in ["0", "-1"]:
            with self.assertRaises(argparse.ArgumentTypeError):
                oc.positive(val)

    def test_kernel_patterns(self):
        self.assertTrue(oc.ERROR_RE.search("xe 0000:09:00.0: [drm] GPU HANG"))
        self.assertTrue(oc.ERROR_RE.search("xe: GuC reset failed"))
        self.assertFalse(oc.ERROR_RE.search("usb: device reset"))


class HardwareTests(unittest.TestCase):
    def test_out_of_bounds_never_invokes_sudo(self):
        xe = object.__new__(oc.Xe)
        xe.freq = Path("/unused")
        xe.limits = lambda: dict(rpn_freq=400, max_freq=2850, rp0_freq=2850, rpa_freq=2850)
        with patch.object(oc.subprocess, "run") as run:
            for value in [0, 399, 2851, 3000]:
                with self.assertRaises(ValueError):
                    xe.set_floor(value)
            run.assert_not_called()

    def test_temperature_and_missing_sensor_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            xe = object.__new__(oc.Xe)
            xe.freq = Path(tmp)
            sensor = Path(tmp) / "temp1_input"
            xe.temps = [sensor]
            sensor.write_text("80000")
            with self.assertRaises(RuntimeError):
                xe.sample(80)
            sensor.unlink()
            with self.assertRaises(OSError):
                xe.sample(80)

    def test_restore_checks_gpu_and_boot(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "restore.json"
            xe = Mock()
            xe.identity.return_value = {"pci": "test"}
            oc.atomic_json(path, {"gpu": {"pci": "other"}})
            with self.assertRaises(ValueError):
                oc.restore(xe, path)
            xe.set_floor.assert_not_called()
            oc.atomic_json(path, {"gpu": xe.identity(), "boot": "old-boot", "min_freq": 1200})
            with contextlib.redirect_stdout(io.StringIO()):
                oc.restore(xe, path)
            xe.set_floor.assert_not_called()
            self.assertTrue(path.with_suffix(".previous-boot.json").exists())


class RunnerTests(unittest.TestCase):
    def runner(self, tmp):
        args = argparse.Namespace(temp_limit=80, timeout=10, chunks=4)
        xe = Mock()
        xe.sample.return_value = {"temperature_max_c": 50, "actual_mhz": 1200}
        return oc.Runner(args, xe, Path("model"), Mock(), Path(tmp))

    def test_nonzero_exit_cannot_pass_even_with_ppl_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            runner = self.runner(tmp)
            with self.assertRaisesRegex(RuntimeError, "exited 7"):
                runner.execute(["/bin/sh", "-c", "echo 'Final estimate: PPL = 8.1'; exit 7"], None, "ppl")

    def test_thermal_abort_terminates_child(self):
        with tempfile.TemporaryDirectory() as tmp:
            runner = self.runner(tmp)
            runner.xe.sample.side_effect = [{}, RuntimeError("too hot")]
            with self.assertRaisesRegex(RuntimeError, "too hot"):
                runner.execute(["/bin/sleep", "30"], None, "bench")

    def test_correctness_mismatch_is_not_pass(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(oc, "tool_commands", return_value=([], [], {})):
            runner = self.runner(tmp)
            rows = [{"n_prompt": 512, "n_gen": 0, "avg_ts": 100},
                    {"n_prompt": 0, "n_gen": 128, "avg_ts": 50}]
            runner.execute = Mock(side_effect=[(json.dumps(rows), "offloaded 29/29 layers to GPU"),
                                               ("Final estimate: PPL = 8.1235", "offloaded 29/29 layers to GPU\nperplexity: calculating perplexity over 4 chunks, n_ctx=4096")])
            with contextlib.redirect_stdout(io.StringIO()):
                result = runner.test(dict(threads=6, ubatch=256, min_freq=1200), "8.1234")
            self.assertFalse(result["pass"])

    def test_partial_offload_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(oc, "tool_commands", return_value=([], [], {})):
            runner = self.runner(tmp)
            runner.execute = Mock(return_value=("[]", "offloaded 20/29 layers to GPU"))
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaisesRegex(RuntimeError, "full GPU offload"):
                runner.test(dict(threads=6, ubatch=256))


class TuneTests(unittest.TestCase):
    def run_case(self, tmp, values, frequency=True, mode="run"):
        args = argparse.Namespace(results=Path(tmp) / "results", card="card0", mode=mode,
                                  threads=[6, 4], ubatches=[256], resume=False,
                                  frequency=frequency, freq_step=150, soak=1, kv="q8_0")
        args.results.mkdir(exist_ok=True)
        xe = Mock()
        xe.identity.return_value = {"pci": "fake"}
        xe.limits.return_value = dict(min_freq=1200, max_freq=1350, rp0_freq=1350, rpa_freq=1350)
        def result(settings, baseline_ppl=None):
            val = next(values)
            if isinstance(val, Exception):
                raise val
            return {**settings, "tg": 50, "pp": 100, "ppl": val, "pass": val == (baseline_ppl or val)}
        runner = Mock()
        runner.test.side_effect = result
        with patch.object(oc, "HERE", Path(tmp)), patch.object(oc, "active_servers", return_value=""), \
                patch.object(oc, "KernelLog"), patch.object(oc.subprocess, "run"), \
                patch.object(oc, "fingerprint", return_value={}), patch.object(oc, "Runner", return_value=runner), \
                contextlib.redirect_stdout(io.StringIO()):
            oc.tune(args, xe, Path("model"))
        return xe

    def test_baseline_no_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            xe = self.run_case(tmp, iter(["8.1"] * 3), mode="baseline")
            xe.set_floor.assert_not_called()

    def test_failed_trial_restores_and_does_not_save_best(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Capture restore independently of the local mock returned only on success.
            with patch.object(oc, "restore") as restore:
                with self.assertRaisesRegex(RuntimeError, "GPU fault"):
                    self.run_case(tmp, iter(["8.1"] * 3 + [RuntimeError("GPU fault")]))
                restore.assert_called_once()
            self.assertFalse((Path(tmp) / "results/best.json").exists())

    def test_nondeterminism_stops_before_recovery_or_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(oc, "restore") as restore:
                with self.assertRaisesRegex(RuntimeError, "nondeterministic"):
                    self.run_case(tmp, iter(["8.1", "8.2", "8.1"]))
                restore.assert_not_called()
            self.assertFalse((Path(tmp) / "results/restore-card0.json").exists())

    def test_successful_soak_saves_and_restores(self):
        with tempfile.TemporaryDirectory() as tmp:
            # End at 60; one complete soak trial, then elapsed time exceeds it.
            with patch.object(oc.time, "monotonic", side_effect=[0, 0, 61]):
                xe = self.run_case(tmp, iter(["8.1"] * 6))
            record = json.loads((Path(tmp) / "results/best.json").read_text())
            self.assertEqual(record["best"]["tg"], 50)
            self.assertEqual(record["measured_gain_percent"], 0)
            xe.set_floor.assert_called_with(1200)
            self.assertFalse((Path(tmp) / "results/restore-card0.json").exists())


if __name__ == "__main__":
    unittest.main()
