# Runtime adapters

Adapters map a compiled [RuntimePlan](RUNTIME_PLAN.md) to a host. They are thin
integration helpers, not a second compiler. The current adapters use only the
Python standard library. Composition and response normalization are pure local
operations. Network access occurs only when a caller explicitly invokes an
execution or discovery function.

Shared helpers provide:

- conservative endpoint classification as `loopback`, `private-network`,
  `remote`, or `unknown` without contacting it;
- tri-state capability records (`supported`, `unsupported`, or `unknown`) with
  evidence;
- normalized, redacted `AdapterRequestError` records for transport and HTTP
  failures.

Capability records report evidence; they do not select a model profile or grant
permission to contact an endpoint.

## Live evaluation callables

`runtime.evals.live.create_live_adapter` wraps the existing Ollama or
OpenAI-compatible request builder, executor, and normalizer as one callable for
the evaluation runner. It does not duplicate HTTP logic. Each observation uses
one non-streaming attempt and returns response text for grading plus a redacted
provider request/raw response, usage, latency, response model ID, provider
timing, finish/partial/truncation fields, and normalized errors.

The CLI exposes these callables through `upgradeables eval run`; see
[Runtime evaluation](EVALUATION.md) for exact dry-run and live commands. Dry-run
constructs no callable request, contacts no endpoint, and writes no experiment.
A live Ollama experiment performs read-only exact-model preflight before the
experiment directory is created. OpenAI-compatible evaluation has no implicit
discovery. Neither path retries or downloads a model.

## Generic composition

`upgradeables_harness.runtime.adapters.generic.compose_instructions` supports:

- `return-separate-block` (default);
- `append-managed-runtime-block`;
- `prepend-managed-runtime-block`.

It returns base, runtime, and combined instruction strings plus all structured
plan channels. In separate mode, `combined_instructions` is the unchanged base
and `runtime_instructions` is returned independently.

```python
from upgradeables_harness.runtime.adapters.generic import compose_instructions

parts = compose_instructions("Existing host rules", plan)
```

## Ollama

The `upgradeables run ollama` facade resolves the task, compiles a plan,
composes the request, performs one non-streaming `/api/chat` call, normalizes
the response, and records the plan hash and run artifacts. It uses the exact
model name supplied by the caller. It does not run discovery, pull a model, or
retry implicitly.

Inspect the complete request and `RuntimePlan` without network access or
artifact writes:

```bash
upgradeables run ollama \
  --model your-already-installed-model \
  --task "review this function for a regression" \
  --dry-run \
  --format json
```

Run against an explicitly selected Ollama endpoint:

```bash
upgradeables run ollama \
  --model your-already-installed-model \
  --task "review this function for a regression" \
  --endpoint http://127.0.0.1:11434 \
  --options-json '{"temperature": 0}' \
  --output-root .upgradeables/runs
```

A live run prints response text and the new artifact-directory path. Add
`--format json` for the normalized response, hashes, request, plan, and path.
Transport and HTTP failures also produce an artifact set and a nonzero CLI
exit. The artifact directory contains `manifest.json`, `task.txt`,
`runtime-plan.json`, `compiled-instructions.txt`, `raw-response.txt`, and
`metrics.json`.

`build_ollama_request` constructs a native `/api/chat` request with:

- exact caller-supplied model name;
- preserved base plus managed runtime block in a `system` message;
- the task in a distinct `user` message;
- optional `options` copied into the request;
- explicit `stream` boolean.

`chat(endpoint, request_body, ...)` posts JSON to `<endpoint>/api/chat` using
`urllib`. The endpoint may be a server root or already end in `/api`. The helper
does not pull a model or modify a Modelfile.

```python
from upgradeables_harness.runtime.adapters.ollama import build_ollama_request, chat

request = build_ollama_request(
    model="your-installed-model",
    user_content="Review this function",
    plan=plan,
    base_instructions="Existing host rules",
)
response = chat("http://127.0.0.1:11434", request)
```

Read-only discovery is available only by explicit call:

```python
from upgradeables_harness.runtime.adapters.ollama import discover

capabilities = discover(
    "http://127.0.0.1:11434",
    "your-installed-model",
)
```

`discover` reads `/api/version`, `/api/tags`, and `/api/ps`. It calls
`/api/show` only when the exact model identifier appears in the tag listing. It
never pulls or loads a missing model. `normalize_discovery` can instead process
already captured responses without network access. The normalized record keeps
endpoint locality, server version, exact model availability, tri-state declared
features, theoretical/configured/effective context values, and raw evidence.

