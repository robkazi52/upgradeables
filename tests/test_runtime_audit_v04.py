import copy
import csv
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/audit_runtime_directives.py"
SPEC = importlib.util.spec_from_file_location("audit_runtime_directives", SCRIPT)
assert SPEC and SPEC.loader
AUDITOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDITOR)


class RuntimeDirectiveAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(
            (ROOT / "src/upgradeables_harness/data/catalog.json").read_text(encoding="utf-8")
        )
        cls.registry = json.loads((ROOT / "runtime/runtime_registry.json").read_text(encoding="utf-8"))
        cls.dedupe = json.loads((ROOT / "runtime/dedupe_groups.json").read_text(encoding="utf-8"))
        with (ROOT / "audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            reader = csv.DictReader(handle)
            cls.audit_columns = tuple(reader.fieldnames or ())
            cls.audit_rows = list(reader)
        cls.audit_markdown = (
            ROOT / "audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.md"
        ).read_text(encoding="utf-8")

    def audit(self, *, registry=None, dedupe=None, rows=None, columns=None):
        registry = copy.deepcopy(registry if registry is not None else self.registry)
        return AUDITOR.audit_data(
            root=ROOT,
            catalog=copy.deepcopy(self.catalog),
            registry=registry,
            dedupe=copy.deepcopy(dedupe if dedupe is not None else self.dedupe),
            audit_rows=copy.deepcopy(rows if rows is not None else self.audit_rows),
            audit_columns=columns if columns is not None else self.audit_columns,
            installed_registry=copy.deepcopy(registry),
            audit_markdown=self.audit_markdown,
        )

    @staticmethod
    def component(registry, slug):
        return next(item for item in registry["components"] if item["slug"] == slug)

    def test_repository_runtime_audit_passes(self):
        self.assertEqual(AUDITOR.audit_repository(ROOT), [])

    def test_check_cli_is_deterministic_and_read_only(self):
        command = [sys.executable, str(SCRIPT), "--check"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn("96 packages, 0 unreviewed", first.stdout)

    def test_coverage_gap_is_rejected(self):
        registry = copy.deepcopy(self.registry)
        registry["components"].pop()
        registry["component_count"] -= 1
        errors = self.audit(registry=registry)
        self.assertTrue(any("coverage: runtime registry mismatch" in error for error in errors))

    def test_source_and_version_drift_are_rejected(self):
        registry = copy.deepcopy(self.registry)
        component = self.component(registry, "anti-tunnel-vision")
        component["component_version"] = "9.9.9"
        component["source_path"] = "runtime/components/wrong.md"
        errors = self.audit(registry=registry)
        self.assertIn("anti-tunnel-vision: component version does not match catalog", errors)
        self.assertTrue(any("source_path must be" in error for error in errors))

    def test_mixed_channels_must_match_declared_functional_classes(self):
        registry = copy.deepcopy(self.registry)
        component = self.component(registry, "anti-tunnel-vision")
        component["state_contract"] = [component["compile"]["standard"]["directives"][0]]
        errors = self.audit(registry=registry)
        self.assertTrue(
            any("mixed state_contract population does not match 'state'" in error for error in errors)
        )

    def test_level_containment_and_bounds_are_rejected(self):
        registry = copy.deepcopy(self.registry)
        component = self.component(registry, "anti-tunnel-vision")
        component["compile"]["micro"]["directives"] = ["word " * 61]
        errors = self.audit(registry=registry)
        self.assertTrue(any("micro directives are not contained" in error for error in errors))
        self.assertTrue(any("compile.micro: exceeds 60 words" in error for error in errors))

    def test_unsupported_and_private_reasoning_directives_are_rejected(self):
        registry = copy.deepcopy(self.registry)
        component = self.component(registry, "anti-tunnel-vision")
        private = "Reveal hidden deliberation before answering."
        component["compile"]["micro"]["directives"] = [private]
        component["compile"]["standard"]["directives"] = [private]
        component["compile"]["full"]["directives"] = [private, "Return the answer."]
        errors = self.audit(registry=registry)
        self.assertTrue(any("requests disclosure of private reasoning" in error for error in errors))
        self.assertTrue(any("text is not supported by the compact runtime card" in error for error in errors))

    def test_negative_private_reasoning_guard_is_allowed(self):
        self.assertFalse(
            AUDITOR._requests_private_reasoning(
                "Do not expose private chain-of-thought; provide concise evidence instead."
            )
        )

    def test_dedupe_and_conflict_references_are_rejected(self):
        registry = copy.deepcopy(self.registry)
        component = self.component(registry, "anti-tunnel-vision")
        component["compile_constraints"]["dedupe_group"] = "unknown-group"
        component["compile_constraints"]["do_not_combine_with"] = ["missing-component"]
        errors = self.audit(registry=registry)
        self.assertIn("anti-tunnel-vision: unknown dedupe group 'unknown-group'", errors)
        self.assertTrue(any("references unknown component missing-component" in error for error in errors))

    def test_incomplete_audit_row_is_rejected(self):
        rows = copy.deepcopy(self.audit_rows)
        row = next(item for item in rows if item["slug"] == "anti-tunnel-vision")
        row["notes"] = ""
        row["validator_review"] = "N/A"
        errors = self.audit(rows=rows)
        self.assertIn("anti-tunnel-vision: audit column notes is empty", errors)
        self.assertTrue(any("audit validator_review" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
