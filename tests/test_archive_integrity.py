import hashlib
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ArchiveTests(unittest.TestCase):
    def test_archived_sources_match_manifest(self):
        for line in (ROOT / "archive/SOURCE_SHA256SUMS").read_text(encoding="utf-8").splitlines():
            digest, relative = line.split("  ", 1)
            # Git may materialize Markdown with CRLF on Windows. The manifest
            # records canonical repository (LF) bytes.
            content = (ROOT / relative).read_bytes().replace(b"\r\n", b"\n")
            actual = hashlib.sha256(content).hexdigest()
            self.assertEqual(digest, actual, relative)
