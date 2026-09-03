import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BehavioralEvalRunnerTests(unittest.TestCase):
    def test_mock_run_is_explicitly_non_evidence(self):
        result = subprocess.run(
            [
                sys.executable,
                "scripts/run_behavioral_evals.py",
                "--adapter", "mock",
                "--allow-mock",
                "--model", "mock",
                "--package", "grounding-no-invention",
                "--max-cases", "1",
                "--stdout",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["evidence_status"], "mock-not-evidence")
        self.assertEqual(report["case_count"], 1)
        self.assertIsNone(report["results"][0]["judgment"])

    def test_mock_requires_explicit_acknowledgment(self):
        result = subprocess.run(
            [
                sys.executable,
                "scripts/run_behavioral_evals.py",
                "--adapter", "mock",
                "--model", "mock",
                "--stdout",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--allow-mock", result.stderr)


if __name__ == "__main__":
    unittest.main()
