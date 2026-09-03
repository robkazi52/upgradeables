import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def estimated_tokens(path):
    return len(path.read_text(encoding="utf-8")) / 4


class RuntimeProjectionTests(unittest.TestCase):
    def test_runtime_build_is_current(self):
        result = subprocess.run(
            [sys.executable, "scripts/build_runtime.py", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_expected_projection_counts(self):
        self.assertEqual(len(list((ROOT / "runtime/components").glob("*.md"))), 96)
        self.assertEqual(len(list((ROOT / "runtime/recipes").glob("*.md"))), 17)
        self.assertEqual(len(list((ROOT / "dist/recipe-packs").glob("*.md"))), 17)

    def test_low_context_budgets(self):
        cards = list((ROOT / "runtime/components").glob("*.md"))
        packs = list((ROOT / "runtime/recipes").glob("*.md"))
        self.assertLessEqual(max(map(estimated_tokens, cards)), 800)
        self.assertLessEqual(max(map(estimated_tokens, packs)), 10_000)
        self.assertLessEqual(estimated_tokens(ROOT / "runtime/router.json"), 3_000)
        self.assertLessEqual(estimated_tokens(ROOT / "dist/OFFLINE_START.md"), 1_500)

    def test_cards_identify_canonical_source(self):
        registry = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        for item in registry["upgradeables"]:
            card = (ROOT / f"runtime/components/{item['slug']}.md").read_text(encoding="utf-8")
            self.assertIn(f"`{item['slug']}@{item['version']}`", card)
            self.assertIn(item["purpose"], card)
            self.assertIn(item["package_path"], card)

    def test_offline_packs_use_portable_links(self):
        link = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for path in (ROOT / "dist/recipe-packs").glob("*.md"):
            targets = link.findall(path.read_text(encoding="utf-8"))
            self.assertTrue(all(target.startswith(("https://", "#")) for target in targets), path.name)


if __name__ == "__main__":
    unittest.main()
