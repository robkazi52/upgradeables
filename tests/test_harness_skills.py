import contextlib
import io
import json
import shutil
import subprocess
import sys
import unittest
import uuid
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upgradeables_harness.skills.brief import build_skill_brief, command_brief
from upgradeables_harness.skills.history import (
    history_path,
    load_task_events,
    record_task_event,
)
from upgradeables_harness.skills.map import ensure_skill_map, validate_skill_map
from upgradeables_harness.skills.scaffold import (
    command_list,
    command_scaffold,
    scaffold_skill,
)
from upgradeables_harness.skills.suggest import analyze_skill_suggestions, command_suggest
from upgradeables_harness.skills.validate import (
    command_validate,
    validate_project_skill,
    validate_skill_path,
)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


@contextlib.contextmanager
def workspace():
    root = ROOT / "tests" / "fixtures" / "harness" / f"generated-{uuid.uuid4().hex}"
    root.mkdir()
    try:
        yield root
    finally:
        shutil.rmtree(root)


def make_harness(root: Path, *, record: bool = False) -> None:
    base = root / ".upgradeables"
    write_json(
        base / "project.json",
        {
            "schema_version": "1.0.0",
            "registry_version": "0.2.1",
            "project_root": ".",
            "languages": ["python"],
            "frameworks": [],
            "project_types": ["software-development"],
            "selected_profiles": ["software-development"],
            "features": {
                "git": True,
                "tests": True,
                "documentation": False,
                "ci": True,
                "pull_requests": True,
                "long_context": False,
            },
            "signals": [],
            "likely_task_families": ["code-review"],
            "host_capabilities": {
                "shell": "available",
                "web": "unknown",
                "durable_state": "project-files",
                "parallel_agents": "unknown",
            },
        },
    )
    write_json(
        base / "config.json",
        {
            "schema_version": "1.0.0",
            "profile_mode": "auto",
            "install_depth": "standard",
            "preferred_profiles": [],
            "agent_integrations": [],
            "record_task_events": record,
            "skill_suggestion_threshold": 3,
            "reference_roots": [],
            "network": {"allow_registry_update": False},
        },
    )


class SkillMapTests(unittest.TestCase):
    def test_ensure_skill_map_is_stable_and_valid(self):
        with workspace() as root:
            make_harness(root)
            first = ensure_skill_map(root)
            before = (root / ".upgradeables" / "skill-map.json").read_bytes()
            second = ensure_skill_map(root)
            self.assertEqual(first, second)
            self.assertEqual(before, (root / ".upgradeables" / "skill-map.json").read_bytes())
            self.assertEqual([], validate_skill_map(first))
            self.assertEqual("0.3.0", first["harness_version"])
            self.assertTrue((root / ".upgradeables" / "skills" / "README.md").is_file())


class SkillBriefAndScaffoldTests(unittest.TestCase):
    task = "Review this pull request for breaking changes to the exported Python API. Do not edit files."

    def test_brief_uses_resolver_and_registry_pins(self):
        with workspace() as root:
            make_harness(root)
            ensure_skill_map(root)
            brief = build_skill_brief(self.task, root)
            self.assertEqual("code-review", brief["primary_recipe"])
            self.assertIn("task-set-lock-in@1.1.0", brief["required_components"])
            self.assertTrue(all("@" in item for item in brief["selected_component_pins"]))
            self.assertEqual("candidate-brief", brief["status"])

    def test_scaffold_is_draft_valid_and_does_not_overwrite(self):
        with workspace() as root:
            make_harness(root)
            ensure_skill_map(root)
            result = scaffold_skill(root, "api-review", task=self.task)
            path = root / result["skill"]["path"]
            first = path.read_bytes()
            validation = validate_skill_path(path, draft=True)
            self.assertTrue(validation["valid"], validation["errors"])
            self.assertIn("draft contains TODO placeholders", validation["warnings"])
            with self.assertRaisesRegex(RuntimeError, "not empty"):
                scaffold_skill(root, "api-review", task=self.task)
            self.assertEqual(first, path.read_bytes())
            mapped = ensure_skill_map(root)
            self.assertEqual("draft", mapped["skills"][0]["status"])

    def test_frozen_command_handlers_return_codes_and_json(self):
        with workspace() as root:
            make_harness(root)
            ensure_skill_map(root)
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(0, command_brief(Namespace(task=self.task, project=str(root), json=True)))
            self.assertEqual("code-review", json.loads(stream.getvalue())["primary_recipe"])
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, command_scaffold(Namespace(slug="api-review", task=None, project=str(root), force=False, json=True)))
                self.assertEqual(0, command_list(Namespace(project=str(root), json=True)))
                self.assertEqual(0, command_validate(Namespace(path=str(root / ".upgradeables/skills/api-review"), draft=True, json=True)))
                self.assertEqual(0, command_suggest(Namespace(project=str(root), json=True)))


