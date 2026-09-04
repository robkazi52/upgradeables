import io
import json
import os
import shutil
import socket
import sys
import unittest
import uuid
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.runtime.evals.live import (
    create_live_adapter,
    validate_api_key_environment,
    validate_endpoint_origin,
)
from upgradeables_harness.runtime.evals.runner import mock_adapter, run_experiment


@contextmanager
def workspace_directory():
    path = ROOT / "build" / f"live-eval-test-{uuid.uuid4().hex}"
    path.mkdir(parents=True)
    try:
        yield path
    finally:
        shutil.rmtree(path)


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


def condition(instructions=""):
    return {
        "condition": "baseline" if not instructions else "static-full",
        "task": "Return exactly: OK",
        "instructions": instructions,
        "runtime_plan": None,
    }


class LiveEvalAdapterTests(unittest.TestCase):
    def test_ollama_reuses_chat_transport_once_and_captures_evidence(self):
        calls = []

        def opener(request, timeout):
            calls.append((request, timeout))
            return FakeResponse({
                "model": "installed:tag", "done": True, "done_reason": "stop",
                "message": {"content": "OK"},
                "prompt_eval_count": 7, "eval_count": 1,
                "total_duration": 12345,
            })

        adapter = create_live_adapter(
            "ollama", model="installed:tag", endpoint="http://127.0.0.1:11434",
            timeout=2, opener=opener,
        )
        result = adapter(
            condition("STATIC"), {},
            {"temperature": 0, "generation_parameters": {"temperature": 0, "top_p": 0.75, "stream": False}},
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][0].full_url, "http://127.0.0.1:11434/api/chat")
        self.assertEqual(result["response_text"], "OK")
        self.assertEqual(result["usage"]["total_tokens"], 8)
        self.assertEqual(result["model_id"], "installed:tag")
        self.assertEqual(result["provider_timing"]["total_duration"], 12345)
        self.assertGreaterEqual(result["latency_ms"], 0)
        self.assertEqual(result["provider_request"]["messages"][0]["content"], "STATIC")
        self.assertEqual(result["provider_request"]["options"], {"temperature": 0, "top_p": 0.75})
        self.assertIsNone(result["error"])

    def test_openai_compatible_uses_bearer_only_in_header_and_redacts_echo(self):
        secret = 'opaque\\"live-eval-secret'
        calls = []

        def opener(request, timeout):
            calls.append((request, timeout))
            return FakeResponse({
                "model": "exact-model",
                "choices": [{"message": {"content": f"OK {secret}"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 5, "completion_tokens": 2, "total_tokens": 7},
                "debug": secret,
            })

        adapter = create_live_adapter(
            "openai-compatible", model="exact-model", endpoint="https://models.example/v1",
            api_key=secret, timeout=3, opener=opener,
        )
        result = adapter(
            condition(), {},
            {"temperature": 0.25, "generation_parameters": {"temperature": 0.25, "top_p": 0.5, "stream": False}},
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][0].get_header("Authorization"), f"Bearer {secret}")
        serialized = json.dumps(result)
        self.assertNotIn(secret, serialized)
        self.assertIn("[REDACTED]", serialized)
        self.assertEqual(result["raw_response"]["debug"], "[REDACTED]")
        self.assertEqual(result["response_text"], "OK [REDACTED]")
        self.assertEqual(result["usage"]["total_tokens"], 7)
        self.assertEqual(result["model_id"], "exact-model")
        self.assertEqual(result["provider_request"]["temperature"], 0.25)
        self.assertEqual(result["provider_request"]["top_p"], 0.5)
        self.assertFalse(result["provider_request"]["stream"])

    def test_transport_failure_is_redacted_and_not_retried(self):
        calls = []

        def opener(request, timeout):
            calls.append((request, timeout))
            raise TimeoutError("token=gho_1234567890123456")

        adapter = create_live_adapter(
            "ollama", model="installed:tag", endpoint="http://localhost:11434",
            opener=opener,
        )
        result = adapter(condition(), {}, {"temperature": 0})
        self.assertEqual(len(calls), 1)
        self.assertEqual(result["error"]["kind"], "endpoint_unavailable")
        self.assertNotIn("gho_", json.dumps(result))

    def test_unexpected_transport_error_cannot_persist_escaping_api_key(self):
        secret = 'opaque\\"unexpected-secret'

        def opener(_request, _timeout):
            raise ValueError(f"transport wrapper exposed {secret}")

        adapter = create_live_adapter(
            "openai-compatible", model="exact-model", endpoint="https://models.example",
            api_key=secret, opener=opener,
        )
        result = adapter(condition(), {}, {"temperature": 0})
        self.assertEqual(result["error"]["kind"], "unexpected_adapter_error")
        self.assertNotIn(secret, result["error"]["message"])
        self.assertNotIn(secret, result["raw_response"]["adapter_error"]["message"])

    def test_factory_itself_performs_no_network(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network attempted")):
            adapter = create_live_adapter(
                "ollama", model="installed:tag", endpoint="http://127.0.0.1:11434",
            )
        self.assertTrue(callable(adapter))

    def test_runner_records_the_same_live_generation_parameters_it_sends(self):
        def opener(_request, _timeout):
            return FakeResponse({
                "model": "exact-model",
                "choices": [{"message": {"content": "OK"}, "finish_reason": "stop"}],
                "usage": {},
            })

        adapter = create_live_adapter(
            "openai-compatible", model="exact-model",
            endpoint="http://127.0.0.1:8000/v1", opener=opener,
        )
        manifest = {
            "schema_version": "1.0.0",
            "experiment_id": "generation-parameters",
            "suite": "synthetic-runtime-v1",
            "conditions": ["baseline"],
            "model": {
                "adapter": "openai-compatible", "model": "exact-model",
                "endpoint_origin": "http://127.0.0.1:8000/v1",
                "endpoint_type": "loopback",
            },
            "trials_per_task": 1,
            "temperature": 0.2,
            "generation_parameters": {"temperature": 0.2, "top_p": 0.7, "stream": False},
            "seed_policy": "provider-controlled-no-retry",
            "grader": "objective",
        }
        with workspace_directory() as directory:
            target = run_experiment(manifest, adapter, directory)
            record = json.loads(
                (target / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()[0]
            )
        self.assertEqual(record["generation_parameters"], manifest["generation_parameters"])
        self.assertEqual(record["provider_request"]["temperature"], 0.2)
        self.assertEqual(record["provider_request"]["top_p"], 0.7)
        self.assertFalse(record["provider_request"]["stream"])

    def test_endpoint_origin_rejects_credentials_paths_and_remote_plaintext(self):
        invalid = (
            "https://user:secret@example.com",
            "https://example.com/v1/chat/completions",
            "https://example.com/v1?key=value",
            "https://exa mple.com/v1",
            "https://example.com\\@attacker.example/v1",
            "http://example.com",
            "file:///tmp/socket",
        )
        for endpoint in invalid:
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(ValueError):
                    validate_endpoint_origin(endpoint, "openai-compatible")
        self.assertEqual(
            validate_endpoint_origin("http://127.0.0.1:11434/api/", "ollama"),
            "http://127.0.0.1:11434/api",
        )
        self.assertEqual(
            validate_endpoint_origin("https://example.com:443/v1/", "openai-compatible"),
            "https://example.com/v1",
        )

    def test_exact_model_timeout_and_api_key_env_validation(self):
        for model in ("", " model", "model "):
            with self.subTest(model=model):
                with self.assertRaises(ValueError):
                    create_live_adapter(
                        "ollama", model=model, endpoint="http://127.0.0.1:11434",
                    )
        with self.assertRaises(ValueError):
            create_live_adapter(
                "ollama", model="m", endpoint="http://127.0.0.1:11434", timeout=0,
            )
        self.assertEqual(validate_api_key_environment("UPGRADEABLES_API_KEY"), "UPGRADEABLES_API_KEY")
        for name in ("", "A-B", "1KEY", "KEY=value"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    validate_api_key_environment(name)


class LiveEvalCliTests(unittest.TestCase):
    def run_main(self, arguments):
        from upgradeables_harness.cli import main

        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(arguments)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_eval_dry_run_is_no_network_no_write_and_deterministic(self):
        with workspace_directory() as directory:
            output_root = directory / "experiments"
            arguments = [
                "eval", "run", "synthetic-runtime-v1", "--adapter", "ollama",
                "--model", "installed:tag", "--conditions", "baseline", "static-full",
                "--trials", "2", "--output-root", str(output_root), "--dry-run", "--json",
            ]
            with patch.object(socket.socket, "connect", side_effect=AssertionError("network attempted")):
                first = self.run_main(arguments)
                second = self.run_main(arguments)
            self.assertEqual(first[0], 0, first[2])
            self.assertEqual(second[0], 0, second[2])
            preview = json.loads(first[1])
            repeated = json.loads(second[1])
            self.assertFalse(preview["network_performed"])
            self.assertFalse(preview["writes_performed"])
            self.assertEqual(preview["request_count_planned"], 40)
            self.assertEqual(preview["configuration_hash"], repeated["configuration_hash"])
            self.assertEqual(preview["estimated_cost"]["availability"], "unavailable")
            self.assertFalse(output_root.exists())

    def test_human_dry_run_prints_fixed_resolution_and_cost_availability(self):
        code, stdout, stderr = self.run_main([
            "eval", "run", "synthetic-runtime-v1", "--adapter", "mock",
            "--conditions", "baseline", "--dry-run",
        ])
        self.assertEqual(code, 0, stderr)
        self.assertIn("Suite: synthetic-runtime-v1", stdout)
        self.assertIn("Conditions (1): baseline", stdout)
        self.assertIn("Planned model requests: 10", stdout)
        self.assertRegex(stdout, r"Fixed resolutions: \d+/10 available")
        self.assertIn("Estimated cost: unavailable", stdout)

    def test_eval_openai_key_is_read_from_environment_and_never_rendered(self):
        secret = 'opaque\\"cli-secret'
        with patch.dict(os.environ, {"LIVE_EVAL_KEY": secret}):
            code, stdout, stderr = self.run_main([
                "eval", "run", "synthetic-runtime-v1",
                "--adapter", "openai-compatible", "--model", "exact-model",
                "--endpoint", "https://models.example/v1",
                "--api-key-env", "LIVE_EVAL_KEY", "--conditions", "baseline",
                "--dry-run", "--json",
            ])
        self.assertEqual(code, 0, stderr)
        self.assertNotIn(secret, stdout + stderr)
        self.assertNotIn("LIVE_EVAL_KEY", stdout + stderr)

    def test_eval_live_requires_exact_model_and_safe_endpoint(self):
        invalid = (
            ["--adapter", "ollama"],
            ["--adapter", "ollama", "--model", " model"],
            ["--adapter", "openai-compatible", "--model", "m", "--endpoint", "http://example.com"],
        )
        for options in invalid:
            with self.subTest(options=options):
                code, _stdout, stderr = self.run_main([
                    "eval", "run", "synthetic-runtime-v1", *options,
                    "--conditions", "baseline", "--dry-run",
                ])
                self.assertEqual(code, 2)
                self.assertTrue(stderr)

    def test_eval_ollama_unavailable_model_fails_cleanly(self):
        discovery = {
            "endpoint_type": "loopback", "server_version": "test",
            "model_available": {"status": "unsupported"},
        }
        with workspace_directory() as directory:
            output_root = directory / "experiments"
            with patch("upgradeables_harness.runtime.adapters.ollama.discover", return_value=discovery) as preflight:
                code, _stdout, stderr = self.run_main([
                    "eval", "run", "synthetic-runtime-v1", "--adapter", "ollama",
                    "--model", "missing:tag", "--conditions", "baseline",
                    "--output-root", str(output_root),
                ])
            self.assertEqual(code, 2)
            preflight.assert_called_once()
            self.assertIn("not available", stderr)
            self.assertFalse(output_root.exists())

    def test_eval_openai_live_wires_structured_results_without_real_network(self):
        def factory(*_args, **_kwargs):
            def adapter(request, task, manifest):
                response = mock_adapter(request, task, manifest)
                return {
                    "response_text": response,
                    "provider_request": {"model": "exact-model"},
                    "raw_response": {"choices": [{"text": response}]},
                    "usage": {"input_tokens": 3, "output_tokens": 1, "total_tokens": 4},
                    "latency_ms": 1.25,
                    "model_id": "exact-model",
                    "provider_timing": {},
                    "finish_reason": "stop",
                    "partial": False,
                    "truncated": False,
                    "error": None,
                }
            return adapter

        with workspace_directory() as directory:
            with patch("upgradeables_harness.runtime.evals.live.create_live_adapter", side_effect=factory):
                code, stdout, stderr = self.run_main([
                    "eval", "run", "synthetic-runtime-v1",
                    "--adapter", "openai-compatible", "--model", "exact-model",
                    "--endpoint", "http://127.0.0.1:8000/v1",
                    "--conditions", "baseline", "--output-root", str(directory), "--json",
                ])
            self.assertEqual(code, 0, stderr)
            completed = json.loads(stdout)
            self.assertEqual(completed["request_count_planned"], 10)
            self.assertEqual(completed["request_count_completed"], 10)
            records = [
                json.loads(line) for line in
                (Path(completed["experiment_directory"]) / "raw-results.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(records[0]["usage"]["total_tokens"], 4)
            self.assertEqual(records[0]["latency_ms"], 1.25)
            self.assertEqual(records[0]["provider_raw_response"]["choices"][0]["text"], records[0]["raw_response"])


if __name__ == "__main__":
    unittest.main()
