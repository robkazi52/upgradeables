import json
import shutil
import sys
import unittest
import uuid
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upgradeables_harness.harness.init import command_init, initialize_project
from upgradeables_harness.project.inspect import inspect_project
from upgradeables_harness.project.profile import PROFILE_ORDER, recommend_project
from upgradeables_harness.project.root import resolve_project_root
from upgradeables_harness.registry.load import load_catalog, load_recipes, load_profiles


class WorkspaceCase(unittest.TestCase):
    def setUp(self):
        self.project = ROOT / f".harness-b-test-{uuid.uuid4().hex}"
        self.project.mkdir()

    def tearDown(self):
        shutil.rmtree(self.project, ignore_errors=True)


class ProjectInspectionTests(WorkspaceCase):
    def test_explicit_root_wins(self):
        nested = self.project / "a" / "b"
        nested.mkdir(parents=True)
        resolution = resolve_project_root(self.project, start=nested)
        self.assertEqual(resolution.root, self.project.resolve())
        self.assertEqual(resolution.source, "explicit")

    def test_nearest_harness_precedes_git_and_manifest(self):
        (self.project / ".upgradeables").mkdir()
        (self.project / ".git").mkdir()
        (self.project / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
        nested = self.project / "a" / "b"
        nested.mkdir(parents=True)
        resolution = resolve_project_root(start=nested)
        self.assertEqual(resolution.root, self.project.resolve())
        self.assertEqual(resolution.source, "nearest-harness")

    def test_inspect_python_project_is_shallow_and_deterministic(self):
        fixture = ROOT / "tests/fixtures/projects/python-lib"
        first = inspect_project(fixture)
        second = inspect_project(fixture)
        self.assertEqual(first, second)
        self.assertEqual(first["languages"], ["python"])
        self.assertTrue(first["features"]["tests"])
        self.assertTrue(first["features"]["ci"])
        self.assertEqual(first["host_capabilities"]["web"], "unknown")

    def test_inspect_empty_project(self):
        result = inspect_project(ROOT / "tests/fixtures/projects/empty")
        self.assertEqual(result["project_types"], ["general"])
        self.assertEqual(result["signals"], [])

    def test_all_profile_fixtures(self):
        expected = {
            "typescript-web": "typescript",
            "rust-cli": "rust",
            "research-corpus": None,
            "docs-only": None,
            "agent-project": None,
        }
        for name, language in expected.items():
            with self.subTest(name=name):
                result = inspect_project(ROOT / "tests/fixtures/projects" / name)
                if language:
                    self.assertIn(language, result["languages"])
                self.assertTrue(result["signals"])

    def test_inspection_and_init_do_not_use_network(self):
        (self.project / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
        with patch("socket.create_connection", side_effect=AssertionError("network attempted")):
            inspect_project(self.project)
            initialize_project(self.project, depth="minimal")

    def test_inspection_does_not_execute_project_code(self):
        marker = self.project / "executed.txt"
        (self.project / "setup.py").write_text(
            f"from pathlib import Path\nPath({str(marker)!r}).write_text('bad')\n",
            encoding="utf-8",
        )
        result = inspect_project(self.project)
        self.assertIn("python", result["languages"])
        self.assertFalse(marker.exists())


class ProfileRecommendationTests(unittest.TestCase):
    def test_all_ten_profiles_ship(self):
        self.assertEqual(len(PROFILE_ORDER), 10)

    def test_recommend_python_project(self):
        result = recommend_project(ROOT / "tests/fixtures/projects/python-lib")
        self.assertTrue(result["selection_only"])
        self.assertEqual(result["registry_version"], "0.2.1")
        self.assertEqual(result["likely_recipes"][:3], ["coding-debugging", "code-review", "architecture-skill-building"])
        self.assertIn("task-set-lock-in", result["candidate_cross_cutting"])

    def test_packaged_profile_references_are_canonical(self):
        profiles = load_profiles()["profiles"]
        recipes = {item["slug"] for item in load_recipes()["recipes"]}
        components = {item["slug"] for item in load_catalog()["components"]}
        self.assertEqual({item["slug"] for item in profiles}, set(PROFILE_ORDER))
        for profile in profiles:
            self.assertLessEqual(set(profile["likely_recipes"]), recipes)
            self.assertLessEqual(set(profile["candidate_cross_cutting"]), components)


class HarnessInitTests(WorkspaceCase):
    def setUp(self):
        super().setUp()
        (self.project / "pyproject.toml").write_text("[project]\n", encoding="utf-8")

    def snapshot(self):
        return {
            path.relative_to(self.project).as_posix(): path.read_bytes()
            for path in self.project.rglob("*")
            if path.is_file()
        }

    def test_init_minimal(self):
        result = initialize_project(self.project, depth="minimal")
        base = self.project / ".upgradeables"
        self.assertEqual(result["depth"], "minimal")
        self.assertTrue((base / "project.json").is_file())
        self.assertTrue((base / "config.json").is_file())
        self.assertTrue((base / "lock.json").is_file())
        self.assertTrue((base / "agents/generic.md").is_file())
        self.assertFalse((base / "task-map.json").exists())
        self.assertFalse((base / "agents/codex.md").exists())

    def test_init_standard_and_lock_versions(self):
        initialize_project(self.project)
        base = self.project / ".upgradeables"
        self.assertTrue((base / "task-map.json").is_file())
        self.assertTrue((base / "skill-map.json").is_file())
        self.assertTrue((base / "agents/codex.md").is_file())
        lock = json.loads((base / "lock.json").read_text(encoding="utf-8"))
        self.assertEqual(lock["harness_version"], "0.4.0")
        self.assertEqual(lock["registry_version"], "0.2.1")

    def test_explicit_profile_is_fixed(self):
        initialize_project(self.project, profile="research", no_detect=True)
        project = json.loads((self.project / ".upgradeables/project.json").read_text(encoding="utf-8"))
        config = json.loads((self.project / ".upgradeables/config.json").read_text(encoding="utf-8"))
        self.assertEqual(project["selected_profiles"], ["research"])
        self.assertEqual(config["profile_mode"], "fixed")

    def test_init_is_byte_idempotent(self):
        initialize_project(self.project)
        before = self.snapshot()
        result = initialize_project(self.project)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(result["created"])
        self.assertFalse(result["updated"])

    def test_init_preserves_differing_harness_file_without_force(self):
        initialize_project(self.project)
        config = self.project / ".upgradeables/config.json"
        custom = b'{"user_owned_preference":true}\n'
        config.write_bytes(custom)
        result = initialize_project(self.project)
        self.assertEqual(config.read_bytes(), custom)
        self.assertIn(".upgradeables/config.json", result["preserved"])

    def test_init_never_writes_host_agent_files(self):
        agents = self.project / "AGENTS.md"
        agents.write_text("user instructions\n", encoding="utf-8")
        initialize_project(self.project, force=True)
        self.assertEqual(agents.read_text(encoding="utf-8"), "user instructions\n")

    def test_init_full_creates_explicit_runtime_state(self):
        initialize_project(self.project, depth="full")
        base = self.project / ".upgradeables/runtime"
        self.assertTrue((base / "task-events.jsonl").is_file())
        self.assertTrue((base / "session").is_dir())

    def test_command_init_json_contract(self):
        args = Namespace(path=str(self.project), profile=None, no_detect=False, minimal=True, standard=False, full=False, force=False, json=True)
        self.assertEqual(command_init(args), 0)


class HarnessSchemaTests(unittest.TestCase):
    def test_b_schemas_are_valid_json(self):
        for name in ("PROJECT_PROFILE_SCHEMA.json", "HARNESS_CONFIG_SCHEMA.json", "HARNESS_LOCK_SCHEMA.json", "TASK_MAP_SCHEMA.json"):
            with self.subTest(name=name):
                value = json.loads((ROOT / "spec/harness" / name).read_text(encoding="utf-8"))
                self.assertEqual(value["$schema"], "https://json-schema.org/draft/2020-12/schema")


if __name__ == "__main__":
    unittest.main()
