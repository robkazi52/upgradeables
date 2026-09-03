import json
import unittest
from pathlib import Path

from scripts.run_deterministic_package_checks import CHECKS, evaluate_fixture


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/fixtures/deterministic_package_cases.json"


class DeterministicPackageChecksTests(unittest.TestCase):
    def test_canonical_fixture_has_positive_and_negative_case_per_checker(self):
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        expectations = {name: set() for name in CHECKS}
        for case in fixture["cases"]:
            expectations[case["check"]].add(case["expected"])
        self.assertEqual(set(CHECKS), set(expectations))
        for check, observed in expectations.items():
            self.assertEqual({True, False}, observed, check)
        self.assertEqual([], evaluate_fixture(fixture))

    def test_deliberately_invalid_behavior_fixture_fails_evaluation(self):
        fixture = {
            "schema_version": "1.1.0",
            "cases": [
                {
                    "id": "invalid-stateblock-claimed-valid",
                    "package": "stateblock",
                    "check": "required_stateblock_fields",
                    "input": {"state": {"task": "audit"}},
                    "expected": True,
                }
            ],
        }
        failures = evaluate_fixture(fixture)
        self.assertEqual(1, len(failures))
        self.assertIn("invalid-stateblock-claimed-valid", failures[0])
        self.assertIn("expected True, got False", failures[0])

    def test_malformed_fixture_is_rejected_before_execution(self):
        with self.assertRaisesRegex(ValueError, "unknown check"):
            evaluate_fixture(
                {
                    "schema_version": "1.1.0",
                    "cases": [
                        {
                            "id": "unknown-check",
                            "package": "stateblock",
                            "check": "always_true",
                            "input": {},
                            "expected": True,
                        }
                    ],
                }
            )


if __name__ == "__main__":
    unittest.main()
