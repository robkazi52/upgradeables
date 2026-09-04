import json
import shutil
import socket
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.runtime.compiler import canonical_hash
from upgradeables_harness.runtime.evals.conditions import build_condition, static_full_text
from upgradeables_harness.runtime.evals.graders import grade
from upgradeables_harness.runtime.evals.report import summarize, write_report
from upgradeables_harness.runtime.evals.runner import (
    condition_schedule,
    mock_adapter,
    prepare_experiment,
    run_experiment,
    validate_manifest,
)
from upgradeables_harness.runtime.evals.suites import list_suites, load_suite


@contextmanager
def writable_tempdir():
    """Avoid Python 3.14 TemporaryDirectory ACL tightening in managed Windows CI."""
    path = ROOT / "build" / f"runtime-eval-test-{uuid.uuid4().hex}"
    path.mkdir(parents=True)
    try:
        yield str(path)
    finally:
        shutil.rmtree(path)


def manifest(experiment_id="eval-test", **updates):
    value = {
        "schema_version": "1.0.0",
        "experiment_id": experiment_id,
        "suite": "tiny-v1",
        "conditions": ["baseline", "static-full", "adaptive-runtime"],
        "model": {"adapter": "mock", "model": "deterministic-fixture"},
        "trials_per_task": 1,
        "temperature": 0,
        "seed_policy": "deterministic-mock",
        "grader": "objective",
        "order_seed": 17,
    }
    value.update(updates)
    return value


def tiny_suite(grader=None):
    return {
        "schema_version": "1.0.0",
        "slug": "tiny-v1",
        "description": "test suite",
        "license": "CC0-1.0",
        "tasks": [
            {
                "id": "task-1",
                "family": "constraint-following",
                "prompt": "Return exactly: OK",
                "grader": grader or {"type": "exact", "expected": "OK"},
            }
        ],
    }


def fake_condition(task, condition, **_kwargs):
    instructions = {
        "baseline": "",
        "static-full": "STATIC",
        "adaptive-end-to-end": "ADAPTIVE",
        "adaptive-fixed-resolution": "FIXED",
    }[condition]
    value = {
        "condition": condition,
        "evaluation_mode": condition,
        "task": task,
        "instructions": instructions,
        "instruction_hash": canonical_hash(instructions),
        "runtime_plan": {"instruction_capsule": instructions} if condition.startswith("adaptive-") else None,
        "runtime_plan_hash": canonical_hash({"instruction_capsule": instructions}) if condition.startswith("adaptive-") else None,
        "task_resolution_source": "fixed-suite" if condition == "adaptive-fixed-resolution" else ("v0.3-resolver" if condition == "adaptive-end-to-end" else None),
        "task_resolution_hash": "sha256:task" if condition.startswith("adaptive-") else None,
        "fixed_resolution_hash": "sha256:fixed" if condition == "adaptive-fixed-resolution" else None,
    }
    value["condition_hash"] = canonical_hash(value)
    return value


def result(task_id, condition, success, trial=0, status="graded"):
    return {
        "task_id": task_id,
        "condition": condition,
        "trial_index": trial,
        "raw_response": "output",
        "directive_token_estimate": 0,
        "observation_status": "completed" if status == "graded" else "adapter-error",
        "grade": {
            "status": status,
            "success": success if status == "graded" else None,
            "score": (1.0 if success else 0.0) if status == "graded" else None,
        },
    }


