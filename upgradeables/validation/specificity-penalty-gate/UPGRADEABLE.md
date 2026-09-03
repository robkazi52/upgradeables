# Specificity Penalty Gate

## Summary

A provisional gate that penalizes unsupported precision when an answer is more specific than its evidence, task need, or epistemic state permits.

## Purpose

Provide a conservative modern interpretation of the recovered name while keeping the historical source gap explicit.

## Problem Solved

Models often replace uncertainty with exact dates, quantities, identities, causes, or implementation details that sound useful but are not supported.

## Where It Fits in the OS

Roles: provisional-overprecision-gate, evidence-resolution-matcher. Pipeline stages: drafting, claim validation, pre-release.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- research answers
- estimates
- incident explanations
- requirements derived from incomplete evidence
- source recovery

## When Not to Use

- exact values are directly provided and verified
- a formal specification requires exactness and the evidence supports it
- the user needs the unrecovered historical mechanism

## Scope

Canonical package: `specificity-penalty-gate@1.1.0`. ID: `JAN26-15`. Functional classes: validation, truth-grounding. Activation: `U2-specialized`. Mechanism basis: `modern-interpretation`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- precise details may be plausible but unsupported

## Non-Triggers

- exact values are directly provided and verified
- a formal specification requires exactness and the evidence supports it
- the user needs the unrecovered historical mechanism

## Inputs / Required State

- draft claims
- evidence and its resolution
- epistemic labels
- task precision requirement

## Outputs / Produced State

- overprecision flags
- support-to-specificity map
- generalized or qualified claims
- source-gap notice

## Mechanism

Tag specificity-bearing atoms—numbers, dates, named causes, unique identities, fine-grained scope, and certainty language—and compare each with the resolution of available evidence and actual task need. Unsupported precision receives a penalty that forces one of four actions: cite stronger evidence, widen to a supported range or class, label the detail provisional, or remove it. This scoring/gating procedure is not claimed as historical reconstruction.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify all atoms whose precision materially narrows the claim.
2. Record the evidence resolution and confidence for each atom.
3. Ask whether the task outcome requires that degree of precision.
4. Flag atoms more precise than evidence or need.
5. Resolve each flag by stronger evidence, supported generalization, explicit provisional labeling, or removal.
6. Recheck that generalization has not erased a decision-critical distinction.

## Always-Do Rules

- Penalize precision mismatch rather than detail itself.
- Preserve verified exact values when decision-relevant.
- Label the mechanism and thresholds as modern interpretation.

## Never-Do / Avoid Rules

- Replace an unsupported exact number with a different guessed range.
- Make all writing vague by default.
- Attribute penalty weights or thresholds to unrecovered history.

## Interaction Rules

### `grounding-no-invention`

Removes details that have no supporting evidence.

### `epistemic-status-gating`

Supplies confidence and fact/inference/hypothesis labels.

### `citation-fidelity`

Tests whether a citation supports the claimed degree of precision.

## Compatible Upgradeables

- `grounding-no-invention` — Removes details that have no supporting evidence.
- `epistemic-status-gating` — Supplies confidence and fact/inference/hypothesis labels.
- `citation-fidelity` — Tests whether a citation supports the claimed degree of precision.

## Counterbalancing Upgradeables

### `critical-atomic-verification`

Protects exact details that are both supported and essential rather than generalizing them away.

## Potential Redundancy

### `grounding-no-invention`

Grounding rejects unsupported facts; this provisional gate specifically compares claim resolution to evidence resolution and task need.

## Conflict / Precedence Rules

- A verified decision-critical exact atom is not penalized merely for being specific.
- When evidence supports only a bound or category, that weaker form outranks a fluent point estimate.
- Safety-relevant uncertainty must remain visible.

## Failure Boundary

- Do not release a material exact claim when the available evidence supports only a broader range, class, or uncertainty state.

## Strong-Model Scaling

May skip:

- formal scoring when all specificity atoms are direct user-provided constants

Keep mandatory:

- support-versus-resolution comparison for generated dates, numbers, causes, and identities

## Recommended Skill Types

- high-stakes evidence work
- review and quality assurance
- source-grounded research

## Example Composition

**Task context:** A model infers that a regression began at exactly 14:32 because logs show the first observed error then.

**Why it activates:** Observation time does not establish exact onset time or cause.

**Inputs/state:** Sparse logs, deploy timeline, and incident question.

**Action:** Changes the claim to 'observed by 14:32' and keeps the causal explanation provisional.

**Does not:** Invent a 14:31–14:32 onset interval or delete the verified timestamp.

**Result/state change:** The response retains useful evidence while removing unsupported temporal and causal precision.

**Companions:** ['grounding-no-invention', 'epistemic-status-gating', 'citation-fidelity']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-15` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `modern-interpretation`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 15. January 2026 registry philosophy recovered from historical work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 20. RECOVERY GAPS AFTER DEEP PASS 2.0 (historical_assistant_artifact)
