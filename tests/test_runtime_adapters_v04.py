import asyncio
import io
import json
import shutil
import sys
import threading
import time
import unittest
import uuid
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.runtime.adapters.generic import (
    AdapterRequestError,
    capability,
    compose_instructions,
    endpoint_type,
    normalized_error,
)
from upgradeables_harness.runtime.adapters.ollama import (
    build_ollama_request,
    chat as ollama_chat,
    discover as discover_ollama,
    normalize_discovery as normalize_ollama_discovery,
    normalize_response as normalize_ollama_response,
    normalize_stream as normalize_ollama_stream,
    run_ollama,
)
from upgradeables_harness.runtime.adapters.openai_agents import (
    apply_runtime_plan,
    describe_capabilities,
)
from upgradeables_harness.runtime.adapters.openai_compatible import (
    chat_completions,
    discover_models,
    normalize_discovery as normalize_openai_discovery,
    normalize_response as normalize_openai_response,
    normalize_stream as normalize_openai_stream,
)


PLAN = {
    "manifest_hash": "sha256:" + "1" * 64,
    "instruction_capsule": (
        '<upgradeables-runtime version="0.4.0">\n'
        "Task controls:\n- Keep scope bounded.\n"
        "</upgradeables-runtime>"
    ),
    "state_contract": [],
    "validators": [],
    "orchestration": [],
    "tool_requirements": [],
    "output_contract": [],
    "warnings": [],
}


@contextmanager
def workspace_directory(prefix="tmp-runtime-adapter-"):
    path = ROOT / "tests" / f"{prefix}{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield str(path)
    finally:
        shutil.rmtree(path)


