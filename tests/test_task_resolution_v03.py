import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.resolver.task import resolve_task

LEVEL = {f"L{value}": value for value in range(6)}


class TaskResolutionV03Tests(unittest.TestCase):
    def test_research_first_fixture(self):
        cases = json.loads((ROOT / "tests/fixtures/task_resolution_v03.json").read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(task=case["task"]):
                result = resolve_task(case["task"])
                self.assertEqual(result["task"]["archetype"], case["archetype"])
                self.assertEqual(result["best_recipe"]["slug"] if result["best_recipe"] else None, case["recipe"])
                self.assertTrue(result["selection_only"])
                required = {item["slug"] for item in result["required_by_recipe"]}
                self.assertLessEqual(set(case.get("required", [])), required)
                if case.get("review_only"):
                    self.assertIs(result["environment"]["review_only"], True)
                if case.get("minimum_floor"):
                    self.assertGreaterEqual(LEVEL[result["complexity"]["floor"]], LEVEL[case["minimum_floor"]])
                if case.get("maximum_ceiling"):
                    self.assertLessEqual(LEVEL[result["complexity"]["ceiling"]], LEVEL[case["maximum_ceiling"]])

    def test_stable_order_and_output(self):
        task = "review this pull request for bugs and regressions"
        self.assertEqual(resolve_task(task), resolve_task(task))

    def test_review_only_never_selects_mutation_components(self):
        result = resolve_task("review this patch, do not modify files")
        self.assertIn("review-only-boundary", {item["id"] for item in result["matched_prior_rules"]})
        selected = {
            item["slug"] for key in ("required_by_recipe", "trigger_likely", "conditional", "optional")
            for item in result[key]
        }
        self.assertTrue(selected.isdisjoint({"micro-repair", "surgery-edit", "crispr-edit", "safe-rewrite"}))

    def test_simple_edit_uses_composition_suppression_without_recipe(self):
        result = resolve_task("rename this heading from Foo to Bar")
        self.assertIsNone(result["best_recipe"])
        self.assertIn("simple-exact-edit-suppression", {item["id"] for item in result["matched_prior_rules"]})
        self.assertIn("micro-repair", {item["slug"] for item in result["trigger_likely"]})
        self.assertIn("meta-supervisor", {item["slug"] for item in result["excluded"]})

    def test_no_citations_is_an_explicit_exclusion(self):
        result = resolve_task("research this without citations")
        excluded = {item["slug"] for item in result["excluded"]}
        self.assertIn("citation-fidelity", excluded)

    def test_project_context_breaks_under_specified_tie(self):
        software = resolve_task("review this change", {"project_types": ["software-development"]})
        research = resolve_task("review this change", {"project_types": ["research-and-knowledge"]})
        self.assertEqual(software["best_recipe"]["slug"], "code-review")
        self.assertEqual(research["best_recipe"]["slug"], "source-grounded-analysis")

    def test_explicit_task_outweighs_project_profile(self):
        result = resolve_task(
            "review this pull request for regressions",
            {"project_types": ["research-and-knowledge"]},
        )
        self.assertEqual(result["best_recipe"]["slug"], "code-review")

    def test_resolution_does_not_touch_network(self):
        with patch("socket.create_connection", side_effect=AssertionError("network used")):
            result = resolve_task("research five supplied sources")
        self.assertEqual(result["best_recipe"]["slug"], "research-skill")

    def test_all_emitted_references_are_canonical(self):
        source = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        known = {item["slug"] for item in source["upgradeables"]}
        result = resolve_task("review this pull request for bugs and regressions")
        emitted = {item["slug"] for key in (
            "required_by_recipe", "trigger_likely", "conditional", "optional", "excluded",
            "needs_agent_evaluation",
        ) for item in result[key]}
        self.assertLessEqual(emitted, known)


if __name__ == "__main__":
    unittest.main()
