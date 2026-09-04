# RuntimePlan

`RuntimePlan` is the provider-neutral interface between task selection and a
host adapter. It is produced by the deterministic compiler and validated
against [RUNTIME_PLAN_SCHEMA.json](../../spec/runtime/RUNTIME_PLAN_SCHEMA.json).
Adapters consume the plan; they do not redo v0.3 classification or component
selection.

## Channel model

| Field | Meaning | Default host treatment |
| --- | --- | --- |
| `instruction_capsule` | Managed execution directives and mandatory invariants | Return separately; compose only with explicit host policy |
| `state_contract` | Structured state obligations | Native state, or an explicit documented fallback |
| `validators` | Required checks | Deterministic validator or host guardrail where possible |
| `orchestration` | Scheduling, handoff, or workflow controls | Host orchestration only |
| `tool_requirements` | Required capability plus availability result | Preflight before execution |
| `output_contract` | Output constraints | Native structured output where supported |
| `warnings` | Missing capability and budget limitations | Show to the host/operator, not the model |

Only `instruction_capsule` is ready for an instruction channel. Folding other
channels into prose is a lossy adapter decision and must be explicit.

## Identity and provenance fields

- `schema_version`: runtime-plan wire schema, currently `1.0.0`.
- `compiler_version`: compiler behavior version.
- `task_resolution_hash`: canonical SHA-256 hash of the complete v0.3 input.
- `model_profile`: requested generic instruction-density profile.
- `host`: normalized host capabilities used during compilation.
- `base_instructions_present`: whether the caller reported existing host
  instructions.
- `manifest_hash`: canonical SHA-256 hash of the complete plan with this field
  omitted.

Hashes use UTF-8 JSON with sorted keys, compact separators, and non-ASCII text
preserved. They establish artifact identity, not anonymity or authenticity.

## Components and exclusions

Each `components` item records:

- component `slug` and pinned `version`;
- chosen `runtime_level` and `runtime_form`;
- activation `source_group`;
- whether it was structurally required;
- v0.3 selection reasons;
- source package path.

Directive bodies and internal dedupe metadata are not repeated in this list;
the rendered result is in `instruction_capsule`, and the transformations are in
`decisions`.

`excluded_runtime_components` records active selections intentionally removed
from runtime execution, such as a meta/builder package or an editing control
suppressed by review-only authority.

## Decisions

`decisions` is an ordered audit trail. Current decision types include:

- `dependency`: added a declared runtime dependency;
- `runtime-form`: excluded a non-runtime-injectable component;
- `precedence`: applied an authority rule such as review-only suppression;
- `capability`: identified an unavailable required host capability;
- `dedupe`: suppressed a duplicate directive while retaining invariants;
- `budget`: lowered a component level or removed an optional directive.

Decision objects are intentionally descriptive and may gain additive fields.
Consumers should branch on `type` and tolerate fields they do not use.

## Token estimate

`token_estimate` is currently `ceil(character_count / 4)` for the instruction
capsule. `token_estimate_approximate` is always `true`. This is a portable budget
heuristic, not provider billing or tokenizer output.

When the minimum required capsule exceeds the requested budget, the current
compiler preserves the required content and adds a warning. Callers that require
a hard size limit must treat that warning as a preflight failure.

## Example shape

```json
{
  "schema_version": "1.0.0",
  "compiler_version": "0.4.0",
  "task_resolution_hash": "sha256:...",
  "model_profile": "strong",
  "instruction_capsule": "<upgradeables-runtime version=\"0.4.0\">...",
  "state_contract": [],
  "validators": [],
  "orchestration": [],
  "tool_requirements": [],
  "output_contract": [],
  "components": [],
  "excluded_runtime_components": [],
  "warnings": [],
  "token_estimate": 83,
  "token_estimate_approximate": true,
  "decisions": [],
  "manifest_hash": "sha256:..."
}
```

The actual plan also includes normalized `host` and
`base_instructions_present` fields emitted by the current implementation.

## Runtime plan versus run manifest

The plan is deterministic for identical inputs and installed runtime data. A
run manifest is execution evidence and includes time, model, endpoint, generation
settings, trial index, and repository commit; it is therefore not deterministic.
See [Versioning](VERSIONING.md) and [Evaluation](EVALUATION.md).
