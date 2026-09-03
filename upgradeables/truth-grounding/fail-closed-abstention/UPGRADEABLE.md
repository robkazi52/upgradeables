# Fail-Closed Abstention

## Summary

A terminal disposition rule that narrows or withholds a conclusion when a required truth, evidence, or integrity gate remains unsatisfied.

## Purpose

Ensure that missing essential support produces an explicit bounded result rather than fabricated closure.

## Problem Solved

Prevents a workflow from converting uncertainty, validator disagreement, or absent evidence into a confident final answer.

## Where It Fits in the OS

Roles: commit-gate, abstention-controller. Pipeline stages: post-validation, pre-output-commitment.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- medical, legal, or policy analysis
- citation-bearing research
- safety-critical decisions
- source transcription and fidelity work

## When Not to Use

- the failed condition is optional and does not affect the supported deliverable
- a harmless creative task has no factual commitment gate

## Scope

Canonical package: `fail-closed-abstention@1.1.0`. ID: `T3-11`. Functional classes: truth-grounding, validation, output. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- required evidence cannot be verified

## Non-Triggers

- the failed condition is optional and does not affect the supported deliverable
- a harmless creative task has no factual commitment gate

## Inputs / Required State

- candidate conclusion
- required gate list
- validator outcomes
- supported claim subset

## Outputs / Produced State

- committed supported subset
- narrowed conclusion
- abstention with unresolved dependency

## Mechanism

Consume explicit validator outcomes and distinguish essential from optional failures. If an essential condition is failed or unverifiable, block the affected conclusion, preserve any independently supported subset, and state the unresolved dependency; never synthesize a missing fact merely to obtain a pass.

## Procedure

1. List the conditions required to commit the conclusion.
2. Read each condition's pass, fail, or unverifiable result.
3. Determine which failures invalidate only one claim and which invalidate the whole conclusion.
4. Remove or narrow invalidated claims while preserving independently supported content.
5. Return the supported subset plus the unresolved dependency or an explicit abstention.

## Always-Do Rules

- Tie abstention scope to the failed requirement.
- Return supported partial results when safe and useful.
- Name the blocking dependency concisely.

## Never-Do / Avoid Rules

- Invent evidence to clear a gate.
- Turn every minor uncertainty into total refusal.
- Hide the fact that a required gate failed.

## Interaction Rules

### `grounding-no-invention`

Supplies unsupported-claim failures that may require abstention.

### `fermionic-veto`

The veto raises a non-overridable block; fail-closed abstention determines the safe output after that block.

### `parallel-qms`

Persistent crucial disagreement from QMS becomes an abstain, rework, or uncertainty disposition.

## Compatible Upgradeables

- `grounding-no-invention` — Supplies unsupported-claim failures that may require abstention.
- `fermionic-veto` — The veto raises a non-overridable block; fail-closed abstention determines the safe output after that block.
- `parallel-qms` — Persistent crucial disagreement from QMS becomes an abstain, rework, or uncertainty disposition.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `fermionic-veto`

Veto detects and asserts a blocking condition; fail-closed abstention specifies how output is narrowed or withheld after the block.

## Conflict / Precedence Rules

- A request for a definitive answer cannot override a failed required truth gate.
- Preserve supported content unless higher authority requires withholding the entire output.

## Failure Boundary

- A conclusion cannot be committed while any indispensable evidence or integrity condition remains failed or unverifiable.

## Strong-Model Scaling

May skip:

- verbose explanation of nonmaterial optional failures

Keep mandatory:

- no essential failed gate may be bypassed by fluency or confidence

## Recommended Skill Types

- medical, legal, or policy analysis
- citation-bearing research
- safety-critical decisions
- source transcription and fidelity work

## Example Composition

**Task context:** A medical evidence summary has strong support for background facts but lacks the study result required for the final recommendation.

**Why it activates:** A required decision anchor is missing.

**Inputs/state:** Passed background checks and an unverifiable decision-critical result.

**Action:** Returns the supported background and abstains from the recommendation while naming the missing result.

**Does not:** Infer the result from adjacent evidence.

**Result/state change:** A useful bounded summary without unsupported closure.

**Companions:** ['grounding-no-invention', 'fermionic-veto']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-11` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Fail-Closed Tier-3 Abstention.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-11. Fail-Closed Tier-3 Abstention (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.12 Historical global collapse rule (historical_assistant_artifact)
