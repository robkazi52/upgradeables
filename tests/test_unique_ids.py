import re
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class IdentityTests(unittest.TestCase):
    def test_unique_ids_and_slugs(self):
        items = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))["upgradeables"]
        self.assertEqual(len(items), len({x["id"] for x in items}))
        self.assertEqual(len(items), len({x["slug"] for x in items}))
    def test_registry_generations_separate(self):
        data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        members = [x for x in data["historical_records"] if x["registry_generation"] == "frozen-t2-master-2025-11-28" and re.fullmatch(r"T2-\d{3}", x["historical_id"])]
        original = [x for x in members if x["source_document"] == "OS_Upgradeables_Historical_Recovery_Inventory.md"]
        resonance = [x for x in members if x["source_kind"] == "direct_user_spec"]
        provisional = [x for x in members if x["source_kind"] == "historical_assistant_artifact"]
        self.assertEqual((len(original), len(resonance), len(provisional)), (23, 6, 7))
        self.assertTrue(all(x["canonicality"] == "provisional" for x in provisional))
    def test_deep_recovery_does_not_fill_frozen_t1_gaps(self):
        data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        prefreeze = [x for x in data["historical_records"] if x["registry_generation"] == "t1-pre-freeze-library-2025-11-28"]
        self.assertEqual(len(prefreeze), 13)
        self.assertTrue(all(x["canonicality"] == "provisional" for x in prefreeze))
        unresolved = {x["slug"] for x in data["unresolved_records"]}
        self.assertNotIn("frozen-t2-resonance-members", unresolved)
        self.assertNotIn("frozen-t2-supervisor-members", unresolved)
