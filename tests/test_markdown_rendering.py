import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class MarkdownRenderingTests(unittest.TestCase):
    def test_generated_headings_are_not_code_indented(self):
        targets = list(ROOT.glob("upgradeables/*/*/UPGRADEABLE.md")) + list((ROOT / "recipes").glob("*.md")) + list((ROOT / "bundles").glob("*/README.md"))
        bad = []
        for path in targets:
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if re.match(r" {4,}#{1,6} ", line):
                    bad.append(f"{path.relative_to(ROOT)}:{number}")
        self.assertFalse(bad, "indented headings render as code: " + ", ".join(bad[:20]))
