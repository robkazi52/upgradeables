"""Bounded, deterministic stress checks for the v0.3 harness contract."""
from __future__ import annotations

import json
import random
import shutil
import string
import sys
import unittest
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upgradeables_harness.agents.managed_block import (
    END_MARKER,
    START_MARKER,
    ManagedBlockError,
    insert_or_update_managed_block,
    remove_managed_block,
)
from upgradeables_harness.harness.doctor import doctor_project
from upgradeables_harness.harness.init import initialize_project
from upgradeables_harness.project.inspect import inspect_project
from upgradeables_harness.registry.load import load_catalog
from upgradeables_harness.resolver.task import resolve_task
from upgradeables_harness.skills.common import SkillFactoryError, validate_slug
from scripts.build_release_assets import canonical_asset_bytes


def tree_fingerprint(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


class StressWorkspace(unittest.TestCase):
    def setUp(self):
        self.workspace = ROOT / f".harness-stress-{uuid.uuid4().hex}"
        self.workspace.mkdir()

    def tearDown(self):
        shutil.rmtree(self.workspace, ignore_errors=True)


class ResolverStressTests(unittest.TestCase):
    def test_paraphrase_matrix_is_deterministic_and_internally_consistent(self):
        verbs = ("review", "analyze", "debug", "summarize", "research")
        objects = (
            "this pull request",
            "the supplied sources",
            "a failing Python test",
            "a long design document",
            "an API migration plan",
        )
        constraints = (
            "without editing files",
            "with citations",
            "and explain the risks",
            "using only local evidence",
        )
        known = {item["slug"] for item in load_catalog()["components"]}
        groups = ("required_by_recipe", "trigger_likely", "conditional", "optional")

        for verb in verbs:
            for target in objects:
                for constraint in constraints:
                    task = f"Please {verb} {target} {constraint}."
                    with self.subTest(task=task):
                        first = resolve_task(task)
                        second = resolve_task(task)
                        self.assertEqual(first, second)
                        self.assertTrue(first["selection_only"])
                        selected = [item["slug"] for group in groups for item in first[group]]
                        excluded = {item["slug"] for item in first["excluded"]}
                        self.assertEqual(len(selected), len(set(selected)))
                        self.assertLessEqual(set(selected) | excluded, known)
                        self.assertTrue(set(selected).isdisjoint(excluded))


class ManagedBlockStressTests(unittest.TestCase):
    def test_newlines_unicode_and_random_host_text_are_stable(self):
        randomizer = random.Random(303)
        alphabet = string.ascii_letters + string.digits + " _-.,:/[]()" + "é中🙂"
        originals = ["", "plain", "plain\n", "windows\r\n", "é中🙂\n"]
        for _ in range(100):
            newline = "\r\n" if randomizer.randrange(2) else "\n"
            lines = [
                "".join(randomizer.choice(alphabet) for _ in range(randomizer.randrange(0, 70)))
                for _ in range(randomizer.randrange(1, 8))
            ]
            originals.append(newline.join(lines) + (newline if randomizer.randrange(2) else ""))

        for index, original in enumerate(originals):
            fragment = f"generated fragment {index}\nUnicode: é中🙂"
            with self.subTest(index=index):
                inserted = insert_or_update_managed_block(original, fragment)
                repeated = insert_or_update_managed_block(inserted.text, fragment)
                self.assertFalse(repeated.changed)
                self.assertEqual(repeated.text, inserted.text)
                self.assertEqual(inserted.text.count(START_MARKER), 1)
                self.assertEqual(inserted.text.count(END_MARKER), 1)
                removed = remove_managed_block(inserted.text)
                self.assertNotIn(START_MARKER, removed.text)
                self.assertNotIn(END_MARKER, removed.text)
                self.assertEqual(removed.text.rstrip("\r\n"), original.rstrip("\r\n"))

    def test_malformed_marker_fuzz_fails_closed(self):
        malformed = (
            START_MARKER,
            END_MARKER,
            END_MARKER + START_MARKER,
            START_MARKER * 2 + END_MARKER,
            START_MARKER + END_MARKER * 2,
            START_MARKER + " nested " + START_MARKER + END_MARKER,
        )
        for value in malformed:
            with self.subTest(value=value):
                with self.assertRaises(ManagedBlockError):
                    insert_or_update_managed_block(value, "safe fragment")


class HarnessStressTests(StressWorkspace):
    def test_release_asset_hashing_is_checkout_eol_independent(self):
        asset = self.workspace / "asset.md"
        asset.write_bytes(b"first\r\nsecond\r\n")
        self.assertEqual(canonical_asset_bytes(asset), b"first\nsecond\n")

    def test_concurrent_first_init_is_consistent(self):
        (self.workspace / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(initialize_project, self.workspace) for _ in range(8)]
            results = [future.result() for future in futures]
        self.assertEqual(doctor_project(self.workspace)["status"], "PASS")
        self.assertFalse((self.workspace / ".upgradeables/.init.lock").exists())
        self.assertTrue(any(result["created"] for result in results))
        before = tree_fingerprint(self.workspace / ".upgradeables")
        initialize_project(self.workspace)
        self.assertEqual(before, tree_fingerprint(self.workspace / ".upgradeables"))

    def test_repeated_init_handles_spaces_unicode_and_all_depths(self):
        for depth, name in (("minimal", "space path"), ("standard", "é中"), ("full", "full-depth")):
            project = self.workspace / name
            project.mkdir()
            (project / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
            with self.subTest(depth=depth, name=name):
                initialize_project(project, depth=depth)
                before = tree_fingerprint(project / ".upgradeables")
                for _ in range(20):
                    initialize_project(project, depth=depth)
                self.assertEqual(before, tree_fingerprint(project / ".upgradeables"))
                self.assertEqual(doctor_project(project)["status"], "PASS")

    def test_corrupt_and_unsafe_state_fails_closed(self):
        initialize_project(self.workspace)
        config = self.workspace / ".upgradeables/config.json"
        config.write_bytes(b'{"broken":')
        corrupted = config.read_bytes()
        result = doctor_project(self.workspace, fix=True)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("invalid-json", {item["code"] for item in result["diagnostics"]})
        self.assertEqual(config.read_bytes(), corrupted)

        initialize_project(self.workspace, force=True)
        value = json.loads(config.read_text(encoding="utf-8"))
        value["reference_roots"] = ["../outside-project"]
        config.write_text(json.dumps(value), encoding="utf-8")
        result = doctor_project(self.workspace)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("unsafe-reference-path", {item["code"] for item in result["diagnostics"]})

    def test_inspection_remains_shallow_under_deep_noise(self):
        (self.workspace / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
        marker = self.workspace / "executed.txt"
        (self.workspace / "setup.py").write_text(
            f"from pathlib import Path\nPath({str(marker)!r}).write_text('bad')\n",
            encoding="utf-8",
        )
        deep = self.workspace / "vendor/a/b/c/d/e"
        deep.mkdir(parents=True)
        for index in range(1000):
            (deep / f"noise-{index}.txt").write_text("not a project signal", encoding="utf-8")
        first = inspect_project(self.workspace)
        second = inspect_project(self.workspace)
        self.assertEqual(first, second)
        self.assertIn("python", first["languages"])
        self.assertFalse(marker.exists())

    def test_skill_slug_fuzz_cannot_escape_project(self):
        initialize_project(self.workspace)
        invalid = ("../escape", "a/b", "A-Caps", " leading", "two--hyphens", "", ".", "é")
        for slug in invalid:
            with self.subTest(slug=slug):
                with self.assertRaises(SkillFactoryError):
                    validate_slug(slug)
        self.assertFalse((self.workspace.parent / "escape").exists())


if __name__ == "__main__":
    unittest.main()