@contextmanager
def mock_ollama_server(*, status=200, payload=None, delay=0):
    requests = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
            requests.append((self.path, json.loads(body.decode("utf-8"))))
            if delay:
                time.sleep(delay)
            response = json.dumps(payload or {"error": "mock error"}).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            try:
                self.wfile.write(response)
            except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
                pass

        def log_message(self, _format, *_args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", requests
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload if isinstance(payload, bytes) else json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


class RoutedOpener:
    def __init__(self, routes):
        self.routes = routes
        self.requests = []

    def __call__(self, request, timeout):
        self.requests.append((request, timeout))
        path = urlsplit(request.full_url).path
        if path not in self.routes:
            raise AssertionError(f"unexpected request path: {path}")
        value = self.routes[path]
        return FakeResponse(value)


class GenericAdapterTests(unittest.TestCase):
    def test_endpoint_type_is_conservative(self):
        self.assertEqual(endpoint_type("http://localhost:11434"), "loopback")
        self.assertEqual(endpoint_type("http://127.0.0.1"), "loopback")
        self.assertEqual(endpoint_type("http://192.168.1.5:8000"), "private-network")
        self.assertEqual(endpoint_type("http://modelbox:8000"), "private-network")
        self.assertEqual(endpoint_type("https://api.example.com"), "remote")
        self.assertEqual(endpoint_type("not-a-url"), "unknown")

    def test_capability_validates_tri_state(self):
        self.assertEqual(capability("supported", "probe"), {"status": "supported", "evidence": "probe"})
        with self.assertRaises(ValueError):
            capability("maybe")

    def test_composition_rejects_non_text_instructions(self):
        with self.assertRaises(TypeError):
            compose_instructions(["base"], PLAN)
        with self.assertRaises(TypeError):
            compose_instructions("base", {"instruction_capsule": []})

    def test_normalized_error_redacts_and_classifies(self):
        error = normalized_error(
            provider="openai-compatible",
            status=401,
            message="token=gho_1234567890123456",
        )
        self.assertEqual(error["kind"], "authentication_failed")
        self.assertNotIn("gho_", error["message"])


class OllamaAdapterTests(unittest.TestCase):
    def test_request_preserves_task_and_base(self):
        request = build_ollama_request(
            model="exact:tag", user_content="TASK", plan=PLAN,
            base_instructions="BASE", stream=False,
        )
        self.assertEqual(request["model"], "exact:tag")
        self.assertTrue(request["messages"][0]["content"].startswith("BASE"))
        self.assertEqual(request["messages"][-1], {"role": "user", "content": "TASK"})

    def test_discovery_normalizes_exact_model_and_context(self):
        result = normalize_ollama_discovery(
            endpoint="http://localhost:11434/api",
            model="tiny:latest",
            version={"version": "1.2.3"},
            tags={"models": [{"name": "tiny:latest"}]},
            show={
                "capabilities": ["completion", "tools"],
                "parameters": "temperature 0.8\nnum_ctx 4096",
                "model_info": {"tiny.context_length": 8192},
            },
            running={"models": [{"name": "tiny:latest", "context_length": 2048}]},
        )
        self.assertEqual(result["endpoint_type"], "loopback")
        self.assertEqual(result["model_available"]["status"], "supported")
        self.assertEqual(result["features"]["tools"]["status"], "supported")
        self.assertEqual(result["features"]["vision"]["status"], "unsupported")
        self.assertEqual(result["context"]["model_max_context_tokens"], 8192)
        self.assertEqual(result["context"]["configured_context_tokens"], 4096)
        self.assertEqual(result["context"]["effective_context_tokens"], 2048)

    def test_explicit_discovery_skips_show_for_missing_model(self):
        opener = RoutedOpener({
            "/api/version": {"version": "1"},
            "/api/tags": {"models": [{"name": "other"}]},
            "/api/ps": {"models": []},
        })
        result = discover_ollama("http://localhost:11434/api", "missing", opener=opener)
        self.assertEqual(result["model_available"]["status"], "unsupported")
        self.assertNotIn("/api/show", [urlsplit(item[0].full_url).path for item in opener.requests])

    def test_chat_accepts_endpoint_already_ending_in_api(self):
        opener = RoutedOpener({"/api/chat": {"done": True, "message": {"content": "ok"}}})
        payload = ollama_chat("http://localhost:11434/api", {"model": "m"}, opener=opener)
        self.assertTrue(payload["done"])
        self.assertEqual(urlsplit(opener.requests[0][0].full_url).path, "/api/chat")

    def test_non_stream_response_normalization(self):
        result = normalize_ollama_response({
            "model": "m", "done": True, "done_reason": "stop",
            "message": {"content": "hello", "tool_calls": [{"name": "x"}]},
            "prompt_eval_count": 3, "eval_count": 4, "total_duration": 10,
        })
        self.assertEqual(result["response_text"], "hello")
        self.assertEqual(result["usage"]["total_tokens"], 7)
        self.assertFalse(result["partial"])
        self.assertEqual(len(result["tool_calls"]), 1)

    def test_non_stream_malformed_response_is_explicit(self):
        result = normalize_ollama_response({"done": True})
        self.assertTrue(result["partial"])
        self.assertEqual(result["error"]["kind"], "malformed_response")

    def test_ndjson_stream_normalization(self):
        records = [
            '{"model":"m","message":{"content":"hel"},"done":false}\n',
            '{"model":"m","message":{"content":"lo"},"done":true,"done_reason":"stop","prompt_eval_count":2,"eval_count":1}\n',
        ]
        result = normalize_ollama_stream(records)
        self.assertEqual(result["response_text"], "hello")
        self.assertFalse(result["partial"])
        self.assertEqual(result["usage"]["total_tokens"], 3)

    def test_ndjson_midstream_error_preserves_partial_output(self):
        result = normalize_ollama_stream([
            '{"message":{"content":"partial"},"done":false}\n',
            '{"error":"worker crashed"}\n',
        ])
        self.assertEqual(result["response_text"], "partial")
        self.assertTrue(result["partial"])
        self.assertEqual(result["error"]["kind"], "stream_interrupted")

    def test_facade_dry_run_never_opens_network_or_writes_artifacts(self):
        def forbidden_opener(*_args, **_kwargs):
            raise AssertionError("dry run attempted network access")

        with workspace_directory() as directory:
            result = run_ollama(
                model="installed:tag",
                task="rename this heading from Foo to Bar",
                output_root=directory,
                dry_run=True,
                opener=forbidden_opener,
            )
            self.assertFalse(result["network_performed"])
            self.assertIsNone(result["artifact_directory"])
            self.assertTrue(result["runtime_plan_hash"].startswith("sha256:"))
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_facade_success_records_plan_hash_and_artifacts(self):
        opener = RoutedOpener({
            "/api/chat": {
                "model": "installed:tag",
                "done": True,
                "done_reason": "stop",
                "message": {"content": "Bar"},
                "prompt_eval_count": 4,
                "eval_count": 1,
            }
        })
        with workspace_directory() as directory:
            result = run_ollama(
                model="installed:tag",
                task="rename this heading from Foo to Bar",
                output_root=directory,
                opener=opener,
            )
            target = Path(result["artifact_directory"])
            self.assertTrue(result["network_performed"])
            self.assertEqual(result["response"]["response_text"], "Bar")
            self.assertTrue(target.is_dir())
            self.assertEqual(
                {item.name for item in target.iterdir()},
                {
                    "manifest.json", "task.txt", "runtime-plan.json",
                    "compiled-instructions.txt", "raw-response.txt", "metrics.json",
                },
            )
            manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            plan = json.loads((target / "runtime-plan.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["runtime_plan_hash"], result["runtime_plan_hash"])
            self.assertEqual(plan["manifest_hash"], result["runtime_plan_hash"])

    def test_facade_timeout_is_normalized_and_recorded_without_retry(self):
        with mock_ollama_server(delay=0.1) as (endpoint, requests):
            with workspace_directory() as directory:
                result = run_ollama(
                    endpoint=endpoint,
                    model="installed:tag",
                    task="return OK",
                    output_root=directory,
                    timeout=0.01,
                )
                self.assertEqual(len(requests), 1)
                self.assertEqual(result["response"]["error"]["kind"], "endpoint_unavailable")
                self.assertTrue(Path(result["artifact_directory"]).is_dir())

    def test_facade_http_error_is_normalized_and_recorded_without_pull(self):
        with mock_ollama_server(status=404, payload={"error": "model not found"}) as (endpoint, requests):
            with workspace_directory() as directory:
                result = run_ollama(
                    endpoint=endpoint,
                    model="missing:tag",
                    task="return OK",
                    output_root=directory,
                )
                self.assertEqual(len(requests), 1)
                self.assertEqual(requests[0][0], "/api/chat")
                self.assertEqual(result["response"]["error"]["kind"], "model_unavailable")
                self.assertTrue(Path(result["artifact_directory"]).is_dir())

    def test_cli_dry_run_exposes_request_and_plan_without_network(self):
        from upgradeables_harness.cli import main

        output = io.StringIO()
        with redirect_stdout(output):
            code = main([
                "run", "ollama", "--model", "installed:tag", "--task",
                "rename this heading from Foo to Bar", "--dry-run",
            ])
        payload = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertTrue(payload["dry_run"])
        self.assertFalse(payload["network_performed"])
        self.assertEqual(payload["request"]["model"], "installed:tag")
        self.assertEqual(payload["runtime_plan_hash"], payload["runtime_plan"]["manifest_hash"])

    def test_cli_live_loopback_run_normalizes_and_records_artifacts(self):
        from upgradeables_harness.cli import main

        response = {
            "model": "installed:tag", "done": True, "done_reason": "stop",
            "message": {"content": "OK"},
        }
        with mock_ollama_server(payload=response) as (endpoint, requests):
            with workspace_directory() as directory:
                stdout = io.StringIO()
                stderr = io.StringIO()
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    code = main([
                        "run", "ollama", "--model", "installed:tag",
                        "--task", "return OK", "--endpoint", endpoint,
                        "--output-root", directory, "--format", "json",
                    ])
                payload = json.loads(stdout.getvalue())
                self.assertEqual(code, 0)
                self.assertEqual(len(requests), 1)
                self.assertEqual(payload["response"]["response_text"], "OK")
                self.assertTrue(Path(payload["artifact_directory"], "manifest.json").is_file())


class OpenAICompatibleAdapterTests(unittest.TestCase):
    def test_models_discovery_keeps_undeclared_capabilities_unknown(self):
        result = normalize_openai_discovery(
            endpoint="http://modelbox:8000/v1",
            model="m",
            payload={"data": [{"id": "m"}]},
            declared_capabilities={"system_role": True, "tools": False, "context_window_tokens": 4096},
        )
        self.assertEqual(result["model_available"]["status"], "supported")
        self.assertEqual(result["instruction_roles"]["system"]["status"], "supported")
        self.assertEqual(result["features"]["tools"]["status"], "unsupported")
        self.assertEqual(result["features"]["streaming"]["status"], "unknown")
        self.assertEqual(result["context"]["configured_context_tokens"], 4096)

    def test_discovery_does_not_duplicate_v1(self):
        opener = RoutedOpener({"/v1/models": {"data": [{"id": "m"}]}})
        result = discover_models("http://modelbox:8000/v1", "m", opener=opener)
        self.assertEqual(result["model_available"]["status"], "supported")
        self.assertEqual(urlsplit(opener.requests[0][0].full_url).path, "/v1/models")

    def test_chat_does_not_duplicate_v1(self):
        opener = RoutedOpener({"/v1/chat/completions": {"choices": []}})
        chat_completions("http://modelbox:8000/v1", {"model": "m", "messages": []}, opener=opener)
        self.assertEqual(urlsplit(opener.requests[0][0].full_url).path, "/v1/chat/completions")

    def test_non_stream_response_normalization(self):
        result = normalize_openai_response({
            "model": "m",
            "choices": [{"message": {"content": "hello", "tool_calls": []}, "finish_reason": "length"}],
            "usage": {"prompt_tokens": 2, "completion_tokens": 3, "total_tokens": 5},
        })
        self.assertEqual(result["response_text"], "hello")
        self.assertEqual(result["usage"]["total_tokens"], 5)
        self.assertTrue(result["truncated"])
        self.assertFalse(result["partial"])

    def test_non_stream_malformed_response_is_explicit(self):
        result = normalize_openai_response({"choices": []})
        self.assertTrue(result["partial"])
        self.assertEqual(result["error"]["kind"], "malformed_response")

    def test_sse_stream_normalization_with_terminal_usage(self):
        result = normalize_openai_stream([
            'data: {"model":"m","choices":[{"delta":{"content":"hel"},"finish_reason":null}]}\n\n',
            'data: {"model":"m","choices":[{"delta":{"content":"lo"},"finish_reason":"stop"}]}\n',
            'data: {"choices":[],"usage":{"prompt_tokens":2,"completion_tokens":1,"total_tokens":3}}\n\n',
            "data: [DONE]\n\n",
        ])
        self.assertEqual(result["response_text"], "hello")
        self.assertEqual(result["usage"]["total_tokens"], 3)
        self.assertFalse(result["partial"])

    def test_sse_without_done_is_partial(self):
        result = normalize_openai_stream([
            'data: {"choices":[{"delta":{"content":"partial"},"finish_reason":null}]}\n'
        ])
        self.assertEqual(result["response_text"], "partial")
        self.assertTrue(result["partial"])
        self.assertIsNone(result["usage"]["total_tokens"])

    def test_sse_malformed_event_returns_normalized_error(self):
        result = normalize_openai_stream(["data: {bad json}\n"])
        self.assertTrue(result["partial"])
        self.assertEqual(result["error"]["kind"], "malformed_response")


class OpenAIAgentsAdapterTests(unittest.TestCase):
    def test_reapplication_uses_original_static_base(self):
        agent = SimpleNamespace(instructions="BASE")
        apply_runtime_plan(agent, PLAN)
        second = dict(PLAN, instruction_capsule="<upgradeables-runtime>SECOND</upgradeables-runtime>")
        apply_runtime_plan(agent, second)
        self.assertEqual(agent.instructions.count("upgradeables-runtime"), 2)
        self.assertNotIn("Keep scope bounded", agent.instructions)
        self.assertTrue(agent.instructions.startswith("BASE"))

    def test_sync_dynamic_instructions_remain_supported(self):
        agent = SimpleNamespace(instructions=lambda context, current: "DYNAMIC BASE")
        apply_runtime_plan(agent, PLAN)
        result = agent.instructions(None, agent)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("DYNAMIC BASE"))
        self.assertIn("Keep scope bounded", result)

    def test_manual_base_change_after_application_is_preserved(self):
        agent = SimpleNamespace(instructions="BASE")
        apply_runtime_plan(agent, PLAN)
        agent.instructions = "REPLACEMENT BASE"
        apply_runtime_plan(agent, PLAN)
        self.assertTrue(agent.instructions.startswith("REPLACEMENT BASE"))
        self.assertNotIn("BASE\n\nBASE", agent.instructions)

    def test_async_dynamic_instructions_are_awaited(self):
        async def base(context, current):
            return "ASYNC BASE"

        agent = SimpleNamespace(instructions=base)
        apply_runtime_plan(agent, PLAN)
        result = asyncio.run(agent.instructions(None, agent))
        self.assertTrue(result.startswith("ASYNC BASE"))

    def test_sync_callable_returning_awaitable_is_awaited(self):
        async def value():
            return "AWAITABLE BASE"

        agent = SimpleNamespace(instructions=lambda context, current: value())
        apply_runtime_plan(agent, PLAN)
        result = asyncio.run(agent.instructions(None, agent))
        self.assertTrue(result.startswith("AWAITABLE BASE"))

    def test_agent_capabilities_are_observation_based(self):
        agent = SimpleNamespace(
            instructions="BASE", tools=[], output_type=None,
            input_guardrails=[], output_guardrails=[], handoffs=[],
        )
        result = describe_capabilities(agent)
        self.assertEqual(result["instruction_callback"]["status"], "supported")
        self.assertEqual(result["tools"]["status"], "supported")
        self.assertNotIn("model", result)

    def test_missing_instructions_attribute_fails_explicitly(self):
        with self.assertRaises(TypeError):
            apply_runtime_plan(object(), PLAN)


if __name__ == "__main__":
    unittest.main()
