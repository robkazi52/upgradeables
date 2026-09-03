import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
    def test_populated(self):
        self.assertGreaterEqual(len(self.data["upgradeables"]), 70)
    def test_package_paths(self):
        for item in self.data["upgradeables"]:
            self.assertTrue((ROOT / item["package_path"]).is_file(), item["slug"])
    def test_dependencies_resolve(self):
        known = {item["slug"] for item in self.data["upgradeables"]}
        for item in self.data["upgradeables"]:
            for key in ("requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts"):
                self.assertLessEqual(set(item[key]), known)
