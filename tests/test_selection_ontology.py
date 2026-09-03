import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_OUTPUTS = (
    ROOT / "registry/upgradeable_task_priors.json",
    ROOT / "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.csv",
    ROOT / "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.md",
)
OUTPUTS_EXIST = all(path.is_file() for path in GENERATED_OUTPUTS)


@unittest.skipUnless(
    OUTPUTS_EXIST,
    "selection-ontology outputs have not been generated yet",
)
class SelectionOntologyTests(unittest.TestCase):
    def run_script(self, *arguments):
        return subprocess.run(
            [sys.executable, *arguments],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

    def test_selection_ontology_validator_passes(self):
        result = self.run_script("scripts/validate_selection_ontology.py")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_selection_ontology_compiler_outputs_are_current(self):
        result = self.run_script("scripts/build_selection_ontology.py", "--check")
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
