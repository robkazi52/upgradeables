# Directive compiler

The compiler converts the v0.3 [TaskResolution](V0.3_INPUT_CONTRACT.md) into a
typed [RuntimePlan](RUNTIME_PLAN.md). The implementation is a deterministic data
transform: it does not call a model, inspect a provider, or use an API key.

## Active selections

The compiler activates only `required_by_recipe` and `trigger_likely`. It does
not silently activate `conditional`, `optional`, or `needs_agent_evaluation`.
Duplicate slugs are retained only at their first active occurrence.

Before compilation, it requires the v0.3 schema/version contract, a non-empty
query, array-valued selection groups, known component slugs, and exact pinned
component versions. Missing or incompatible input raises `RuntimeCompileError`.

## Pipeline

The current order is:

1. Normalize `RuntimeContext`; validate profile and non-negative budget.
2. Load installed [runtime registry data](../../runtime/runtime_registry.json).
3. Validate the full v0.3 input and every referenced component pin.
4. Select active groups and add declared `requires` dependencies.
5. Fail closed on a selected `do_not_combine_with` conflict.
6. Apply review-only precedence and exclude non-runtime-injectable packages.
7. Choose `micro`, `standard`, or `full` per component.
8. Check host capabilities, route structured channels, and add task-resolution
   required checks to `validators`.
9. Order directives, deduplicate semantic groups, and retain mandatory
   invariants.
10. Compress levels to fit the budget, then remove optional directives if
    necessary.
11. Render the managed block and emit canonical hashes and an explain trail.

This sequence is intentionally stable. Changing it can change plan bytes and is
a compiler-version concern.

## Runtime form routing

Every operational package has a representation governed by
[RUNTIME_REPRESENTATION_SCHEMA.json](../../spec/runtime/RUNTIME_REPRESENTATION_SCHEMA.json).
Allowed forms are instruction directive, state contract, validator check,
orchestration control, tool capability, output contract, host behavior, mixed,
and not runtime injectable.

`not-runtime-injectable` packages are excluded with a recorded decision. Other
forms contribute only the channels populated by their representation. A state
or validator package may therefore produce an empty instruction capsule while
still producing a useful plan.

## Density selection

The initial profile mapping is:

```text
small  -> full
medium -> standard
strong -> micro
auto   -> standard
custom -> standard
```

The v0.3 complexity ceiling can reduce this: `L0` forces `micro`, and `L1`
allows at most `standard`. Each component's `maximum_default_verbosity` is a
second upper bound. See [Model Profiles](MODEL_PROFILES.md).

## Capabilities

Current host facts are instruction channel, named tools, state support, and
parallelism. `parallel-workers` checks the parallelism flag;
`durable-state` checks that state support is not empty, `none`, or
`unsupported`; other requirements match a named tool exactly.

When a capability is missing, the compiler:

- records a warning and capability decision;
- marks the tool requirement `available: false`;
- suppresses that component's ordinary directives;
- retains mandatory invariants for an injectable component;
- still emits the component's structured channels.

The adapter must surface this limitation and must not claim the capability
exists.

## Precedence and conflicts

`environment.review_only == true` suppresses components in the
`editing-repair` functional class. Selected component conflicts declared in
`do_not_combine_with` fail closed before a plan is emitted.

Current conflict handling does not synthesize blended instructions. The
compiler also does not infer undocumented conflicts from prose or lexical
similarity.

The v0.4 runtime-form audit found zero concrete pairwise conflicts that
required a `do_not_combine_with` declaration in the generated registry. This is
a negative audit result, not a claim that future components cannot conflict.
The fail-closed path is therefore covered with a synthetic conflicting registry
fixture rather than a fabricated production declaration.

## Ordering and deduplication

Directive groups are ordered by semantic category, then slug:

1. authority;
2. task/scope lock;
3. truth grounding and context retrieval;
4. state and drift control;
5. planning, framing, and meta control;
6. editing and repair;
7. validation;
8. output.

The declared dedupe groups and current rule are in
[dedupe_groups.json](../../runtime/dedupe_groups.json). A group identifies the
semantic comparison boundary; it does not make all member controls equivalent.
Within that boundary, only whitespace/case/punctuation-equivalent directives
are suppressed after their first occurrence. Distinct controls and mandatory
invariants survive in stable compiler order.

## Budget behavior

The compiler repeatedly lowers the last eligible compiled component from full
to standard to micro until the approximate estimate fits or no component can be
lowered. It then removes directives from non-required active additions in
reverse order. Hard restrictions and mandatory invariants are never silently
dropped.

If required content still exceeds the budget, compilation succeeds with an
explicit `Minimum required runtime capsule exceeds budget` warning. This allows
inspection, but an execution adapter may enforce a stricter policy and stop.

## Managed block

Hard restrictions from v0.3 precede compiled directives:

```text
<upgradeables-runtime version="0.4.0">
Task controls:
- ...
</upgradeables-runtime>
```

An empty set of hard restrictions and directives yields an empty capsule.
Composition with an existing host prompt is deliberately outside the compiler;
see [Authority and Composition](AUTHORITY_AND_COMPOSITION.md).

## Determinism

The compiler canonicalizes hashes with sorted, compact UTF-8 JSON. Determinism
depends on the complete task resolution, model profile, budget, host facts,
compiler version, and installed runtime registry. No timestamp or absolute
checkout path enters the plan hash.

There is no runtime-plan cache in the current implementation. Callers may cache
by all inputs above, but must not treat a task hash as anonymized data.