`normalize_response` converts a completed chat object into common text, model,
finish, usage, timing, tool-call, truncation, partial, and error fields.
`normalize_stream` parses caller-supplied Ollama NDJSON chunks, accumulates
content/tool calls, reads metrics from the terminal object, and preserves
partial output plus a normalized error when a stream fails or ends malformed.

Current limitation: the facade and `chat` expect one JSON response. Streaming
callers must own the HTTP stream and pass its chunks to `normalize_stream`.
Discovery does not prove that a model will honor its stored template/system
behavior, and structured-output support remains unknown when it is not declared
per model.

## OpenAI-compatible Chat Completions

`build_chat_completions_request` creates a conservative request for
`/v1/chat/completions`. The instruction role must be explicitly `system` or
`developer`; it defaults to `system`. The task remains a distinct `user`
message. Caller generation parameters may be added but cannot replace `model`
or `messages`.

`chat_completions(endpoint, request_body, ...)` performs the explicit POST and
optionally adds a bearer header. The endpoint may be a server root or already
end in `/v1`.

```python
from upgradeables_harness.runtime.adapters.openai_compatible import (
    build_chat_completions_request,
    chat_completions,
)

request = build_chat_completions_request(
    model="server-model-id",
    user_content="Summarize the supplied source",
    plan=plan,
    instruction_role="system",
)
response = chat_completions("http://127.0.0.1:8000", request)
```

`discover_models` explicitly reads `/models` to check connectivity and exact
model identity. `normalize_discovery` accepts an already captured response plus
caller declarations for system/developer roles, chat, streaming, tools,
structured output, and configured context. Anything `/models` cannot establish
and the caller did not declare stays `unknown`.

```python
from upgradeables_harness.runtime.adapters.openai_compatible import discover_models

capabilities = discover_models(
    "http://127.0.0.1:8000/v1",
    "server-model-id",
    declared_capabilities={"system_role": True, "streaming": True},
)
```

`normalize_response` provides the same common response fields for a completed
Chat Completions object. `normalize_stream` parses caller-supplied SSE chunks,
retains extension objects, terminal usage when supplied, tool-call deltas,
truncation, and partial/malformed stream status.

Compatibility beyond identity remains the caller's responsibility. Discovery
does not send synthetic prompts to probe roles or features. The executor remains
non-streaming; callers own the live SSE connection and pass chunks to the
normalizer. No Responses API path is implemented.

## OpenAI Agents SDK instructions

`apply_runtime_plan(agent, plan)` has no import-time dependency on the Agents
SDK; it accepts an object with an `instructions` attribute. It mutates that
attribute in place:

- static or missing instructions become preserved base plus runtime block;
- a synchronous instruction callback is wrapped and its returned base is
  preserved;
- coroutine functions and awaitables returned by ordinary callables are awaited,
  then composed;
- reapplication replaces the prior managed plan against the remembered original
  base instead of stacking old blocks;
- a manually replaced base becomes the new base on the next application.

```python
from upgradeables_harness.runtime.adapters.openai_agents import apply_runtime_plan

agent = apply_runtime_plan(agent, plan)
```

The helper captures an already compiled plan. It does not resolve a new task
from run context, clone the agent, map validators to guardrails, or map tool and
orchestration channels. `describe_capabilities` reports only integration
surfaces observable on the supplied object; it does not infer model behavior.
Applications should test their exact SDK version and callback form.

## Structured channels

The generic composer returns structured channels, but the current Ollama and
Chat Completions request builders transmit only the composed instructions and
user task. Before execution, application code must inspect:

- unavailable `tool_requirements`;
- `state_contract` storage needs;
- `validators` and their execution point;
- `orchestration` support;
- native `output_contract` support;
- compiler `warnings`.

Do not turn a missing tool or worker into a textual claim that it exists.

## Reproducible artifacts

`runtime.manifest.build_manifest` records version and plan identity, and
`write_run_artifacts` writes a new run directory containing manifest, task,
plan, compiled instructions, raw response, and metrics. Secret redaction is
best-effort; see [Security](SECURITY.md).

## Not implemented

The current tree has no Responses API composer, LangChain middleware, MCP
server, transparent localhost proxy, automatic
retries, or automatic capability probing during composition/execution.
OpenAI-compatible discovery establishes identity only unless the caller
supplies declarations; neither executor owns a live streaming connection.
These are integration opportunities, not implied features. Research rationale
is recorded in
[API and agent-framework adapters](../../research/runtime/api-agent-adapters.md)
and [local-model adapters](../../research/runtime/local-model-adapters.md).
