# API and agent-framework adapter research

Status: implementation research for Upgradeables v0.4
Checked: 2026-09-03
Scope: generic output, OpenAI-style requests, OpenAI Agents SDK, optional LangChain and MCP surfaces.

## Executive conclusion

Implement adapters as thin consumers of `RuntimePlan`. The core compiler should return a separate managed instruction block and structured non-instruction channels. An adapter may map those channels to a host only after it checks the host's declared capabilities, preserves existing instructions, and records degradations.

The required first-class API surfaces should be:

1. a dependency-free generic text/JSON renderer;
2. a configurable OpenAI-compatible request composer, with Responses and Chat Completions treated as different dialects;
3. an optional OpenAI Agents SDK helper based on dynamic `instructions`;
4. optional extras for LangChain and MCP, neither imported by core.

## Cross-adapter contract

Each adapter should accept an already compiled `RuntimePlan` plus an explicit host composition configuration. It should not rerun component selection, silently alter the plan, infer a model capability tier from a product name, or make a network call during composition.

Common outputs should include:

- the preserved user task/input;
- the exact base instructions as supplied by the host application;
- the exact managed Upgradeables block;
- the final composed instruction value or a separate-block result;
- mapped tools, validators, state, output schema, and orchestration controls;
- warnings for every unsupported channel;
- adapter name/version and capability facts used.

Secrets must be accepted through caller-owned configuration or environment-variable names, never copied into a plan, manifest, log, exception, or dry-run rendering.

## Generic adapter

This is the universal fallback and should remain in core:

```text
render_text(plan) -> managed instruction block
render_json(plan) -> canonical RuntimePlan JSON
compose(base, block, mode) -> composed text or separate parts
```

Default `mode` is `return-separate-block`. Text-only hosts may render state, validators, or output constraints only through explicit, labeled downgrade functions; the adapter must add a warning rather than silently folding every channel into prose.

## OpenAI Responses request composer

