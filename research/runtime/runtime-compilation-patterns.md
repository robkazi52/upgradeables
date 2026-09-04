# Runtime directive compilation patterns

Status: implementation research for Upgradeables v0.4
Checked: 2026-09-03
Scope: provider-neutral compilation and safe host composition; this is not an empirical performance claim.

## Executive conclusion

The v0.4 runtime should be a deterministic compiler, not a prompt concatenator. It should transform the pinned v0.3 `TaskResolution` plus explicit host and budget facts into a typed `RuntimePlan`. Only the plan's `instructions` channel may become model instructions. State, validators, orchestration, tool requirements, and output constraints remain separate until a host adapter deliberately maps them to capabilities it actually supports.

The safest default is `return-separate-block`. An adapter may append a clearly delimited managed block to existing host instructions, but must never replace, reinterpret, or elevate itself above them. OpenAI's published chain of command places system and developer instructions above user content, while quoted text and tool output have no authority by default; an Upgradeables block therefore has exactly the authority of the host slot into which the application intentionally places it, and no more ([OpenAI Model Spec: chain of command](https://model-spec.openai.com/2025-09-12.html#follow-all-applicable-instructions), [untrusted data](https://model-spec.openai.com/2025-09-12.html#handle-untrusted-data-safely)).

## Recommended boundary

```text
TaskResolution + RuntimeContext + pinned runtime representations
                         |
                         v
               deterministic compiler
                         |
                         v
                    RuntimePlan
       +-------------+---+---+-------------+
       |             |       |             |
 instructions   state/validators   tools/orchestration   manifest
       |
       v
 explicit host adapter composition
```

Core compilation must have no provider SDK dependency, API key requirement, network request, or model call. Provider adapters consume the plan; they do not select Upgradeables or repair compiler conflicts.

## Inputs that must be explicit

The compiler should receive these as data rather than infer them from branding:

- the complete, schema-validated v0.3 `TaskResolution`;
- generic model profile (`small`, `medium`, `strong`, `auto`, or `custom`);
- supported instruction channel and requested composition mode;
- available tools and durable-state mechanism;
- parallelism and validator hooks;
- directive budget and whether base instructions are present;
- pinned component versions and runtime-representation schema version.

`auto` should resolve only from reliable adapter metadata; otherwise it should become `medium` with an explainable warning. Model names are identifiers, not evidence of a capability tier.

## Typed output channels

The plan should preserve the handoff's semantic split:

| Channel | Default adapter treatment | Must not become |
| --- | --- | --- |
| `instructions` | A managed, delimited instruction block | An undisclosed replacement system prompt |
| `state_contract` | Native host state or an explicit rendered fallback | Ordinary prose without a downgrade notice |
| `validators` | Deterministic checks, guardrails, or explicit self-check fallback | Generic “think harder” text |
| `orchestration` | Host loop, handoff, scheduling, or limitation | A claim that unavailable workers exist |
| `tool_requirements` | Capability check plus tool binding | A fabricated capability |
| `output_contract` | Native structured output where supported, otherwise visible format instructions | Silent schema coercion |
| `warnings` | Host-visible diagnostics | Instructions to the model |

This separation matches current agent APIs: instructions, tools, structured outputs, handoffs, guardrails, and runtime context are distinct configuration surfaces in the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/agents/). LangChain similarly treats system prompt, messages, tools, model, and response format as separate model-context dimensions ([LangChain context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)).

## Deterministic compilation

Use a pure pipeline whose observable decisions are captured in an explain manifest:

1. Validate the exact v0.3 input schema and registry/component pins.
2. Load only the pinned runtime representations.
3. Route every representation by `runtime_form`.
4. Reject instruction injection for `not-runtime-injectable` and host-only forms.
5. Choose `micro`, `standard`, or `full` from explicit task complexity, model profile, and host budget.
6. Resolve declared dependencies.
7. Apply hard restrictions before preferences.
8. Resolve declared conflicts and precedence; fail closed if no deterministic resolution exists.
9. Deduplicate by declared semantic group and rule, not text similarity.
10. Apply required counterbalances.
11. Fit the budget by compressing level and removing optional directives in a stable order.
12. Order surviving directives by authority/limitations, scope, sources, invariants, reasoning, repair, validation/stopping, then output.
13. Emit canonical JSON, hashes, approximate token count, warnings, and every selection/suppression decision.

