import json
import os
import subprocess
import sys
import shutil
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.harness.doctor import doctor_project
from upgradeables_harness.harness.init import initialize_project
from upgradeables_harness.resolver.task import resolve_task


def run_cli(*args, cwd=ROOT):
    return subprocess.run(
        [sys.executable, "-m", "upgradeables_harness", *args],
        cwd=cwd, env=ENV, capture_output=True, text=True,
    )


class RuntimeCliTests(unittest.TestCase):
    def setUp(self):
        self.root = ROOT / f".runtime-v04-test-{uuid.uuid4().hex}"
        self.root.mkdir()

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_compile_resolution_file_to_json(self):
        path = self.root / "resolution.json"
        path.write_text(json.dumps(resolve_task("say hello")), encoding="utf-8")
        result = run_cli("runtime", "compile", "--resolution", str(path), "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        self.assertEqual(plan["compiler_version"], "0.4.0")
        self.assertEqual(plan["instruction_capsule"], "")

    def test_runtime_profiles_json(self):
        result = run_cli("runtime", "profiles", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        profiles = json.loads(result.stdout)["profiles"]
        self.assertEqual(set(profiles), {"small", "medium", "strong", "auto", "custom"})

    def test_project_runtime_defaults_are_used(self):
        initialize_project(self.root, depth="minimal")
        config_path = self.root / ".upgradeables/config.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["runtime"]["default_model_profile"] = "strong"
        config["runtime"]["max_directive_tokens"] = 250
        config_path.write_text(json.dumps(config), encoding="utf-8")
        result = run_cli("runtime", "plan", "fix this one failing test", "--project", str(self.root))
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        self.assertEqual(plan["model_profile"], "strong")

    def test_runtime_explain_includes_traceability(self):
        result = run_cli("runtime", "explain", "review this patch, do not modify files")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Task archetype: evaluation-audit", result.stdout)
        self.assertIn("Directive provenance:", result.stdout)
        self.assertIn("No file edits", result.stdout)


class RuntimeDoctorTests(unittest.TestCase):
    def setUp(self):
        self.root = ROOT / f".runtime-v04-test-{uuid.uuid4().hex}"
        self.root.mkdir()

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_v03_lock_is_compatible_warning_not_failure(self):
        initialize_project(self.root, depth="minimal")
        lock_path = self.root / ".upgradeables/lock.json"
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        lock["harness_version"] = "0.3.0"
        lock_path.write_text(json.dumps(lock), encoding="utf-8")
        result = doctor_project(self.root)
        self.assertEqual(result["status"], "WARN")
        self.assertIn("compatible-v03-lock", {item["code"] for item in result["diagnostics"]})

    def test_invalid_runtime_config_fails(self):
        initialize_project(self.root, depth="minimal")
        config_path = self.root / ".upgradeables/config.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["runtime"]["default_model_profile"] = "marketing-tier"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        result = doctor_project(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("invalid-runtime-profile", {item["code"] for item in result["diagnostics"]})


if __name__ == "__main__":
    unittest.main()
