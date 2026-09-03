import subprocess
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class BuildTests(unittest.TestCase):
    def test_registry_is_reproducible(self):
        result = subprocess.run([sys.executable, "scripts/build_registry.py", "--check"], cwd=ROOT)
        self.assertEqual(result.returncode, 0)
    def test_all_in_one_is_reproducible(self):
        result = subprocess.run([sys.executable, "scripts/build_all_in_one.py", "--check"], cwd=ROOT)
        self.assertEqual(result.returncode, 0)
    def test_all_in_one_has_core_sections(self):
        text = (ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md").read_text(encoding="utf-8")
        for heading in ("Start Here", "Model Consumption Guide", "Quick Task Prompt", "Build a Skill Prompt", "Skill Recipe Matrix", "Current Registry Summaries", "Unresolved Records"):
            self.assertIn(heading, text)
        self.assertIn("name: <lowercase-skill-name>", text)
        self.assertIn("name: source-bounded-research", text)
