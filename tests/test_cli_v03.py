import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, "PYTHONPATH": str(ROOT / "src")}


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "upgradeables_harness", *args],
        cwd=ROOT, env=ENV, capture_output=True, text=True,
    )


class CliV03Tests(unittest.TestCase):
    def test_help_exposes_complete_command_surface(self):
        result = run_cli("--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("init", "inspect", "recommend", "task", "skill", "integrate", "doctor", "update", "version"):
            self.assertIn(command, result.stdout)

    def test_version_json_is_stable_and_uses_current_registry(self):
        result = run_cli("version", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["harness_version"], "0.3.0")
        self.assertEqual(payload["bundled_registry_version"], "0.2.1")
        self.assertEqual(payload["aggregate_registry_schema_version"], "1.0.0")
        self.assertEqual(payload["component_schema_version"], "2.0.0")

    def test_task_json_and_human_output(self):
        json_result = run_cli("task", "review this pull request", "--json")
        self.assertEqual(json_result.returncode, 0, json_result.stderr)
        self.assertEqual(json.loads(json_result.stdout)["best_recipe"]["slug"], "code-review")
        text_result = run_cli("task", "review this pull request", "--explain")
        self.assertEqual(text_result.returncode, 0, text_result.stderr)
        self.assertIn("Best recipe:\ncode-review", text_result.stdout)
        self.assertIn("selection candidates", text_result.stdout)

    def test_update_requires_explicit_check(self):
        result = run_cli("update")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--check", result.stderr)

    def test_apply_is_honestly_deferred(self):
        result = run_cli("update", "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not implemented", result.stderr)


if __name__ == "__main__":
    unittest.main()