class ConditionBoundaryTests(unittest.TestCase):
    def test_only_runtime_layer_varies_across_core_conditions(self):
        plan = {"instruction_capsule": "ADAPTIVE", "manifest_hash": "sha256:plan"}
        with patch("upgradeables_harness.runtime.evals.conditions.compile_task", return_value=plan) as compiler:
            baseline = build_condition("same task", "baseline")
            static = build_condition("same task", "static-full")
            adaptive = build_condition("same task", "adaptive-runtime")

        self.assertEqual({item["task"] for item in (baseline, static, adaptive)}, {"same task"})
        self.assertEqual(baseline["instructions"], "")
        self.assertIsNone(baseline["runtime_plan"])
        self.assertEqual(static["instructions"], static_full_text())
        self.assertIsNone(static["runtime_plan"])
        self.assertEqual(adaptive["instructions"], "ADAPTIVE")
        self.assertIs(adaptive["runtime_plan"], plan)
        self.assertEqual(adaptive["condition"], "adaptive-end-to-end")
        compiler.assert_called_once_with(
            "same task", model_profile="medium", max_directive_tokens=500, use_project_profile=False,
        )
        for item in (baseline, static, adaptive):
            unhashed = {key: value for key, value in item.items() if key != "condition_hash"}
            self.assertEqual(item["condition_hash"], canonical_hash(unhashed))

    def test_eval_fixed_resolution_condition(self):
        task = load_suite("synthetic-runtime-v1")["tasks"][0]
        result = build_condition(
            task["prompt"],
            "adaptive-fixed-resolution",
            fixed_resolution=task["fixed_resolution"],
        )
        self.assertEqual(result["condition"], "adaptive-fixed-resolution")
        self.assertEqual(result["task_resolution_source"], "fixed-suite")
        self.assertEqual(result["fixed_resolution_hash"], canonical_hash(task["fixed_resolution"]))
        self.assertEqual(result["task_resolution_hash"], result["fixed_resolution_hash"])

    def test_eval_end_to_end_condition(self):
        result = build_condition("Return exactly: OK", "adaptive-end-to-end")
        self.assertEqual(result["condition"], "adaptive-end-to-end")
        self.assertEqual(result["task_resolution_source"], "v0.3-resolver")
        self.assertIsNone(result["fixed_resolution_hash"])
        self.assertTrue(result["task_resolution_hash"].startswith("sha256:"))

    def test_eval_adaptive_runtime_alias_or_migration(self):
        canonical = build_condition("Return exactly: OK", "adaptive-end-to-end")
        alias = build_condition("Return exactly: OK", "adaptive-runtime")
        self.assertEqual(alias, canonical)

    def test_eval_fixed_resolution_missing_fails_cleanly(self):
        with self.assertRaisesRegex(ValueError, "requires a fixed TaskResolution"):
            build_condition("Return exactly: OK", "adaptive-fixed-resolution")
        with patch("upgradeables_harness.runtime.evals.runner.load_suite", return_value=tiny_suite()):
            with self.assertRaisesRegex(ValueError, "missing: task-1"):
                prepare_experiment(manifest(conditions=["adaptive-fixed-resolution"]))

    def test_static_full_is_fixed_across_tasks(self):
        first = build_condition("task one", "static-full")
        second = build_condition("entirely different task", "static-full")
        self.assertEqual(first["instructions"], second["instructions"])
        self.assertNotEqual(first["condition_hash"], second["condition_hash"])

    def test_unknown_condition_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            build_condition("task", "large-model-baseline")


class ObjectiveGraderTests(unittest.TestCase):
    def test_exact_grader_normalizes_outer_whitespace_only(self):
        self.assertTrue(grade("  17 BLUE\n", {"type": "exact", "expected": "17 BLUE"})["success"])
        self.assertFalse(grade("17  BLUE", {"type": "exact", "expected": "17 BLUE"})["success"])

    def test_contains_and_excludes_graders_preserve_diagnostics(self):
        all_result = grade("Alpha only", {"type": "contains-all", "values": ["alpha", "beta"]})
        any_result = grade("Alpha only", {"type": "contains-any", "values": ["beta", "alpha"]})
        excluded = grade("Alpha only", {"type": "excludes", "values": ["beta"]})
        self.assertEqual(all_result["details"]["missing"], ["beta"])
        self.assertEqual(any_result["details"]["matched"], ["alpha"])
        self.assertTrue(excluded["success"])
        self.assertEqual(excluded["details"]["found"], [])

    def test_json_fields_requires_object_and_distinguishes_missing_null(self):
        self.assertTrue(grade('{"answer": 5}', {"type": "json-fields", "fields": {"answer": 5}})["success"])
        missing = grade("{}", {"type": "json-fields", "fields": {"answer": None}})
        non_object = grade("[1, 2]", {"type": "json-fields", "fields": {"answer": 5}})
        self.assertFalse(missing["success"])
        self.assertTrue(missing["details"]["mismatches"]["answer"]["missing"])
        self.assertFalse(non_object["success"])
        self.assertIn("object", non_object["details"]["error"])

    def test_grader_result_is_typed_deterministic_evidence(self):
        graded = grade("OK", {"type": "exact", "expected": "OK"})
        self.assertEqual(graded["schema_version"], "1.0.0")
        self.assertEqual(graded["grader_kind"], "deterministic")
        self.assertEqual(graded["grader_type"], "objective")
        self.assertEqual(graded["status"], "graded")

    def test_malformed_and_unknown_graders_fail_explicitly(self):
        invalid = (
            ("OK", {}),
            ("OK", {"type": "exact", "expected": 1}),
            ("OK", {"type": "contains-all", "values": []}),
            ("OK", {"type": "unknown"}),
        )
        for response, specification in invalid:
            with self.subTest(specification=specification):
                with self.assertRaises(ValueError):
                    grade(response, specification)
        with self.assertRaises(TypeError):
            grade(None, {"type": "exact", "expected": "OK"})


