import json
import io
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.registry.load import load_snapshot
from upgradeables_harness.registry.snapshot import verify_snapshot
from upgradeables_harness.registry.update import check_for_update


class PackagedDataTests(unittest.TestCase):
    def test_snapshot_matches_canonical_registry(self):
        source = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        snapshot = load_snapshot()
        self.assertEqual(snapshot["manifest"]["registry_version"], "0.2.1")
        self.assertEqual(snapshot["manifest"]["aggregate_registry_schema_version"], "1.0.0")
        self.assertEqual(snapshot["manifest"]["component_schema_version"], "2.0.0")
        self.assertEqual(
            {item["slug"] for item in source["upgradeables"]},
            {item["slug"] for item in snapshot["catalog"]["components"]},
        )
        self.assertEqual(
            {item["slug"] for item in source["recipes"]},
            {item["slug"] for item in snapshot["recipes"]["recipes"]},
        )
        self.assertEqual(len(snapshot["profiles"]["profiles"]), 10)
        components = {item["slug"] for item in snapshot["catalog"]["components"]}
        recipes = {item["slug"] for item in snapshot["recipes"]["recipes"]}
        for profile in snapshot["profiles"]["profiles"]:
            self.assertLessEqual(set(profile["likely_recipes"]), recipes, profile["slug"])
            self.assertLessEqual(set(profile["likely_exclusions"]), recipes, profile["slug"])
            self.assertLessEqual(set(profile["candidate_cross_cutting"]), components, profile["slug"])
        self.assertTrue(all(item["source_url"].startswith("https://github.com/")
                            for item in snapshot["catalog"]["components"]))

    def test_snapshot_hash_verifies(self):
        valid, actual = verify_snapshot()
        self.assertTrue(valid, actual)

    def test_generated_data_is_current(self):
        result = subprocess.run(
            [sys.executable, "scripts/build_harness_data.py", "--check"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_configuration_has_entrypoint(self):
        import tomllib
        data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertEqual(data["project"]["version"], "0.3.0")
        self.assertEqual(data["project"]["scripts"]["upgradeables"], "upgradeables_harness.cli:main")
        self.assertIn("data/*.json", data["tool"]["setuptools"]["package-data"]["upgradeables_harness"])

    def test_update_check_is_explicit_and_injectable(self):
        class Response(io.BytesIO):
            def __enter__(self):
                return self
            def __exit__(self, *args):
                self.close()
        def opener(request, timeout):
            self.assertEqual(request.full_url, "https://example.invalid/latest")
            self.assertEqual(timeout, 1)
            local = load_snapshot()
            payload = {
                "registry_version": "0.2.1",
                "upgradeables": local["catalog"]["components"],
                "recipes": local["recipes"]["recipes"],
            }
            return Response(json.dumps(payload).encode("utf-8"))
        result = check_for_update(opener=opener, url="https://example.invalid/latest", timeout=1)
        self.assertFalse(result["update_available"])
        self.assertEqual(result["remote_registry_version"], "0.2.1")
        self.assertTrue(result["network_used"])
        self.assertFalse(result["apply_supported"])


if __name__ == "__main__":
    unittest.main()
