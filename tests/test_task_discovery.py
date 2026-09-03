import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def query(*args):
    result = subprocess.run(
        [sys.executable, "scripts/query_registry.py", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


class TaskDiscoveryTests(unittest.TestCase):
    def test_task_fixtures(self):
        fixtures = json.loads((ROOT / "tests/fixtures/task_discovery.json").read_text(encoding="utf-8"))
        for case in fixtures:
            with self.subTest(task=case["task"]):
                data = query("--task", case["task"])
                best = data["best_recipe"]
                self.assertEqual(best["slug"] if best else None, case["recipe"])
                if case.get("skill"):
                    self.assertIn(case["skill"], {item["slug"] for item in data["existing_skills"]})
                for slug in case.get("conditional", []):
                    self.assertIn(slug, {item["slug"] for item in data["conditional"]})
                for slug in case.get("not_required", []):
                    self.assertNotIn(slug, {item["slug"] for item in data["required"]})
                for slug in case.get("not_anywhere", []):
                    self.assertNotIn(slug, json.dumps(data))

    def test_normalized_search_phrases(self):
        for phrase in ("pull request", "long context", "issue", "reproduce"):
            with self.subTest(phrase=phrase):
                self.assertTrue(query("--search", phrase, "--brief", "--limit", "5"))

    def test_brief_and_paths_are_small_and_actionable(self):
        component = query("--slug", "grounding-no-invention", "--brief")
        self.assertLessEqual(len(json.dumps(component)) / 4, 250)
        paths = query("--task", "research five sources", "--paths-only")
        self.assertEqual(paths[0], "runtime/recipes/research-skill.md")
        self.assertTrue(all((ROOT / path).is_file() for path in paths))

    def test_incompatible_projection_flags_fail_cleanly(self):
        result = subprocess.run(
            [sys.executable, "scripts/query_registry.py", "--slug", "stateblock", "--fields", "slug", "--paths-only"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot be combined", result.stderr)


if __name__ == "__main__":
    unittest.main()
