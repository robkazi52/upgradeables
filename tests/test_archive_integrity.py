import hashlib
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ArchiveTests(unittest.TestCase):
    def test_archived_sources_match_manifest(self):
        for line in (ROOT / "archive/SOURCE_SHA256SUMS").read_text(encoding="utf-8").splitlines():
            digest, relative = line.split("  ", 1)
            actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
            self.assertEqual(digest, actual, relative)
