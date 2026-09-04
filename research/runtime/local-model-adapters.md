# Local model adapter research

Research snapshot: 2026-09-03. This brief covers the required Ollama adapter and the generic OpenAI-compatible HTTP adapter. It uses vendor/project documentation rather than assuming that every server advertising "OpenAI compatibility" implements the same protocol.

## Recommendation

Implement two distinct adapters:

1. `ollama`, against Ollama's native `/api` surface.
2. `openai-compatible`, against a deliberately small, configurable `/v1/chat/completions` contract.

Do not implement Ollama by routing it through the generic adapter. Ollama's native API exposes better model discovery, active-context, timing, token, and streamed-error information. Keep OpenAI compatibility as a separate interoperability path.

Both adapters should consume a completed `RuntimePlan`; neither should classify tasks or compile directives. They should preserve caller-provided base instructions, place the managed runtime block in a supported instruction channel, keep the actual task in a distinct user message, and report rather than fabricate unavailable capabilities.

## Ollama native adapter

### Transport and request shape

The default native base URL is `http://localhost:11434/api`. Local access requires no authentication; Ollama's direct cloud API does require authentication. The adapter therefore must label an endpoint as local or remote from the resolved URL, not merely from the adapter name. Sources: [API introduction](https://docs.ollama.com/api/introduction), [authentication](https://docs.ollama.com/api/authentication).