class FinalSkillValidationTests(unittest.TestCase):
    def test_synthetic_project_skill_passes_both_validators(self):
        fixture = ROOT / "tests" / "fixtures" / "harness" / "api-breaking-change-review"
        result = validate_skill_path(fixture)
        self.assertTrue(result["valid"], result["errors"])
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py"), str(fixture)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)

    def test_project_validator_uses_map_status(self):
        example = ROOT / "examples" / "harness" / "python-project" / "after-init"
        results = validate_project_skill(example, "api-breaking-change-review")
        self.assertEqual(1, len(results))
        self.assertTrue(results[0]["valid"], results[0]["errors"])
        self.assertEqual("final", results[0]["mode"])


class SkillHistoryAndSuggestionTests(unittest.TestCase):
    def _event(self, index: int) -> dict:
        return {
            "timestamp": f"2026-09-0{index + 1}T12:00:00Z",
            "raw_task": "Review API compatibility",
            "normalized_task": "review api compatibility",
            "task_archetype": "evaluation-audit",
            "selected_recipe": "code-review",
            "project_constraints": ["python", "public API"],
            "output_contract": {"shape": "prioritized compatibility findings"},
            "authority_mode": "review-only",
            "component_composition": [
                "grounding-no-invention@1.1.0",
                "task-set-lock-in@1.1.0",
            ],
            "required_inputs": ["diff", "API contract"],
            "activation_boundary": "public Python API compatibility review only",
            "procedure_signature": ["scope", "compare contract", "report findings"],
            "chain_of_thought": "must never be stored",
            "outcome": {
                "status": "reviewed",
                "private_reasoning": "must not survive nested normalization",
            },
        }

    def test_history_is_off_by_default_and_filters_private_reasoning(self):
        with workspace() as root:
            make_harness(root, record=False)
            ensure_skill_map(root)
            self.assertIsNone(record_task_event(root, self._event(0)))
            self.assertFalse(history_path(root).exists())
            saved = record_task_event(root, self._event(0), explicitly_requested=True)
            self.assertNotIn("chain_of_thought", saved)
            self.assertNotIn("chain_of_thought", history_path(root).read_text(encoding="utf-8"))
            self.assertNotIn("private_reasoning", history_path(root).read_text(encoding="utf-8"))

    def test_suggestion_requires_repetition_and_never_creates_skill(self):
        with workspace() as root:
            make_harness(root, record=True)
            ensure_skill_map(root)
            empty = analyze_skill_suggestions(root)
            self.assertEqual("not-enough-history", empty["status"])
            for index in range(3):
                record_task_event(root, self._event(index))
            result = analyze_skill_suggestions(root)
            self.assertEqual("candidate", result["status"])
            self.assertFalse(result["writes_performed"])
            self.assertEqual(3, result["suggestions"][0]["occurrence_count"])
            self.assertFalse(
                (root / ".upgradeables" / "skills" / "review-api-compatibility").exists()
            )
            events = load_task_events(root)
            self.assertEqual(3, len(events))
            self.assertTrue(all("chain_of_thought" not in event for event in events))
            self.assertEqual([], ensure_skill_map(root)["skills"])


if __name__ == "__main__":
    unittest.main()
