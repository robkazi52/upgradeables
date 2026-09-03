import ast
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OnboardingTests(unittest.TestCase):
    def test_discovery_files_route_to_start_here(self):
        for relative in ("README.md", "AGENTS.md", "llms.txt", ".github/copilot-instructions.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("START_HERE.md", text, relative)

    def test_copy_ready_prompts_exist(self):
        for name in ("QUICK_TASK.md", "BUILD_A_SKILL.md", "RESEARCH_FROM_SOURCES.md", "WORK_WITH_LONG_DOCUMENTS.md"):
            self.assertTrue((ROOT / "prompts" / name).is_file(), name)

    def test_readme_python_examples_parse(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        examples = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
        self.assertTrue(examples)
        for example in examples:
            ast.parse(example)

    def test_recipe_query_resolves_components(self):
        result = subprocess.run(
            [sys.executable, "scripts/query_registry.py", "--recipe", "research-skill"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["slug"], "research-skill")
        self.assertTrue(all(item["package_path"] for item in data["components"]))

    def test_perception_recipe_is_discoverable(self):
        result = subprocess.run(
            [sys.executable, "scripts/query_registry.py", "--recipe", "perception-reasoning"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["task_family"], "grid puzzles, pattern completion, visual analogies, inductive rule inference, and spatial transformations")
        self.assertEqual(next(item["role"] for item in data["components"] if item["slug"] == "meta-supervisor"), "X")

    def test_common_code_review_terms_are_searchable(self):
        for term in ("review", "unsafe", "regressions", "pull-request", "correctness"):
            result = subprocess.run(
                [sys.executable, "scripts/query_registry.py", "--search", term],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout), term)

    def test_code_review_recipe_is_review_only(self):
        result = subprocess.run(
            [sys.executable, "scripts/query_registry.py", "--recipe", "code-review"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        slugs = {item["slug"] for item in data["components"]}
        self.assertIn("invariance-stress-scaffold", slugs)
        self.assertNotIn("micro-repair", slugs)

    def test_worked_skill_validates(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", "implementations/community/source-bounded-research"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_arc_skill_and_evidence_disclose_limits(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", "implementations/community/arc-perception-solver"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        evidence = (ROOT / "evidence/arc-agi-benchmarks.md").read_text(encoding="utf-8").casefold()
        for disclosure in ("not independently verified", "reconciliation warning", "raw run artifacts"):
            self.assertIn(disclosure, evidence)

    def test_incomplete_skill_is_rejected(self):
        skill = ROOT / "tests/fixtures/invalid-skill/SKILL.md"
        result = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", str(skill)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing section", result.stderr)