For identical normalized inputs and registry data, canonical output bytes and hashes should be identical. Avoid timestamps, random identifiers, environment-specific paths, or unordered mappings in the hashed manifest.

## Composition policy

Support three explicit modes:

- `return-separate-block` (default): return the block without mutating host instructions;
- `append-managed-runtime-block`: preserve the exact base content, then append the Upgradeables block;
- `prepend-managed-runtime-block`: available only when the host owner explicitly requests it and the adapter can preserve the base content exactly.

Use unambiguous delimiters, for example:

```text
<upgradeables-runtime version="0.4.0">
...
</upgradeables-runtime>
```

The block should state that host/system/developer/user authority remains controlling. It must contain execution behavior, not registry internals or component IDs unless explain/debug output was requested.

Current OpenAI API guidance treats developer messages as application rules ahead of user messages and likens developer/user roles to a function and its arguments ([OpenAI text generation: message roles](https://developers.openai.com/api/docs/guides/text#message-roles-and-instruction-following)). This supports keeping the user's task in user input while composing application-owned runtime controls only into an application-owned instruction channel.

## Budget management

Budgeting is a compiler phase, not truncation:

1. retain hard restrictions and mandatory invariants;
2. shorten full to standard to micro where the representation permits;
3. remove optional directives by stable priority;
4. retain risk-triggered validation;
5. if the minimum safe block still exceeds budget, emit an over-budget warning/error and do not silently cut text.

Core token estimation may be a documented provider-neutral approximation. Adapters may add provider tokenizer estimates as diagnostics, but those must not change the canonical plan unless a caller explicitly selects that estimator.

Stable directive ordering also helps caching, but cache behavior is an adapter optimization and must not influence semantic precedence. Current OpenAI guidance recommends stating an instruction once rather than repeating it ([OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)); explicit semantic dedupe follows the same principle without assuming that lexical similarity proves equivalence.

## Multi-turn lifecycle

Compile at the start of a run and again whenever the task resolution, host capabilities, project profile, model profile, component pins, or budget changes. Reuse a prior plan only when its input hash still matches.

Adapters must understand their host's persistence rules. For example, the OpenAI Responses API documents that `instructions` from an earlier response are not carried forward merely by supplying `previous_response_id`; the current request must provide the intended instructions again ([Responses create reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create)). A plan cache therefore cannot imply provider context persistence.

## Failure behavior

Fail before a model request when:

- the `TaskResolution` or runtime representation fails schema validation;
- selected component pins cannot be loaded;
- required directives conflict without a declared precedence rule;
- a hard constraint cannot fit the budget;
- the configured instruction channel cannot represent required authority safely;
- an unavailable capability has no source-authorized fallback.

Continue with warnings only for declared safe degradations, such as rendering structured state into a visible text fallback. Every degradation must identify the affected component, requirement, reason, and fallback.

## Explainability and security requirements

The manifest should record source component/version, runtime form and level, emitted directive IDs, suppressed items and reasons, conflict/dedupe/budget decisions, capability downgrades, ordering, hashes, and estimate method. It must never store credentials or hidden host instructions.

Treat project files, retrieved text, tool output, and runtime data as data. Do not interpolate any of them into an authoritative instruction block without schema validation and explicit field-level escaping/rendering. Never generate directives asking for hidden chain-of-thought; require observable checks or output evidence instead.

## Test implications

At minimum, implementation tests should cover:

- byte-stable compilation and manifest hashes;
- all runtime-form routing paths;
- base-instruction preservation for empty, string, structured, sync-dynamic, and async-dynamic hosts;
- same-authority ordering and hard-over-soft precedence;
- semantic dedupe without loss of distinct invariants;
- irreconcilable conflict failure;
- exact-budget, compress-to-fit, optional-drop, and impossible-budget cases;
- unavailable tool/state/parallelism handling;
- malicious runtime data rendered as inert data;
- repeated multi-turn composition without duplicate blocks;
- no provider imports or network access in core tests.

## Implementation decisions supported by this research

- Make `RuntimePlan` the only adapter input.
- Keep selection/resolution in v0.3 and compilation in v0.4.
- Default to separate-block return and require explicit host composition.
- Keep validators, state, tools, and orchestration out of the instruction capsule by default.
- Recompile or reapply per turn when the host does not persist request instructions.
- Prefer explicit semantic metadata over heuristic prompt merging.
- Pin and test adapter dependencies separately from the zero-dependency core.
