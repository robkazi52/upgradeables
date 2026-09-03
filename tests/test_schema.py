import json
import subprocess
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class SchemaTests(unittest.TestCase):
    def test_schema_files_are_valid_json(self):
        for path in (ROOT / "registry/schema").glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["type"], "object")
            self.assertIn("required", data)
    def test_every_metadata_has_required_schema_keys(self):
        required = set(json.loads((ROOT / "registry/schema/upgradeable.schema.json").read_text(encoding="utf-8"))["required"])
        for path in ROOT.glob("upgradeables/*/*/metadata.yaml"):
            self.assertLessEqual(required, set(json.loads(path.read_text(encoding="utf-8"))), str(path))
    def test_invalid_fixture_is_rejected(self):
        result = subprocess.run([sys.executable, "scripts/validate_upgradeable.py", "tests/fixtures/invalid_metadata.json"], cwd=ROOT, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