class SuiteTests(unittest.TestCase):
    def test_bundled_suite_covers_required_initial_families(self):
        suite = load_suite("synthetic-runtime-v1")
        families = {task["family"] for task in suite["tasks"]}
        self.assertEqual(
            families,
            {
                "constraint-following", "source-grounded-answering", "citation-fidelity",
                "local-editing", "debugging-repair", "code-review", "long-context-state",
                "alternative-hypothesis", "structured-output", "stopping-overwork",
            },
        )
        self.assertEqual(len({task["id"] for task in suite["tasks"]}), len(suite["tasks"]))
        self.assertTrue(all(task["fixed_resolution"]["schema_version"] == "1.0.0" for task in suite["tasks"]))
        self.assertTrue(all(task["fixed_resolution"]["query"] == task["prompt"] for task in suite["tasks"]))

    def test_list_suites_is_metadata_only(self):
        listed = list_suites()
        item = next(value for value in listed if value["slug"] == "synthetic-runtime-v1")
        self.assertEqual(set(item), {"slug", "description", "license"})

    def test_malformed_suite_and_duplicate_task_ids_fail_closed(self):
        malformed = tiny_suite()
        malformed["tasks"].append(dict(malformed["tasks"][0]))
        registry = {"eval_suites": [malformed]}
        with patch("upgradeables_harness.runtime.evals.suites.load_runtime_registry", return_value=registry):
            with self.assertRaisesRegex(ValueError, "duplicate task id"):
                load_suite("tiny-v1")

    def test_fixed_resolution_is_strictly_validated_against_task(self):
        malformed = tiny_suite()
        fixed = load_suite("synthetic-runtime-v1")["tasks"][0]["fixed_resolution"]
        malformed["tasks"][0]["fixed_resolution"] = fixed
        registry = {"eval_suites": [malformed]}
        with patch("upgradeables_harness.runtime.evals.suites.load_runtime_registry", return_value=registry):
            with self.assertRaisesRegex(ValueError, "query must match prompt"):
                load_suite("tiny-v1")


