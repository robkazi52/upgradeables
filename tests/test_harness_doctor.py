import json
import shutil
import sys
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upgradeables_harness.harness.doctor import doctor_project
from upgradeables_harness.harness.init import initialize_project


class HarnessDoctorTests(unittest.TestCase):
    def setUp(self):
        self.project = ROOT / f".harness-doctor-test-{uuid.uuid4().hex}"
        self.project.mkdir()
        (self.project / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
        initialize_project(self.project)

    def tearDown(self):
        shutil.rmtree(self.project, ignore_errors=True)

    def test_doctor_clean(self):
        result = doctor_project(self.project)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["diagnostics"][0]["code"], "harness-clean")

    def test_doctor_clean_minimal_install(self):
        other = self.project.parent / f"{self.project.name}-minimal"
        other.mkdir()
        try:
            initialize_project(other, depth="minimal")
            self.assertEqual(doctor_project(other)["status"], "PASS")
        finally:
            shutil.rmtree(other, ignore_errors=True)

    def test_doctor_unknown_component(self):
        lock_path = self.project / ".upgradeables/lock.json"
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        lock["components"]["not-a-component"] = "1.0.0"
        lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
        result = doctor_project(self.project)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("unknown-component", {item["code"] for item in result["diagnostics"]})

    def test_doctor_fixes_only_stale_harness_fragment(self):
        fragment = self.project / ".upgradeables/agents/codex.md"
        fragment.write_text("stale\n", encoding="utf-8")
        before_project = (self.project / "pyproject.toml").read_bytes()
        result = doctor_project(self.project, fix=True)
        self.assertEqual(result["status"], "PASS")
        self.assertIn(".upgradeables/agents/codex.md", result["fixed"])
        self.assertEqual((self.project / "pyproject.toml").read_bytes(), before_project)
        stable = fragment.read_bytes()
        second = doctor_project(self.project, fix=True)
        self.assertEqual(second["fixed"], [])
        self.assertEqual(fragment.read_bytes(), stable)

    def test_doctor_does_not_repair_malformed_host_block(self):
        host = self.project / "AGENTS.md"
        original = b"user\n<!-- upgradeables-harness:start -->\n"
        host.write_bytes(original)
        result = doctor_project(self.project, fix=True)
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(host.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
