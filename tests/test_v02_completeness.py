import csv
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V02CompletenessTests(unittest.TestCase):
    SKILL_TYPES = {
        "analysis and decision support",
        "communication and content generation",
        "document and code transformation",
        "high-stakes evidence work",
        "long-context workflows",
        "multi-step task execution",
        "review and quality assurance",
        "skill and agent workflows",
        "source-grounded research",
        "structured problem solving",
    }

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
            for key in ("plain_display_name", "task_phrases"):
                self.assertTrue(item[key], f"{item['slug']}: {key}")
            self.assertTrue(set(item["recommended_skill_types"]) <= self.SKILL_TYPES, item["slug"])
            self.assertNotEqual(item["recommended_skill_types"], item["best_fit_tasks"], item["slug"])
            cases = path.parent / "tests/cases.json"
            example = path.parent / "examples/basic.md"
            source_note = ROOT / "audit/source-notes" / f"{item['slug']}.md"
            self.assertTrue(cases.is_file(), item["slug"])
            self.assertTrue(example.is_file(), item["slug"])
            self.assertTrue(source_note.is_file(), item["slug"])

    def test_source_refs_resolve_to_markdown_headings(self):
        source_dir = ROOT / "archive/source"
        headings_by_document = {}
        for path in source_dir.glob("*.md"):
            headings_by_document[path.name] = {
                match.group(1).strip()
                for line in path.read_text(encoding="utf-8").splitlines()
                if (match := re.match(r"^#{1,6}\s+(.+)$", line))
            }
        for path in ROOT.glob("upgradeables/*/*/metadata.yaml"):
            item = json.loads(path.read_text(encoding="utf-8"))
            for source_ref in item["source_refs"]:
                self.assertIn(source_ref["document"], headings_by_document, item["slug"])
                self.assertIn(
                    source_ref["heading"],
                    headings_by_document[source_ref["document"]],
                    f"{item['slug']}: {source_ref['heading']}",
                )

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