class ManifestAndScheduleTests(unittest.TestCase):
    def test_manifest_validation_rejects_unsafe_or_ambiguous_runs(self):
        cases = (
            manifest("../escape"),
            manifest(schema_version="2.0.0"),
            manifest(conditions=[]),
            manifest(conditions=[{}]),
            manifest(conditions=["baseline", "baseline"]),
            manifest(conditions=["adaptive-runtime", "adaptive-end-to-end"]),
            manifest(conditions=["large-model-baseline"]),
            manifest(trials_per_task=True),
            manifest(temperature=float("nan")),
            manifest(model={"adapter": "mock"}),
            manifest(model={"adapter": "mock", "model": "fixture", "API-Key": "must-not-persist"}),
            manifest(generation_parameters={"nested": {"authorization": "must-not-persist"}}),
            manifest(generation_parameters={"nested": float("nan")}),
            manifest(notes={"not", "json"}),
            manifest(endpoint_origin="https://user:pass@example.test"),
            manifest(grader="model-judge"),
            manifest(order_seed="17"),
        )
        for value in cases:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_manifest(value)

    def test_manifest_secret_rejection_precedes_artifact_write(self):
        unsafe = manifest(model={"adapter": "mock", "model": "fixture", "access_token": "secret"})
        with writable_tempdir() as temp:
            with self.assertRaisesRegex(ValueError, "secret-bearing key"):
                run_experiment(unsafe, mock_adapter, temp)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_safe_token_and_authorization_metadata_names_are_allowed(self):
        value = manifest(generation_parameters={
            "tokenizer": "fixture-v1",
            "input_tokens": None,
            "authorization_mode": "environment-reference-only",
            "secretariat": "not-a-credential-field",
        })
        validate_manifest(value)

    def test_invalid_nested_json_leaves_no_artifact_directory(self):
        for unsafe in (
            manifest(notes={"not", "json"}),
            manifest(generation_parameters={"nested": [float("nan")]}),
        ):
            with self.subTest(unsafe=repr(unsafe)):
                with writable_tempdir() as temp:
                    with self.assertRaises(ValueError):
                        run_experiment(unsafe, mock_adapter, temp)
                    self.assertEqual(list(Path(temp).iterdir()), [])

    def test_live_generation_settings_cannot_diverge_from_adapter_request(self):
        base = manifest(
            model={"adapter": "openai-compatible", "model": "fixture"},
            endpoint_origin="https://example.test/v1",
        )
        for parameters in (
            {"temperature": 0, "stream": True},
            {"temperature": 0, "model": "replacement"},
            {"temperature": 0, "messages": []},
        ):
            with self.subTest(parameters=parameters):
                with self.assertRaises(ValueError):
                    validate_manifest({**base, "generation_parameters": parameters})
        validate_manifest({**base, "generation_parameters": {"temperature": 0, "top_p": 0.5, "stream": False}})

    def test_schedule_is_deterministic_and_balanced(self):
        conditions = ["baseline", "static-full", "adaptive-runtime"]
        first = condition_schedule(conditions, 12, 42)
        second = condition_schedule(conditions, 12, 42)
        self.assertEqual(first, second)
        self.assertEqual(len(set(first[:6])), 6)
        for position in range(3):
            counts = {condition: sum(order[position] == condition for order in first[:6]) for condition in conditions}
            self.assertEqual(set(counts.values()), {2})

    def test_two_condition_schedule_alternates_positions(self):
        schedule = condition_schedule(["baseline", "adaptive-runtime"], 4, 1)
        self.assertEqual(len(set(schedule[:2])), 2)
        self.assertEqual(schedule[0], schedule[2])

    def test_prepare_experiment_is_no_write_deterministic_preflight(self):
        value = manifest(
            suite="synthetic-runtime-v1",
            conditions=["baseline", "adaptive-fixed-resolution", "adaptive-end-to-end"],
            trials_per_task=2,
        )
        first = prepare_experiment(value)
        second = prepare_experiment(value)
        self.assertEqual(first, second)
        self.assertEqual(first["manifest"]["request_count_planned"], 60)
        self.assertEqual(first["fixed_resolution_availability"], {
            "available": 10, "required": 10, "missing": [],
        })
        self.assertNotIn("created_at", first["manifest"])
        self.assertEqual(len(first["schedule"]), 20)


