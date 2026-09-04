# Runtime reasoning middleware

The v0.4 runtime compiler turns a deterministic v0.3 task selection into a
compact, provider-neutral `RuntimePlan`. It does not make a model intrinsically
more capable, and it does not inject every Upgradeable as prompt text. The plan
keeps instructions, state, validators, orchestration, tool requirements, and
output contracts in separate channels so a host can apply only the mechanisms
it actually supports.

The compiler is local, deterministic, and requires no API key or provider SDK.
Network access occurs only when application code explicitly calls a network
adapter.

## Directory roles

The top-level [`runtime/`](../../runtime/) directory keeps its v0.3 role: it
contains generated low-context projections such as the router, compact
component cards, recipe packs, and the runtime registry used as compiler source
material. These files remain useful to models and tools that consume the
repository without importing Python.

Executable v0.4 middleware lives separately under
`src/upgradeables_harness/runtime/`. That package loads the generated installed
data, compiles `RuntimePlan` values, and provides adapters and evaluation code;
it does not replace or redefine the top-level projections. Contributors should
change the canonical source/generator and rebuild derived data rather than hand
editing only one generated copy.

## Quick start

Compile a task to the default text capsule:

```bash
upgradeables runtime compile \
  "fix the failing parser test without refactoring unrelated code"
```

Inspect selection, suppression, deduplication, budget, and warning decisions:

```bash
upgradeables runtime explain \
  "review this change for breaking API behavior" \
  --model-profile small
```

Return the complete plan as JSON:

```bash
upgradeables runtime plan \
  "review this change for breaking API behavior" \
  --max-directive-tokens 300
```

Compile a saved v0.3 resolution rather than resolving raw text again:

```bash
upgradeables runtime plan --resolution task-resolution.json
```

List the generic instruction-density profiles:

```bash
upgradeables runtime profiles
```

Preview an end-to-end Ollama request without network access or artifacts:

```bash
upgradeables run ollama \
  --model your-already-installed-model \
  --task "review this function for a regression" \
  --dry-run \
  --format json
```

Execute against an explicitly selected Ollama server and record a reproducible
artifact set:

```bash
upgradeables run ollama \
  --model your-already-installed-model \
  --task "review this function for a regression" \
  --endpoint http://127.0.0.1:11434 \
  --output-root .upgradeables/runs
```

The command never discovers or downloads a model implicitly. The exact model
identifier must already be available at the selected endpoint. See
[Adapters](ADAPTERS.md) for options, output, and limitations.

The common flags are `--project`, `--model-profile`,
`--max-directive-tokens`, `--format text|json|agent-instructions|debug`,
`--explain`, and
`--no-project-profile`. `runtime plan` always emits JSON.

## Python API

For raw task text, use the high-level entry point:

```python
from upgradeables_harness.runtime import compile_task

plan = compile_task(
    "review this change for breaking API behavior",
    project=".",
    model_profile="small",
    max_directive_tokens=300,
)
```

For deterministic replay from a saved v0.3 resolution:

```python
from upgradeables_harness.runtime import RuntimeContext, compile

context = RuntimeContext(model_profile="strong", max_directive_tokens=250)
plan = compile(task_resolution, context)
```

The accepted upstream contract is documented in
[v0.3 Input Contract](V0.3_INPUT_CONTRACT.md). The formal request and output
schemas are [Runtime Compile Request](../../spec/runtime/RUNTIME_COMPILE_REQUEST_SCHEMA.json)
and [Runtime Plan](../../spec/runtime/RUNTIME_PLAN_SCHEMA.json).

## Documentation map

- [Runtime Plan](RUNTIME_PLAN.md): output channels, fields, hashes, and use.
- [Directive Compiler](DIRECTIVE_COMPILER.md): deterministic pipeline,
  precedence, dedupe, and budget behavior.
- [Model Profiles](MODEL_PROFILES.md): `small`, `medium`, `strong`, `auto`, and
  `custom` instruction density.
- [Adapters](ADAPTERS.md): generic, Ollama, OpenAI-compatible, and OpenAI Agents
  SDK helpers.
- [Authority and Composition](AUTHORITY_AND_COMPOSITION.md): safe instruction
  placement and base-prompt preservation.
- [Security](SECURITY.md): trust boundaries, credentials, endpoints, and
  artifact privacy.
- [Versioning](VERSIONING.md): independent runtime, registry, component, and
  schema versions.
- [Evaluation](EVALUATION.md): offline harness, conditions, graders, and honest
  interpretation.

The implementation is derived from the full 96-package
[runtime registry](../../runtime/runtime_registry.json), whose source-facing
coverage is recorded in the
[runtime-form audit](../../audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.md).

## Current boundaries

- Runtime compilation is explicit; project initialization does not turn on
  global instruction injection.
- The CLI compiles plans, defaults evaluation to the offline mock, and exposes
  explicit non-streaming Ollama task execution plus Ollama/OpenAI-compatible
  live evaluation. Live evaluation starts with a no-network/no-write dry-run.
- The OpenAI-compatible helper targets `/v1/chat/completions`, not the Responses
  API. `/models` discovery checks identity only; other capabilities stay
  caller-declared or unknown.
- Ollama has explicit read-only discovery, and both HTTP dialects have offline
  stream normalizers. The included executors still parse a single JSON response;
  callers must own live NDJSON/SSE connections and pass chunks to a normalizer.
- Standalone discovery and execution are explicit. A non-dry Ollama evaluation
  includes documented read-only exact-model preflight before experiment
  creation. No adapter retries automatically, downloads a model, or permanently
  modifies one.
- LangChain, MCP, and a universal proxy are not implemented.
- No paid API tests or model downloads run automatically.
- No empirical superiority or model-equivalence claim has been established.
