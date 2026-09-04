# Runtime versioning

Runtime behavior is governed by several independent versions. Do not replace
them with one ambiguous “Upgradeables version.”

| Dimension | Identifies | Current location |
| --- | --- | --- |
| Distribution/harness version | Installed Python package and CLI | `upgradeables_harness.constants.HARNESS_VERSION` |
| Registry version | Component catalog generation consumed by v0.3 | `upgradeables_harness.constants.REGISTRY_VERSION` |
| Component version | Semantics of one pinned Upgradeable | Registry and runtime component record |
| TaskResolution schema | v0.3 compiler input wire contract | [TASK_RESOLUTION_SCHEMA.json](../../spec/harness/TASK_RESOLUTION_SCHEMA.json) |
| Runtime representation schema | Per-component runtime fields | [RUNTIME_REPRESENTATION_SCHEMA.json](../../spec/runtime/RUNTIME_REPRESENTATION_SCHEMA.json) |
| Runtime compiler version | Selection activation, routing, ordering, dedupe, and budget behavior | `runtime.compiler.COMPILER_VERSION` |
| RuntimePlan schema | Provider-neutral output shape | [RUNTIME_PLAN_SCHEMA.json](../../spec/runtime/RUNTIME_PLAN_SCHEMA.json) |
| Evaluation suite/schema | Task, condition, grader, and experiment meaning | [eval runtime schemas](../../evals/runtime/schemas/) |

The v0.4 candidate tree uses distribution and runtime compiler version `0.4.0`
and runtime schemas `1.0.0`. These remain separate version dimensions even when
their numbers coincide. The branch, version field, or compiler version alone
does not prove that a v0.4 tag or package was published.

## Compatibility rules

The current compiler accepts only `TaskResolution.schema_version == "1.0.0"`
with `selection_only == true`. Every active referenced component must exist in
the installed runtime registry at the exact pinned component version. A mismatch
fails closed.

Additive output fields may be tolerated by consumers. Removing a field, changing
its meaning or type, changing canonicalization, or changing channel semantics
requires an appropriate schema/compiler version change.

## What changes which version

Increment the runtime representation schema when the required per-component
shape or field meaning changes. Increment a component version or explicit
runtime-representation revision when its runtime semantics or directive wording
changes. Increment the compiler version when activation, precedence, ordering,
dedupe, budget, rendering, or hashing behavior changes.

Increment an evaluation suite/grader version whenever tasks, expected outputs,
rubrics, condition construction, or scoring changes. Never overwrite the exact
prompts or graders used for published evidence.

## Generated data

Source runtime records compile into
[runtime/runtime_registry.json](../../runtime/runtime_registry.json) and the
installed package copy. Use:

```bash
python scripts/build_runtime_registry.py --check
```

Generated output must be reproducible. Edit the source/generator path rather
than patching only one generated copy.

## Hashes

`task_resolution_hash` covers the complete normalized v0.3 input. The plan
`manifest_hash` covers the complete emitted plan except the hash field itself.
Both use canonical UTF-8 JSON with sorted keys and compact separators.

An execution run manifest adds timestamp, repository commit, harness/registry/
compiler versions, plan identity, endpoint/model identity, generation
parameters, and trial index. Its hash identifies that run manifest, not just the
deterministic plan.

## Reproduction checklist

To compare two plans as equivalent, pin at least:

- exact task resolution bytes/semantic content;
- registry and component versions;
- runtime registry build;
- representation and plan schemas;
- compiler version;
- model profile and directive budget;
- normalized host capabilities;
- base-instruction-presence flag.

For model experiments, also pin adapter code/version, endpoint type, exact model
identifier or digest, generation parameters, suite and grader versions, trial
count, and order seed. See [Evaluation](EVALUATION.md).