class RunnerArtifactTests(unittest.TestCase):
    def _run(self, root, run_manifest=None, adapter=mock_adapter, suite=None, fake=True):
        run_manifest = run_manifest or manifest()
        suite = suite or tiny_suite()
        with patch("upgradeables_harness.runtime.evals.runner.load_suite", return_value=suite):
            if not fake:
                return run_experiment(run_manifest, adapter, root)
            with patch("upgradeables_harness.runtime.evals.runner.build_condition", side_effect=fake_condition):
                return run_experiment(run_manifest, adapter, root)

    def test_run_preserves_manifest_requests_responses_grades_and_report(self):
        raw_text = "Ω exact raw response\n"

        def adapter(_request, _task, _manifest):
            return raw_text

        with writable_tempdir() as temp:
            target = self._run(temp, adapter=adapter)
            complete_manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
            summary = json.loads((target / "summary.json").read_text(encoding="utf-8"))
            report = (target / "report.md").read_text(encoding="utf-8")

            self.assertEqual(complete_manifest["order_strategy"], "balanced-permutations-v1")
            self.assertEqual(complete_manifest["scheduled_observations"], 3)
            self.assertEqual(complete_manifest["harness_version"], "0.4.0")
            self.assertEqual(complete_manifest["runtime_compiler_version"], "0.4.0")
            self.assertEqual(complete_manifest["registry_version"], "0.2.1")
            self.assertIn("repository_commit", complete_manifest)
            unhashed = {
                key: value for key, value in complete_manifest.items()
                if key not in {"manifest_hash", "request_count_completed"}
            }
            self.assertEqual(complete_manifest["manifest_hash"], canonical_hash(unhashed))
            self.assertEqual(complete_manifest["conditions"], ["baseline", "static-full", "adaptive-end-to-end"])
            self.assertEqual(complete_manifest["requested_conditions"], manifest()["conditions"])
            self.assertEqual(complete_manifest["evaluation_modes"], complete_manifest["conditions"])
            self.assertEqual(complete_manifest["adapter"], "mock")
            self.assertEqual(complete_manifest["model_id"], "deterministic-fixture")
            self.assertEqual(complete_manifest["endpoint_type"], "none")
            self.assertIsNone(complete_manifest["endpoint_origin"])
            self.assertEqual(complete_manifest["request_count_planned"], 3)
            self.assertEqual(complete_manifest["request_count_completed"], 3)
            self.assertEqual(complete_manifest["trial_count"], 1)
            self.assertEqual(complete_manifest["condition_order_seed"], 17)
            self.assertEqual(len(records), 3)
            for record in records:
                self.assertEqual(record["raw_response"], raw_text)
                self.assertEqual(record["raw_response_hash"], canonical_hash(raw_text))
                self.assertEqual(record["request_hash"], canonical_hash(record["raw_request"]))
                self.assertIn("instructions", record["raw_request"])
                self.assertEqual(record["compiled_instruction_hash"], record["raw_request"]["instruction_hash"])
                self.assertEqual(record["task_definition_hash"], canonical_hash(tiny_suite()["tasks"][0]))
                self.assertEqual(record["manifest_hash"], complete_manifest["manifest_hash"])
                self.assertEqual(record["model"], complete_manifest["model"])
                self.assertEqual(record["generation_parameters"], {"temperature": 0})
                self.assertEqual(record["evaluation_mode"], record["condition"])
                self.assertIn("fixed_resolution_hash", record)
                self.assertIn("task_resolution_hash", record)
                self.assertIn("provider_request_hash", record)
                self.assertIn("usage", record)
                self.assertIn("latency_ms", record)
                self.assertIn("grade", record)
            self.assertEqual(summary["experiment_id"], "eval-test")
            self.assertIn("Mock-adapter results", " ".join(summary["limitations"]))
            self.assertIn("Raw requests, responses", report)
            self.assertIn("Task-level paired comparisons", report)

    def test_raw_results_survive_report_regeneration_byte_for_byte(self):
        with writable_tempdir() as temp:
            target = self._run(temp)
            raw_path = target / "raw-results.jsonl"
            before = raw_path.read_bytes()
            complete_manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            records = [json.loads(line) for line in raw_path.read_text(encoding="utf-8").splitlines()]
            write_report(target, complete_manifest, records)
            self.assertEqual(raw_path.read_bytes(), before)

    def test_eval_same_settings_across_conditions(self):
        observed = []

        def adapter(request, task, run_manifest):
            observed.append({
                "condition": request["condition"],
                "task": request["task"],
                "task_object": task,
                "model": dict(run_manifest["model"]),
                "temperature": run_manifest["temperature"],
                "seed_policy": run_manifest["seed_policy"],
            })
            return "OK"

        run_manifest = manifest(temperature=0.25, seed_policy="record-if-supported")
        with writable_tempdir() as temp:
            self._run(temp, run_manifest=run_manifest, adapter=adapter)
        self.assertEqual(
            {item["condition"] for item in observed},
            {"baseline", "static-full", "adaptive-end-to-end"},
        )
        self.assertEqual({item["task"] for item in observed}, {"Return exactly: OK"})
        self.assertEqual(
            {json.dumps(item["task_object"], sort_keys=True) for item in observed},
            {json.dumps(tiny_suite()["tasks"][0], sort_keys=True)},
        )
        self.assertEqual(
            {json.dumps(item["model"], sort_keys=True) for item in observed},
            {json.dumps(run_manifest["model"], sort_keys=True)},
        )
        self.assertEqual({item["temperature"] for item in observed}, {0.25})
        self.assertEqual({item["seed_policy"] for item in observed}, {"record-if-supported"})

    def test_eval_live_manifest_fields_and_structured_evidence(self):
        def adapter(_request, _task, _manifest):
            return {
                "response_text": "OK",
                "provider_request": {"model": "fixture-model", "messages": []},
                "raw_response": {"id": "raw-1", "output": "OK"},
                "usage": {"input_tokens": 2, "output_tokens": 1},
                "latency_ms": 12.5,
                "model_id": "fixture-model",
                "provider_timing": {"source": "client-elapsed"},
                "finish_reason": "stop",
                "partial": False,
                "truncated": False,
                "error": None,
            }

        with writable_tempdir() as temp:
            target = self._run(temp, adapter=adapter)
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
        for record in records:
            self.assertEqual(record["raw_response"], "OK")
            self.assertEqual(record["provider_raw_response"]["id"], "raw-1")
            self.assertEqual(record["provider_request_hash"], canonical_hash(record["provider_request"]))
            self.assertEqual(record["usage"]["input_tokens"], 2)
            self.assertEqual(record["latency_ms"], 12.5)
            self.assertEqual(record["response_model_id"], "fixture-model")

    def test_structured_adapter_error_is_ungraded_and_preserved(self):
        def adapter(_request, _task, _manifest):
            return {
                "response_text": "partial text",
                "raw_response": {"error": "provider unavailable"},
                "usage": None,
                "latency_ms": 3,
                "error": {"kind": "http_error", "message": "provider unavailable"},
            }

        with writable_tempdir() as temp:
            target = self._run(temp, adapter=adapter)
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertTrue(all(record["observation_status"] == "adapter-error" for record in records))
        self.assertTrue(all(record["grade"]["status"] == "ungraded" for record in records))
        self.assertTrue(all(record["raw_response"] == "partial text" for record in records))
        self.assertTrue(all(record["error"]["details"]["kind"] == "http_error" for record in records))

    def test_eval_fixed_resolution_hash_preserved(self):
        suite = load_suite("synthetic-runtime-v1")
        run_manifest = manifest(
            suite="synthetic-runtime-v1",
            conditions=["baseline", "adaptive-fixed-resolution", "adaptive-end-to-end"],
        )
        with writable_tempdir() as temp:
            with patch("upgradeables_harness.runtime.evals.runner.load_suite", return_value=suite):
                target = run_experiment(run_manifest, mock_adapter, temp)
            complete_manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(complete_manifest["fixed_resolution_hashes"]), 10)
        fixed_records = [item for item in records if item["condition"] == "adaptive-fixed-resolution"]
        self.assertEqual(len(fixed_records), 10)
        for record in fixed_records:
            expected = complete_manifest["fixed_resolution_hashes"][record["task_id"]]
            self.assertEqual(record["fixed_resolution_hash"], expected)
            self.assertEqual(record["task_resolution_hash"], expected)

    def test_adapter_failure_is_preserved_as_ungraded_and_run_continues(self):
        def adapter(request, _task, _manifest):
            if request["condition"] == "static-full":
                raise RuntimeError("fixture adapter failed")
            return "OK"

        with writable_tempdir() as temp:
            target = self._run(temp, adapter=adapter)
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(records), 3)
            failed = next(record for record in records if record["condition"] == "static-full")
            self.assertEqual(failed["observation_status"], "adapter-error")
            self.assertEqual(failed["grade"]["status"], "ungraded")
            self.assertIsNone(failed["grade"]["success"])
            self.assertEqual(failed["grade"]["details"]["error_stage"], "adapter")
            self.assertEqual(sum(record["observation_status"] == "completed" for record in records), 2)
            summary = json.loads((target / "summary.json").read_text(encoding="utf-8"))
            self.assertEqual(summary["conditions"]["static-full"]["ungraded_observations"], 1)
            complete_manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(complete_manifest["request_count_completed"], 3)

    def test_grader_failure_preserves_the_raw_model_output(self):
        with writable_tempdir() as temp:
            target = self._run(
                temp,
                adapter=lambda *_args: "RAW BEFORE GRADER ERROR",
                suite=tiny_suite({"type": "exact", "expected": 7}),
            )
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
            for record in records:
                self.assertEqual(record["raw_response"], "RAW BEFORE GRADER ERROR")
                self.assertEqual(record["observation_status"], "grader-error")
                self.assertEqual(record["grade"]["status"], "ungraded")

    def test_existing_experiment_directory_is_never_overwritten(self):
        with writable_tempdir() as temp:
            self._run(temp)
            original = (Path(temp) / "eval-test" / "raw-results.jsonl").read_bytes()
            with self.assertRaises(FileExistsError):
                self._run(temp)
            self.assertEqual((Path(temp) / "eval-test" / "raw-results.jsonl").read_bytes(), original)

    def test_invalid_manifest_creates_no_output_directory(self):
        with writable_tempdir() as temp:
            with self.assertRaises(ValueError):
                self._run(temp, run_manifest=manifest("../escape"))
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_offline_mock_run_makes_no_socket_connection(self):
        with writable_tempdir() as temp:
            with patch.object(socket.socket, "connect", side_effect=AssertionError("network attempted")):
                target = self._run(temp, fake=False)
            records = [json.loads(line) for line in (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(records), 3)
            self.assertTrue(all(record["grade"]["success"] for record in records))


class PairedReportTests(unittest.TestCase):
    def test_eval_report_selection_vs_runtime_attribution(self):
        results = [
            result("runtime-only", "baseline", False),
            result("runtime-only", "adaptive-fixed-resolution", True),
            result("runtime-only", "adaptive-end-to-end", True),
            result("resolver-only", "baseline", False),
            result("resolver-only", "adaptive-fixed-resolution", False),
            result("resolver-only", "adaptive-end-to-end", True),
            result("both-hurt", "baseline", True),
            result("both-hurt", "adaptive-fixed-resolution", False),
            result("both-hurt", "adaptive-end-to-end", False),
            result("mixed", "baseline", False),
            result("mixed", "adaptive-fixed-resolution", True),
            result("mixed", "adaptive-end-to-end", False),
        ]
        summary = summarize(results)
        attribution = summary["selection_vs_runtime_attribution"]
        self.assertEqual(attribution["paired_tasks"], 4)
        self.assertEqual(attribution["per_task"]["runtime-only"]["descriptive_label"], "runtime-helped")
        self.assertEqual(attribution["per_task"]["resolver-only"]["descriptive_label"], "resolver-helped")
        self.assertEqual(attribution["per_task"]["both-hurt"]["descriptive_label"], "runtime-hurt")
        self.assertEqual(attribution["per_task"]["mixed"]["descriptive_label"], "mixed/tied")
        self.assertIn("do not establish a causal mechanism", attribution["interpretation"])
        with writable_tempdir() as temp:
            write_report(temp, manifest(), results)
            report = (Path(temp) / "report.md").read_text(encoding="utf-8")
        self.assertIn("## Selection vs Runtime Attribution", report)
        self.assertIn("`runtime-helped`", report)

    def test_summary_uses_task_level_trial_aggregates_for_paired_delta(self):
        results = [
            result("a", "baseline", False, 0), result("a", "baseline", False, 1),
            result("a", "adaptive-runtime", True, 0), result("a", "adaptive-runtime", True, 1),
            result("b", "baseline", True, 0), result("b", "baseline", True, 1),
            result("b", "adaptive-runtime", False, 0), result("b", "adaptive-runtime", False, 1),
        ]
        summary = summarize(results)
        paired = summary["paired_comparisons"]["adaptive-minus-baseline"]
        self.assertEqual(paired["paired_tasks"], 2)
        self.assertEqual(paired["mean_task_delta"], 0.0)
        self.assertEqual(paired["median_task_delta"], 0.0)
        self.assertEqual(paired["improved_tasks"], 1)
        self.assertEqual(paired["regressed_tasks"], 1)
        self.assertEqual(paired["per_task"], {"a": 1.0, "b": -1.0})

    def test_ungraded_observations_do_not_become_objective_failures(self):
        summary = summarize([
            result("a", "baseline", True),
            result("a", "adaptive-runtime", None, status="ungraded"),
        ])
        adaptive = summary["conditions"]["adaptive-runtime"]
        self.assertEqual(adaptive["observations"], 1)
        self.assertEqual(adaptive["graded_observations"], 0)
        self.assertEqual(adaptive["ungraded_observations"], 1)
        self.assertIsNone(adaptive["success_rate"])
        self.assertEqual(summary["paired_comparisons"]["adaptive-minus-baseline"]["paired_tasks"], 0)

    def test_report_handles_condition_with_no_graded_observations(self):
        run_manifest = manifest()
        results = [result("a", "baseline", None, status="ungraded")]
        with writable_tempdir() as temp:
            summary = write_report(temp, run_manifest, results)
            report = (Path(temp) / "report.md").read_text(encoding="utf-8")
        self.assertIsNone(summary["conditions"]["baseline"]["success_rate"])
        self.assertIn("not available", report)
        self.assertIn("1 ungraded", report)


if __name__ == "__main__":
    unittest.main()
