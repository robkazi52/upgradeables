import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class AliasTests(unittest.TestCase):
    def test_plain_display_names_are_unique(self):
        owners = {}
        for path in ROOT.glob("upgradeables/*/*/metadata.yaml"):
            item = json.loads(path.read_text(encoding="utf-8"))
            normalized = item["plain_display_name"].casefold()
            self.assertNotIn(normalized, owners, f"{item['slug']} / {owners.get(normalized)}")
            owners[normalized] = item["slug"]

    def test_operational_aliases_are_unambiguous(self):
        items = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))["upgradeables"]
        owners = {}
        for item in items:
            for alias in item["historical_aliases"]:
                owners.setdefault(alias.casefold(), set()).add(item["slug"])
        self.assertFalse({alias: values for alias, values in owners.items() if len(values) > 1})
    def test_itfc_collision_is_split(self):
        data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        current = {x["slug"]: x for x in data["upgradeables"]}
        unresolved = {x["slug"]: x for x in data["unresolved_records"]}
        self.assertIn("ITFC", current["image-text-fidelity-capture"]["historical_aliases"])
        self.assertIn("intent-task-framing-controller", unresolved)
        self.assertEqual(unresolved["intent-task-framing-controller"]["operational_status"], "archival_only")