Use `POST /api/chat` for the first implementation. It accepts a model and a message history, supports tools, a structured-output `format`, runtime `options`, streaming, thinking controls, and keep-alive controls. Streaming defaults to `true`; set it explicitly so request manifests are unambiguous. A completed response includes the actual model identifier, stop reason, token counts, and timing fields. Sources: [`/api/chat` reference](https://docs.ollama.com/api/chat), [usage metrics](https://docs.ollama.com/api/usage), [streaming format](https://docs.ollama.com/api/streaming).

Recommended request composition:

```json
{
  "model": "configured-model",
  "messages": [
    {
      "role": "system",
      "content": "<base instructions, if any>\n\n<delimited Upgradeables runtime block>"
    },
    {
      "role": "user",
      "content": "<user task>"
    }
  ],
  "stream": false,
  "options": {}
}
```

If there are no caller-provided base instructions, the system message contains only the delimited runtime block. Do not mutate or create a permanent Modelfile. Ollama's Modelfile supports persistent `SYSTEM`, template, and `num_ctx` settings, but v0.4 needs dynamic request-level control; the handoff also explicitly forbids modifying the model permanently by default. Source: [Modelfile reference](https://docs.ollama.com/modelfile).

Treat the exact interaction between a model's stored system/template and a per-request system message as model/template dependent. Preserve every base instruction known to the caller in the composed request, expose the exact message array in dry-run output, and add an integration fixture with a model that has a stored system prompt before claiming preservation across that boundary.

### Capability discovery

Use read-only discovery before execution, with a short cache keyed by endpoint, server version, and exact model identifier:

| Check | Native endpoint | Use |
|---|---|---|
| Server reachable/version | `GET /api/version` | Diagnostics and compatibility record |
| Installed models | `GET /api/tags` | Verify that an exact local model name exists; never auto-pull |
| Model metadata | `POST /api/show` | Read `capabilities`, `details`, `parameters`, `template`, and `model_info` |
| Active allocation | `GET /api/ps` | Read the context allocated to a loaded model and processor placement |

Sources: [version](https://docs.ollama.com/api-reference/get-version), [list models](https://docs.ollama.com/api/tags), [show model details](https://docs.ollama.com/api-reference/show-model-details), [running models](https://docs.ollama.com/api/ps).

`/api/show.capabilities` is authoritative only for the features it explicitly reports. Do not infer tools, vision, or thinking from a model's name. Structured output is an endpoint feature, but output quality remains model dependent; absence of a dedicated capability flag must remain `unknown`, not `false` or `true`. Ollama documents tool calling and structured output independently: [tool calling](https://docs.ollama.com/capabilities/tool-calling), [structured outputs](https://docs.ollama.com/capabilities/structured-outputs).

Represent discovery as tri-state values (`supported`, `unsupported`, `unknown`) plus evidence, for example:

```json
{
  "chat": {"status": "supported", "evidence": "native endpoint"},
  "tools": {"status": "supported", "evidence": "/api/show capabilities"},
  "structured_output": {"status": "unknown", "evidence": "not declared per model"},
  "effective_context_tokens": {"value": 32768, "evidence": "/api/ps"}
}
```

### Context limits

Keep three values separate:

- `model_max_context`: the architecture/model metadata value from the `*.context_length` entry in `/api/show.model_info`;
- `configured_context`: an explicit per-request `options.num_ctx`, model parameter, or server setting;
- `effective_context`: the allocated context reported for a loaded model by `/api/ps`.

The architecture maximum is not proof that the running server allocated that amount. Ollama currently chooses defaults based on available VRAM and larger context increases memory use. The native API can set `options.num_ctx`; the OpenAI-compatible Ollama endpoint cannot set context per request and instead documents creating a model with `PARAMETER num_ctx`. Sources: [context-length guidance](https://docs.ollama.com/context-length), [FAQ API `num_ctx` example](https://docs.ollama.com/faq), [OpenAI compatibility context note](https://docs.ollama.com/api/openai-compatibility).

Budget against `effective_context` when known. Otherwise use an explicitly configured limit. If neither is known, report it as unknown and use the compiler's conservative configured budget; never budget against the theoretical model maximum silently. Before sending, reserve space for user/history tokens, output tokens, template overhead, and the runtime capsule. A context-overflow response is not retryable with the same payload: recompile to a smaller declared budget or return an explicit limitation.

### Structured output

The native chat endpoint accepts either `"format": "json"` or a JSON Schema object. Ollama recommends also grounding the request with the schema and using a low temperature for deterministic results. Source: [structured outputs](https://docs.ollama.com/capabilities/structured-outputs).

Adapter policy:

- Keep runtime directive compilation independent of response formatting.
- Send a schema only when the caller or execution channel requires structured output.
- Validate returned JSON locally against the requested schema even when constrained decoding was requested.
- Report parse failure and schema mismatch as distinct adapter failures.
- Do not silently fall back from schema-constrained output to free text. An opt-in fallback can issue a new request and must record both attempts.
- Prefer non-streaming for schema-constrained output because Ollama documents it as simpler and better suited to structured responses.

### Streaming and usage

Ollama native streaming uses newline-delimited JSON, not OpenAI-style SSE. Accumulate `message.content`, tool calls, and any other public response fields. The terminal object carries completion metadata; record missing metrics as `null`, never zero. Normalize at least:

```text
model
finish_reason
prompt_tokens
output_tokens
total_duration_ns
load_duration_ns
prompt_eval_duration_ns
generation_duration_ns
partial
raw_provider_metadata
```

When the connection ends without a terminal `done: true`, mark the response incomplete. Preserve partial public output and raw chunks. Ollama can emit an `{"error": ...}` NDJSON object after the HTTP response has already begun, so a `200` status does not prove that a stream completed successfully. Source: [Ollama API errors](https://docs.ollama.com/api/errors).

## Generic OpenAI-compatible adapter

### Minimum portable contract

Target only this baseline initially:

```text
GET  <base_url>/models
POST <base_url>/chat/completions
```

Configuration owns the already-versioned base URL (normally ending in `/v1`), exact model ID, optional API-key environment variable, instruction role, timeout, streaming choice, structured-output mode, context limit, and explicitly declared host capabilities. Do not concatenate `/v1` unconditionally.

The OpenAI Chat Completions contract uses an ordered `messages` array, supports system/developer and user roles, optionally streams with server-sent events, and returns a finish reason and usage object. Parameter support can differ by model. Sources: [Chat Completions API reference](https://developers.openai.com/api/reference/resources/chat), [Models API reference](https://developers.openai.com/api/reference/resources/models).

Use `system` as the default instruction role for local compatibility. Permit an explicit `developer` override for servers that support current OpenAI semantics. Never retry a rejected instruction role by moving the runtime block into the user task: that silently changes authority. If the configured role is unsupported, return a capability limitation or require the caller to select an explicit visible-user-block mode.

Request composition should copy existing messages and preserve their order. If the caller supplies base instructions, append a clearly delimited managed block to those instructions without deleting them. Keep the actual task in its own final `user` message. Multiple-system-message behavior varies across emulators, so a single composed instruction message is the conservative default; dry-run must show the full redacted body.

### Discovery is intentionally limited

The portable `/v1/models` object supplies basic identity/ownership metadata, not context size, instruction-role support, tools, or structured-output support. Therefore:

- use `/models` only for connectivity and exact-model availability;
- never derive the `small`/`medium`/`strong` runtime profile from model naming;
- require explicit configuration for context size and non-baseline capabilities;
- keep unverified capabilities `unknown`;
- allow named server profiles only when backed by that server's current official contract and version evidence;
- never probe with user/project content; any optional capability probe must use fixed synthetic input and be opt-in or part of `doctor`.

The non-uniformity is visible in primary server documentation. Ollama says it implements only parts of the OpenAI API and enumerates supported fields. llama.cpp says its routes are OpenAI-compatible but makes no strong claim of complete compatibility; its model response includes project-specific metadata and its server context is configured separately. LM Studio and vLLM each document their own endpoint sets and structured-output details. Sources: [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility), [llama.cpp server](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), [LM Studio OpenAI compatibility](https://lmstudio.ai/docs/developer/openai-compat), [vLLM online serving](https://docs.vllm.ai/en/latest/serving/online_serving/).

### Context and structured-output policy

There is no portable OpenAI-compatible request field that sets or reliably discovers a local server's context allocation. Make `context_window_tokens` an optional-but-explicit adapter setting. When absent, report unknown and enforce only the compiler's conservative capsule budget; strict runs that cannot establish fit should fail before sending.

Support structured output as a negotiated/configured feature, not an assumed baseline:

```text
off
json_object
json_schema
provider_extension
```

For standard-shaped requests, use `response_format`. Always validate the response locally. A `400`/`422` indicating an unsupported schema or field is a capability mismatch, not permission to resend unconstrained. Provider extensions belong in named profiles, not the generic core. For example, llama.cpp documents an OpenAI-inspired schema variant, LM Studio documents OpenAI-shaped `json_schema`, and vLLM also exposes version-specific `structured_outputs` extension fields. Sources: [llama.cpp response formats](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), [LM Studio structured output](https://lmstudio.ai/docs/developer/openai-compat/structured-output), [vLLM structured outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/).

### Streaming and response parsing

Parse OpenAI-compatible streaming as SSE and tolerate ordinary extension fields. Do not require unknown fields to be absent. Preserve the final model identifier and `finish_reason` when provided. Usage is optional in streamed responses and may appear only in a terminal usage chunk; the official contract warns that an interrupted stream may never deliver it. Source: [Chat Completions streaming response](https://developers.openai.com/api/reference/resources/chat).

The adapter must not treat socket EOF, `[DONE]`, an HTTP success status, or a finish reason as interchangeable:

- `[DONE]`/clean terminal event: transport completed;
- `finish_reason=length`: completed transport but truncated model output;
- EOF before terminal marker: interrupted/partial;
- non-2xx: request failure, parse body best-effort;
- 2xx with malformed payload: protocol failure.

## Unified failure contract

Normalize provider-specific failures without discarding the raw status/body:

| Category | Examples | Default action |
|---|---|---|
| `endpoint_unavailable` | refused connection, DNS failure | Retry only under caller policy |
| `timeout` | connect/read/deadline | Retry only before response bytes; otherwise partial |
| `authentication` | 401/403 | Never retry automatically |
| `model_unavailable` | Ollama 404, configured model absent | Never pull/download; report exact model |
| `invalid_request` | malformed body, unsupported field | Never retry unchanged |
| `capability_mismatch` | rejected role/schema/tool field | Fail closed or use explicit pre-approved fallback |
| `context_overflow` | request exceeds active context | Recompile smaller or return limitation |
| `rate_limited_or_overloaded` | 429, local queue overload | Bounded backoff if enabled |
| `server_error` | 5xx | Bounded retry only before output begins |
| `stream_interrupted` | mid-stream error/EOF | Preserve partial output; do not auto-replay |
| `malformed_response` | invalid JSON/SSE shape | Preserve raw body and fail |
| `structured_output_invalid` | parse/schema validation failure | Fail or explicit recorded retry |

Ollama documents JSON error objects and common statuses `400`, `404`, `429`, `500`, and `502`, plus error records embedded in an already-started NDJSON stream. Its FAQ also documents queue overload behavior. Sources: [errors](https://docs.ollama.com/api/errors), [FAQ](https://docs.ollama.com/faq).

Retries must be bounded, observable, and recorded in the run manifest. Do not automatically replay a request after any response content has been received: it can duplicate text, tool calls, or compute while hiding a partial failure. Redact the configured authorization header and key environment variable from exceptions, logs, dry-run output, and saved raw HTTP diagnostics.

## Proposed adapter data model

Keep capability evidence separate from request results:

```text
HostCapabilities
  endpoint_type: loopback | private-network | remote | unknown
  server_kind/version
  model_id
  instruction_roles: tri-state map
  streaming/tools/structured_output: tri-state
  model_max_context_tokens
  configured_context_tokens
  effective_context_tokens
  evidence[]

AdapterResult
  response_text
  raw_response
  model_id
  finish_reason
  usage (nullable fields)
  timing (nullable fields)
  partial
  attempts[]
  runtime_plan_hash
```

Endpoint locality should be derived conservatively: loopback and local IPC are on-device; a LAN hostname/IP is still a network endpoint and should be identified as `private-network`, not quietly labeled local. Never send project data until the user has selected that endpoint/adapter.

## Required tests

Use mock HTTP servers for the normal suite and make live Ollama tests optional/skipped when unavailable. Cover:

1. base instructions retained and runtime block delimited;
2. user task remains a distinct user message;
3. dry-run performs no generation request;
4. native Ollama version/tags/show/ps discovery and tri-state evidence;
5. exact model name recorded; missing model does not trigger a pull;
6. explicit `num_ctx`, reported active context, and unknown-context behavior;
7. native structured JSON request plus local schema validation failure;
8. native NDJSON success and mid-stream `error` object;
9. generic non-streaming and SSE parsing, including missing final usage;
10. configurable `system` versus `developer` role without silent user-role fallback;
11. generic `json_schema` rejection classified as capability mismatch;
12. timeout before bytes versus interruption after partial output;
13. `400`, `401`, `403`, `404`, `422`, `429`, and `5xx` normalization;
14. malformed success bodies and unknown extension-field tolerance;
15. authorization/key redaction in logs, exceptions, manifests, and dry-run;
16. no automatic model downloads, Modelfile changes, remote calls, or unsupported-tool claims.

## Implementation decisions to lock before coding

- Native Ollama is the preferred Ollama path; OpenAI-compatible Ollama is only a generic-adapter conformance target.
- Generic v0.4 baseline is Chat Completions, not an opportunistic mix of Chat Completions and Responses.
- `system` is the portable default; `developer` and no-instruction-role modes are explicit configuration.
- Unknown context/capabilities stay unknown, with evidence attached.
- Structured-output fallback is opt-in and recorded, never silent.
- A model is never downloaded or permanently modified by an inference command.
- Metrics absent from a provider response are `null`, not estimated or zero.
- No mid-stream automatic replay.
