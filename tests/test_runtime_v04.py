import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.resolver.task import resolve_task
from upgradeables_harness.runtime import RuntimeCompileError, RuntimeCompileRequest, compile, compile_request, compile_task
from upgradeables_harness.runtime.adapters.generic import compose_instructions
from upgradeables_harness.runtime.adapters.ollama import build_ollama_request
from upgradeables_harness.runtime.adapters.openai_agents import apply_runtime_plan
from upgradeables_harness.runtime.adapters.openai_compatible import build_chat_completions_request
from upgradeables_harness.runtime.compiler import REQUIRED_RESOLUTION_FIELDS, canonical_hash
from upgradeables_harness.runtime.data import load_model_profiles, load_runtime_registry, runtime_components
from upgradeables_harness.runtime.manifest import build_manifest, redact_secrets


def resolution_with(*slugs):
    result = resolve_task("help with this")
    records = runtime_components()
    result["required_by_recipe"] = [
        {
            "slug": slug,
            "version": records[slug]["component_version"],
            "plain_display_name": slug,
            "recipe_role": "R",
            "status": "required-by-recipe",
            "reasons": ["test fixture"],
        }
        for slug in slugs
    ]
    result["trigger_likely"] = []
    return result


class RuntimeRegistryTests(unittest.TestCase):
    def test_runtime_schema(self):
        for path in (ROOT / "spec/runtime").glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertTrue(data["$id"].endswith(path.name))
            self.assertEqual(data["type"], "object")
            self.assertIn("required", data)
        task_schema = json.loads((ROOT / "spec/harness/TASK_RESOLUTION_SCHEMA.json").read_text(encoding="utf-8"))
        self.assertEqual(set(task_schema["required"]), REQUIRED_RESOLUTION_FIELDS)

    def test_all_operational_packages_have_runtime_review(self):
        registry = load_runtime_registry()
        source = json.loads((ROOT / "src/upgradeables_harness/data/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["component_count"], 96)
        self.assertEqual(
            {item["slug"] for item in registry["components"]},
            {item["slug"] for item in source["components"]},
        )
        rows = (ROOT / "audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(rows), 97)

    def test_not_every_package_is_injectable(self):
        records = runtime_components()
        self.assertFalse(records["behavior-gene-builder"]["runtime_injectable"])
        self.assertEqual(records["stateblock"]["runtime_form"], "state-contract")
        self.assertEqual(records["citation-fidelity"]["runtime_form"], "validator-check")

    def test_micro_standard_full_relationship(self):
        for record in load_runtime_registry()["components"]:
            sizes = [len(record["compile"][level]["directives"]) for level in ("micro", "standard", "full")]
            self.assertLessEqual(sizes[0], sizes[1], record["slug"])
            self.assertLessEqual(sizes[1], sizes[2], record["slug"])

    def test_model_profile_source_bundled_data_and_compiler_align(self):
        source = json.loads((ROOT / "runtime/model_profiles.json").read_text(encoding="utf-8"))
        self.assertEqual(source, load_model_profiles())
        request = resolution_with("anti-tunnel-vision")
        request["complexity"]["ceiling"] = "L5"
        for profile, specification in source["profiles"].items():
            with self.subTest(profile=profile):
                plan = compile(request, {"model_profile": profile, "max_directive_tokens": 2000})
                self.assertEqual(plan["components"][0]["runtime_level"], specification["default_level"])
        self.assertIn("does not yet", source["profiles"]["auto"]["description"])
        self.assertIn("not yet implemented", source["profiles"]["custom"]["description"])

        patched = copy.deepcopy(source)
        patched["profiles"]["small"]["default_level"] = "micro"
        with patch("upgradeables_harness.runtime.compiler.load_model_profiles", return_value=patched):
            plan = compile(request, {"model_profile": "small", "max_directive_tokens": 2000})
        self.assertEqual(plan["components"][0]["runtime_level"], "micro")

    def test_runtime_registry_build_is_current(self):
        result = subprocess.run(
            [sys.executable, "scripts/build_runtime_registry.py", "--check"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class RuntimeCompilerTests(unittest.TestCase):
    def test_runtime_compile_deterministic(self):
        request = resolve_task("fix the failing parser test without refactoring unrelated code")
        self.assertEqual(compile(request), compile(request))

    def test_runtime_compile_request_object(self):
        resolution = resolution_with("task-set-lock-in")
        request = RuntimeCompileRequest(resolution, model_profile="strong", max_directive_tokens=250)
        self.assertEqual(compile_request(request)["model_profile"], "strong")
        self.assertEqual(RuntimeCompileRequest.from_value(request.as_dict()).as_dict(), request.as_dict())

    def test_runtime_preserves_required_invariants(self):
        plan = compile(resolution_with("micro-repair"), {"model_profile": "strong"})
        self.assertIn("smallest-fault localization", plan["instruction_capsule"])

    def test_runtime_excludes_review_editing(self):
        request = resolution_with("micro-repair", "task-set-lock-in")
        request["environment"]["review_only"] = True
        plan = compile(request)
        self.assertIn("micro-repair", {item["slug"] for item in plan["excluded_runtime_components"]})

    def test_runtime_simple_task_minimal(self):
        plan = compile_task("rename this heading from Foo to Bar", model_profile="small")
        self.assertEqual([item["slug"] for item in plan["components"]], ["micro-repair"])
        self.assertFalse(plan["orchestration"])

    def test_runtime_small_profile_expands(self):
        request = resolution_with("anti-tunnel-vision")
        request["complexity"]["ceiling"] = "L4"
        small = compile(request, {"model_profile": "small", "max_directive_tokens": 2000})
        strong = compile(request, {"model_profile": "strong", "max_directive_tokens": 2000})
        self.assertGreater(len(small["instruction_capsule"]), len(strong["instruction_capsule"]))

    def test_runtime_strong_profile_compresses(self):
        plan = compile(resolution_with("anti-tunnel-vision"), {"model_profile": "strong"})
        self.assertEqual(plan["components"][0]["runtime_level"], "micro")

    def test_runtime_budget_compression(self):
        request = resolution_with("anti-tunnel-vision")
        request["complexity"]["ceiling"] = "L4"
        plan = compile(request, {"model_profile": "small", "max_directive_tokens": 120})
        self.assertTrue(any(item["type"] == "budget" for item in plan["decisions"]))

    def test_runtime_budget_required_overflow(self):
        plan = compile(resolution_with("task-set-lock-in"), {"max_directive_tokens": 0})
        self.assertTrue(any("exceeds budget" in warning for warning in plan["warnings"]))
        self.assertIn("objective", plan["instruction_capsule"])

    def test_runtime_dedupe(self):
        records = copy.deepcopy(runtime_components())
        duplicate = records["crispr-edit"]["compile"]["standard"]["directives"][0]
        records["micro-repair"]["compile"]["standard"]["directives"].insert(
            0, f"  {duplicate.upper()} .  "
        )
        with patch("upgradeables_harness.runtime.compiler.runtime_components", return_value=records):
            plan = compile(resolution_with("micro-repair", "crispr-edit"), {"max_directive_tokens": 2000})
        self.assertIn("Define a repair window", plan["instruction_capsule"])
        self.assertIn("Construct a patch contract", plan["instruction_capsule"])
        decisions = [item for item in plan["decisions"] if item["type"] == "dedupe"]
        self.assertTrue(decisions)
        suppressed = [
            item for item in plan["directive_provenance"]
            if item["component"] == "micro-repair" and not item["emitted"]
        ]
        self.assertEqual(len(suppressed), 1)
        self.assertIn("equivalent directive", suppressed[0]["suppression_reason"])

    def test_runtime_conflict_fail_closed(self):
        records = copy.deepcopy(runtime_components())
        records["micro-repair"]["compile_constraints"]["do_not_combine_with"] = ["crispr-edit"]
        with patch("upgradeables_harness.runtime.compiler.runtime_components", return_value=records):
            with self.assertRaises(RuntimeCompileError):
                compile(resolution_with("micro-repair", "crispr-edit"))

    def test_runtime_state_channel(self):
        plan = compile(resolution_with("stateblock"))
        self.assertTrue(plan["state_contract"])
        self.assertEqual(plan["instruction_capsule"], "")

    def test_runtime_validator_channel(self):
        plan = compile(resolution_with("citation-fidelity"))
        self.assertTrue(plan["validators"])
        self.assertEqual(plan["instruction_capsule"], "")

    def test_runtime_orchestration_channel(self):
        plan = compile(resolution_with("architect-orchestrator"))
        self.assertTrue(plan["orchestration"])
        self.assertEqual(plan["instruction_capsule"], "")

    def test_runtime_missing_capability(self):
        plan = compile(resolution_with("external-state-automation"))
        self.assertTrue(plan["tool_requirements"])
        self.assertFalse(plan["tool_requirements"][0]["available"])
        self.assertTrue(plan["warnings"])

    def test_runtime_manifest_hash(self):
        plan = compile(resolution_with("task-set-lock-in"))
        unhashed = {key: value for key, value in plan.items() if key != "manifest_hash"}
        self.assertEqual(plan["manifest_hash"], canonical_hash(unhashed))

    def test_invalid_resolution_fails_closed(self):
        request = resolve_task("help with this")
        del request["selection_only"]
        with self.assertRaises(RuntimeCompileError):
            compile(request)

    def test_task_resolution_contract_rejects_malformed_types_and_boundaries(self):
        with self.assertRaises(RuntimeCompileError):
            compile([])

        mutations = {
            "empty query": lambda value: value.__setitem__("query", ""),
            "empty normalized task": lambda value: value.__setitem__("normalized_task", "  "),
            "wrong registry version": lambda value: value.__setitem__("registry_version", "future"),
            "string hard restrictions": lambda value: value.__setitem__("hard_restrictions", "NO EDITS"),
            "non-string required check": lambda value: value.__setitem__("required_checks", [1]),
            "non-object task": lambda value: value.__setitem__("task", []),
            "non-object environment": lambda value: value.__setitem__("environment", []),
            "non-array failure modes": lambda value: value.__setitem__("failure_modes", {}),
            "non-array matched priors": lambda value: value.__setitem__("matched_prior_rules", {}),
            "non-array candidates": lambda value: value.__setitem__("candidates", {}),
            "non-object best recipe": lambda value: value.__setitem__("best_recipe", []),
            "empty activation note": lambda value: value.__setitem__("activation_note", ""),
            "non-object project": lambda value: value.__setitem__("project", []),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label):
                request = resolution_with("task-set-lock-in")
                mutate(request)
                with self.assertRaises(RuntimeCompileError):
                    compile(request)

        request = resolution_with("task-set-lock-in")
        request["complexity"]["floor"] = "L5"
        request["complexity"]["ceiling"] = "L1"
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        request["complexity"]["ceiling"] = "L6"
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        request["task"]["resolution"] = "future"
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        request["required_by_recipe"][0] = "task-set-lock-in"
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        request["required_by_recipe"][0]["reasons"] = "not-an-array"
        with self.assertRaises(RuntimeCompileError):
            compile(request)

    def test_task_resolution_contract_requires_nested_schema_fields(self):
        request = resolution_with("task-set-lock-in")
        del request["task"]["execution_form"]
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        del request["complexity"]["reasons"]
        with self.assertRaises(RuntimeCompileError):
            compile(request)

        request = resolution_with("task-set-lock-in")
        del request["required_by_recipe"][0]["plain_display_name"]
        with self.assertRaises(RuntimeCompileError):
            compile(request)

    def test_hard_restrictions_have_emitted_provenance(self):
        request = resolve_task("review this patch, do not modify files")
        plan = compile(request)
        restrictions = request["hard_restrictions"]
        rows = [item for item in plan["directive_provenance"] if item["kind"] == "hard-restriction"]
        self.assertEqual([item["text"] for item in rows], restrictions)
        self.assertTrue(all(item["emitted"] for item in rows))
        self.assertTrue(all(item["component"] == "task-resolution" for item in rows))
        self.assertTrue(all(item["selected_because"] for item in rows))


class RuntimeAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = compile(resolution_with("task-set-lock-in"))

    def test_generic_adapter(self):
        result = compose_instructions("BASE", self.plan)
        self.assertEqual(result["combined_instructions"], "BASE")
        self.assertIn("upgradeables-runtime", result["runtime_instructions"])

    def test_ollama_request_composition(self):
        request = build_ollama_request(model="local", user_content="TASK", plan=self.plan, base_instructions="BASE")
        self.assertEqual(request["messages"][0]["role"], "system")
        self.assertIn("BASE", request["messages"][0]["content"])
        self.assertIn("upgradeables-runtime", request["messages"][0]["content"])

    def test_openai_compatible_mock_request(self):
        request = build_chat_completions_request(model="mock", user_content="TASK", plan=self.plan)
        self.assertEqual(request["messages"][-1], {"role": "user", "content": "TASK"})

    def test_base_instruction_preservation(self):
        result = compose_instructions("DO NOT REMOVE", self.plan, mode="append-managed-runtime-block")
        self.assertTrue(result["combined_instructions"].startswith("DO NOT REMOVE"))

    def test_openai_agents_static_instruction_preservation(self):
        agent = SimpleNamespace(instructions="BASE")
        apply_runtime_plan(agent, self.plan)
        self.assertTrue(agent.instructions.startswith("BASE"))
        self.assertIn("upgradeables-runtime", agent.instructions)

    def test_secret_redaction(self):
        text = redact_secrets("Authorization: Bearer abc123 token=gho_1234567890123456")
        self.assertNotIn("abc123", text)
        self.assertNotIn("gho_1234567890123456", text)

    def test_run_manifest(self):
        manifest = build_manifest(plan=self.plan, model_identifier="mock", endpoint_type="mock")
        self.assertEqual(manifest["runtime_plan_hash"], self.plan["manifest_hash"])
        self.assertTrue(manifest["manifest_hash"].startswith("sha256:"))


if __name__ == "__main__":
    unittest.main()