Current OpenAI documentation exposes a top-level `instructions` field for system/developer-level behavior and an `input` field for user input. `instructions` takes priority over `input`, and it applies only to the current response request ([text generation guide](https://developers.openai.com/api/docs/guides/text#message-roles-and-instruction-following)). The API reference further notes that earlier instructions are not carried over through `previous_response_id` ([Responses create](https://developers.openai.com/api/reference/cli/resources/responses/methods/create)).

Recommended mapping:

```text
base application instructions + managed runtime block -> instructions
user task and attachments                         -> input
native callable capabilities                      -> tools
native response schema, when requested/supported  -> text/output format
```

Consequences:

- compose the block on every request that needs it, including continuations;
- do not put the user task into the managed block;
- do not assume server-side conversation state persists request instructions;
- preserve returned items exactly when the calling application owns manual conversation replay;
- treat provider usage and request identifiers as optional diagnostics.

The composer should produce a request patch or a complete request object only when the caller explicitly supplies the base object. It should not transmit it. This keeps dry runs testable without credentials.

## OpenAI-compatible Chat Completions composer

“OpenAI-compatible” is a transport claim, not a semantic guarantee. Current OpenAI Chat Completions supports `developer`, `system`, `user`, `assistant`, and tool-related messages; current OpenAI guidance prefers `developer` for newer models while retaining `system` for compatibility ([Chat Completions reference](https://developers.openai.com/api/reference/cli/resources/chat/subresources/completions)). Other servers may implement only a subset.

Require explicit configuration or a caller-provided capability probe result:

```text
api_shape: responses | chat-completions
instruction_role: developer | system | none
supports_structured_output: true | false
supports_tools: true | false
supports_streaming: true | false
```

For Chat Completions, preserve all existing messages in order. If the caller owns an existing developer/system message, append the managed block to that message only when explicitly requested; otherwise return a separate proposed message. Never reorder user, assistant, or tool history. If neither instruction role is supported, use the generic separate-block result or return an explicit limitation—do not disguise the runtime block as user content without caller opt-in.

Provider-specific features must be capability gated. The OpenAI Agents SDK itself warns that non-OpenAI providers differ in support for Responses, structured outputs, multimodal inputs, and tools ([Agents SDK model providers](https://openai.github.io/openai-agents-python/models/)).

## OpenAI Agents SDK adapter

### Current supported hook

The current Python SDK accepts `Agent.instructions` as either a string or a sync/async function receiving `(RunContextWrapper, Agent)` and returning a string ([Agents SDK dynamic instructions](https://openai.github.io/openai-agents-python/agents/#dynamic-instructions), [Agent API reference](https://openai.github.io/openai-agents-python/ref/agent/)). This is the appropriate v0.4 integration hook.

Important limitation: the callback receives the run context and agent, not the raw `Runner.run` input as a dedicated argument. The host application should therefore put the normalized project/task or a precompiled plan into its typed context before the run. The adapter must not guess a task by scraping conversation history.

### Helper shape

Provide an optional helper conceptually like:

```python
upgradeables_instructions(
    base_instructions,
    *,
    plan_getter,
    composition_mode="append-managed-runtime-block",
)
```

It should return a sync or async dynamic-instructions callback. On each invocation it:

1. obtains or compiles a plan from explicit typed context;
2. evaluates the caller-supplied base instructions, whether static or dynamic;
3. composes the exact base result with one delimited runtime block;
4. returns the combined string without mutating the source `Agent`.

If helper installation on an existing agent is offered, prefer returning a cloned/configured agent rather than in-place mutation. The SDK documents `Agent.clone()` as a shallow copy, so callers must understand that list attributes such as tools and handoffs remain shared unless replaced ([Agents SDK cloning](https://openai.github.io/openai-agents-python/agents/#cloningcopying-agents)).

Do not use `call_model_input_filter` as the primary integration hook. That hook can edit prepared input immediately before a model call and can preserve instructions when returning `ModelInputData`, but it is broader and easier to misuse; reserve it for advanced host-controlled history redaction or late input shaping ([Agents SDK call-model input filter](https://openai.github.io/openai-agents-python/running_agents/#call-model-input-filter)).

### Mapping non-instruction channels

- `tool_requirements`: preflight against `agent.tools` and MCP-backed tools; missing requirements become explicit limitations.
- `validators`: host-side deterministic validation first. Agents SDK input/output guardrails can be optional mappings, but input guardrails run only on the first agent and output guardrails only on the final-output agent; they are not universal workflow validators ([Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/#workflow-boundaries)).
- `output_contract`: use `output_type` only when the contract is representable as a supported structured type.
- `orchestration`: map only declared, supported handoffs/agent-as-tool behavior; never create workers from prose.
- `state_contract`: keep in application context/state; render to text only through an explicit fallback.

### Runs, streaming, usage, and tracing

Support ordinary and streamed runs without changing compilation semantics. The SDK offers `Runner.run`, `run_sync`, and `run_streamed`; streamed consumers must drain `stream_events()` before treating the run as complete ([Agents SDK running](https://openai.github.io/openai-agents-python/running_agents/), [streaming](https://openai.github.io/openai-agents-python/streaming/)).

Capture `raw_responses`, normalized usage, optional request IDs, and optional raw usage. The current SDK documents that raw usage and request IDs may be absent and that streaming totals can lag until final chunks are processed ([Agents SDK results](https://openai.github.io/openai-agents-python/results/), [usage](https://openai.github.io/openai-agents-python/usage/)).

Tracing is enabled by default in the SDK. The integration docs should explain disabling it for local/non-OpenAI use and excluding sensitive inputs/outputs from traces; no v0.4 helper should enable verbose logging or sensitive tracing implicitly ([Agents SDK configuration](https://openai.github.io/openai-agents-python/config/#tracing)).

### Dependency and compatibility policy

Keep this adapter behind an extra and import it lazily. Pin a tested lower/upper compatibility range in the extra, exercise it in a separate CI job, and fail with an installation hint when absent. Do not expose third-party SDK objects in the core compiler API.

## Optional LangChain adapter

Current LangChain Python supports runtime system-prompt modification through agent middleware. Although `@dynamic_prompt` can generate a system prompt from `ModelRequest`, the safer preservation path for Upgradeables is `@wrap_model_call`: read `request.system_message.content_blocks`, append a new text block, and call `request.override(system_message=...)`. The official example explicitly recommends this pattern to preserve existing structure ([LangChain custom middleware: dynamic prompt](https://docs.langchain.com/oss/python/langchain/middleware/custom#dynamic-prompt)).

Recommendations:

- implement as a separate extra, not a core dependency;
- append a content block rather than flattening or replacing structured content;
- document middleware ordering and test coexistence with other prompt middleware;
- read plan/task data from explicit runtime context;
- keep state updates, tool selection, and response validation in their own middleware/hooks;
- expose only tools the plan requires and the host actually authorizes.

LangChain's current middleware docs distinguish node-style sequential hooks from wrap-style control-flow hooks and emphasize independent tests and deliberate order ([middleware overview](https://docs.langchain.com/oss/python/langchain/middleware/overview), [custom middleware best practices](https://docs.langchain.com/oss/python/langchain/middleware/custom#best-practices)).

## Optional MCP adapter

MCP should expose compiler functionality, not promise invisible instruction injection. The protocol distinguishes prompts (user-controlled), resources (application-controlled), and tools (model-controlled) ([MCP server overview, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/index)). MCP prompts are explicitly designed for user selection, and servers must declare prompt capability before clients list/get them ([MCP prompts specification](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)).

Useful tool surfaces are:

```text
resolve_task
compile_runtime_plan
get_runtime_directives
get_component
get_project_profile
build_skill_brief
```

A client or host must still decide when to call a tool and where to compose returned instructions. If prompts are offered, label them as explicit user-invoked templates. Validate every argument and result, negotiate capabilities, and treat server-returned content as untrusted data until the host deliberately maps it.

## Capability and failure matrix

| Surface | Native dynamic instructions | Base preservation | Non-text channels | Required behavior when absent |
| --- | --- | --- | --- | --- |
| Generic | Returned block only | Caller-controlled | JSON plan only | Warn on any text downgrade |
| Responses | Per-request `instructions` | Compose before request | Tools/output format vary | Reapply each request; gate features |
| Compatible chat | Role varies by server | Preserve message list; explicit merge | Highly variable | Require config/probe; fail explicit |
| Agents SDK | Sync/async callback | Evaluate base then append | Tools, guardrails, output type, context | Preflight and document workflow boundaries |
| LangChain | Middleware | Append structured content block | Separate middleware/state/tool surfaces | Optional extra; no core import |
| MCP | Prompt/tool exposure, client-controlled | Host decides | Tools/resources/prompts | Never claim automatic injection |

## Tests implied by the adapter design

- no network calls in composition or dry-run tests;
- exact preservation of static and dynamic base instructions;
- sync and async Agents SDK callbacks;
- repeated callback invocation without duplicate managed blocks;
- task/project context missing, invalid, or changed between runs;
- Responses continuation reapplication;
- developer/system/none role configurations for compatible chat;
- structured message content preserved byte-for-byte outside the appended block;
- absent tools, state, validator hooks, and structured output support;
- LangChain middleware order and structured content blocks;
- MCP capability negotiation and malicious returned content;
- credentials redacted from plans, diagnostics, exceptions, and snapshots;
- optional dependencies absent and version incompatibility messages.

## Recommended v0.4 implementation order

1. Generic renderer/composer and adapter conformance fixtures.
2. OpenAI-compatible request composers as pure data transforms.
3. OpenAI Agents SDK optional helper with static/sync/async base preservation.
4. Dry-run examples and CI tests with no paid calls.
5. LangChain extra only after the core interfaces stabilize.
6. MCP tools/prompts only if time remains; do not block v0.4 on it.
