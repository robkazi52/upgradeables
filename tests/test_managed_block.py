import shutil
import sys
import unittest
import uuid
from argparse import Namespace
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upgradeables_harness.agents.base import command_integrate
from upgradeables_harness.agents.managed_block import (
    END_MARKER,
    START_MARKER,
    ManagedBlockError,
    insert_or_update_managed_block,
    remove_managed_block,
)
from upgradeables_harness.harness.init import initialize_project


class ManagedBlockUnitTests(unittest.TestCase):
    def test_insert_and_repeat_are_idempotent(self):
        first = insert_or_update_managed_block("user\n", "generated")
        second = insert_or_update_managed_block(first.text, "generated")
        self.assertTrue(first.changed)
        self.assertFalse(second.changed)
        self.assertEqual(first.text, second.text)

    def test_update_preserves_outside_bytes(self):
        first = insert_or_update_managed_block("before\r\nafter", "one")
        updated = insert_or_update_managed_block(first.text, "two")
        self.assertTrue(updated.text.startswith("before\r\nafter\r\n"))
        self.assertIn("two", updated.text)
        self.assertNotIn("one", updated.text)

    def test_remove_preserves_everything_outside_markers(self):
        source = f"before\n{START_MARKER}\nmanaged\n{END_MARKER}\nafter\n"
        removed = remove_managed_block(source)
        self.assertEqual(removed.text, "before\n\nafter\n")

    def test_malformed_or_double_markers_fail_closed(self):
        for text in (START_MARKER, END_MARKER, START_MARKER + START_MARKER + END_MARKER, END_MARKER + START_MARKER):
            with self.subTest(text=text):
                with self.assertRaises(ManagedBlockError):
                    insert_or_update_managed_block(text, "content")


class IntegrationCommandTests(unittest.TestCase):
    def setUp(self):
        self.project = ROOT / f".harness-agent-test-{uuid.uuid4().hex}"
        self.project.mkdir()
        initialize_project(self.project)

    def tearDown(self):
        shutil.rmtree(self.project, ignore_errors=True)

    def call(self, **overrides):
        values = {"provider": "codex", "project": str(self.project), "write": False, "remove": False, "json": False}
        values.update(overrides)
        with redirect_stdout(StringIO()):
            return command_integrate(Namespace(**values))

    def test_preview_never_writes(self):
        self.assertEqual(self.call(), 0)
        self.assertFalse((self.project / "AGENTS.md").exists())

    def test_write_update_remove_preserve_user_text(self):
        host = self.project / "AGENTS.md"
        host.write_bytes(b"user instructions\n")
        self.assertEqual(self.call(write=True), 0)
        first = host.read_bytes()
        self.assertIn(START_MARKER.encode(), first)
        self.assertEqual(self.call(write=True), 0)
        self.assertEqual(host.read_bytes(), first)
        self.assertEqual(self.call(remove=True), 0)
        self.assertEqual(host.read_bytes(), b"user instructions\n\n")

    def test_malformed_host_file_is_not_changed(self):
        host = self.project / "AGENTS.md"
        original = b"user\n<!-- upgradeables-harness:start -->\n"
        host.write_bytes(original)
        self.assertEqual(self.call(write=True), 1)
        self.assertEqual(host.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
