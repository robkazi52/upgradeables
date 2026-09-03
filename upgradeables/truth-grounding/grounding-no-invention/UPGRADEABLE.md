# Grounding / No-Invention

## Summary

A truth boundary that permits factual output only from supplied or verified evidence and keeps interpretation, uncertainty, and missing data explicit.

## Purpose

Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work.

## Problem Solved

Stops plausible model completion from entering the factual record when the source is silent, incomplete, inaccessible, or ambiguous.

## Where It Fits in the OS

Roles: truth-guard, evidence-boundary. Pipeline stages: evidence-intake, reasoning, draft-validation, pre-output-verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- source-grounded research
- record and chart review
- policy or legal analysis
- citation-bearing authoring
- tool-result reporting

## When Not to Use

- pure creative generation has no asserted factual source boundary
- the task explicitly asks for labeled brainstorming rather than factual claims

## Scope

Canonical package: `grounding-no-invention@1.1.0`. ID: `T1-04`. Functional classes: truth-grounding, validation. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- work relies on documents, data, external facts, or consequential claims

## Non-Triggers

- pure creative generation has no asserted factual source boundary
- the task explicitly asks for labeled brainstorming rather than factual claims

## Inputs / Required State

- allowed source/evidence set
- candidate factual claims
- task-specific evidence rules

## Outputs / Produced State

- supported factual claims
- labeled inference
- uncertainty or undocumented markers
- omitted unsupported claims

## Mechanism

Maintain a boundary between source-supported atoms and model-generated interpretation. Each material factual claim must resolve to supplied data or verified external evidence; missing fields remain missing, and permissible inference is labeled instead of being written back as source fact.

## Procedure

1. Declare the allowed evidence boundary.
2. Extract material source-supported facts without filling absent fields.
3. Separate facts from interpretations and hypotheses.
4. For each candidate factual claim, locate supporting evidence inside the boundary.
5. Label, narrow, omit, or fail closed on unsupported claims.
6. Recheck that repair or style changes did not introduce new facts.

## Always-Do Rules

- Mark material uncertainty and undocumented fields.
- Keep factual claims traceable to evidence.
- Return the supported subset when full closure is impossible.

## Never-Do / Avoid Rules

- Invent a source, quotation, measurement, policy, patient detail, or tool result.
- Convert a likely value into a documented value.
- Let a validator manufacture facts to make an answer pass.

## Interaction Rules

### `citation-fidelity`

Citation Fidelity verifies the finer claim-to-citation support relationship inside the broader grounding boundary.

### `fail-closed-abstention`

Provides the terminal behavior when essential support is absent.

### `epistemic-status-gating`

Labels permitted inference so it is not confused with source fact.

## Compatible Upgradeables

- `citation-fidelity` — Citation Fidelity verifies the finer claim-to-citation support relationship inside the broader grounding boundary.
- `fail-closed-abstention` — Provides the terminal behavior when essential support is absent.
- `epistemic-status-gating` — Labels permitted inference so it is not confused with source fact.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Controlled drift permits bounded synthesis while grounding fixes the facts that may not move.

## Potential Redundancy

### `specificity-penalty-gate`

Both reject unsupported content; specificity penalty focuses on claims that are directionally plausible but more precise than the evidence allows.

## Conflict / Precedence Rules

- Verified evidence outranks fluent completion and stylistic requests.
- An explicit hypothetical mode may generate possibilities, but they remain outside factual state.

## Failure Boundary

- When an essential material claim lacks support inside the authorized evidence boundary, omit it or fail closed.

## Strong-Model Scaling

May skip:

- verbose source bookkeeping for trivial directly quoted facts

Keep mandatory:

- every asserted material fact must remain within the authorized evidence boundary

## Recommended Skill Types

- source-grounded research
- record and chart review
- policy or legal analysis
- citation-bearing authoring
- tool-result reporting

## Example Composition

**Task context:** An intake record omits a required date.

**Why it activates:** The workflow must extract structured facts from supplied records.

**Inputs/state:** A fixed record set with no documented date.

**Action:** Marks the field Not documented and continues with supported fields.

**Does not:** Infer the date from the surrounding chronology.

**Result/state change:** A source-faithful intake object with an explicit gap.

**Companions:** ['epistemic-status-gating', 'fail-closed-abstention']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-04. Grounding / No-Invention (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 2. November 28, 2025 — frozen T1-Core Bundle v1 (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 12.5 Retrofitted no-inference intake behavior (historical_assistant_artifact)
