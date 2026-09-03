import csv
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V02CompletenessTests(unittest.TestCase):
    def test_every_baseline_package_has_a_disposition(self):
        baseline = json.loads((ROOT / "audit/v0.1.0-operational-baseline.json").read_text(encoding="utf-8"))
        with (ROOT / "audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual({item["slug"] for item in baseline["packages"]}, {row["slug"] for row in rows})
        self.assertTrue(all(row["final_status"] in {"PASS", "BLOCKED_BY_SOURCE_GAP"} for row in rows))

    def test_every_package_has_v02_semantics_and_cases(self):
        for path in ROOT.glob("upgradeables/*/*/metadata.yaml"):
            item = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(item["schema_version"], "2.0.0", item["slug"])
            self.assertEqual(item["version"], "1.1.0", item["slug"])
            for key in ("os_role", "pipeline_stages", "best_fit_tasks", "avoid_when", "source_refs"):
                self.assertTrue(item[key], f"{item['slug']}: {key}")
            cases = path.parent / "tests/cases.json"
            example = path.parent / "examples/basic.md"
            source_note = ROOT / "audit/source-notes" / f"{item['slug']}.md"
            self.assertTrue(cases.is_file(), item["slug"])
            self.assertTrue(example.is_file(), item["slug"])
            self.assertTrue(source_note.is_file(), item["slug"])

    def test_semantic_auditor_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/audit_semantic_specificity.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_behavior_cases_pass(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_behavior_cases.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_readme_registry_example_executes(self):
        registry = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        research = next(
            recipe["classifications"]
            for recipe in registry["recipes"]
            if recipe["slug"] == "research-skill"
        )
        self.assertIn("task-set-lock-in", research)

    def test_deterministic_package_checks_pass(self):
        result = subprocess.run(
            [sys.executable, "scripts/run_deterministic_package_checks.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
