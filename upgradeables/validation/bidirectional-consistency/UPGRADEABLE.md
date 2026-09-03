# Bidirectional Consistency

## Summary

Validates a mapping in both directions so a plausible forward result must also reconstruct or imply its originating conditions.

## Purpose

Expose lossy, non-invertible, or spuriously plausible transformations that one-way review misses.

## Problem Solved

A result can look correct from input to output while the output cannot support the claims, constraints, or provenance attributed to it.

## Where It Fits in the OS

Roles: transformation-validator, reverse-entailment-check. Pipeline stages: post-transformation, pre-release-validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- requirements-to-implementation checks
- summary-to-source checks
- schema migrations
- plan-to-objective traceability

## When Not to Use

- the transformation is intentionally irreversible and no reverse contract is claimed
- creative output has no declared source mapping

## Scope

Canonical package: `bidirectional-consistency@1.1.0`. ID: `T2-18`. Functional classes: validation, planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- causal, logical, quantitative, or evidence claims are central

## Non-Triggers

- the transformation is intentionally irreversible and no reverse contract is claimed
- creative output has no declared source mapping

## Inputs / Required State

- source atoms
- transformed result
- transformation contract
- permitted loss or abstraction

## Outputs / Produced State

- forward coverage map
- reverse reconstruction
- directional mismatch list
- pass/repair decision

## Mechanism

Run a forward check from source conditions to proposed result, then independently read the result backward to enumerate which source conditions it actually entails. Compare the reconstructed set with the locked source atoms; missing, invented, or many-to-one-collapsed atoms fail even when the forward narrative is fluent.

## Procedure

1. Lock the source atoms and declared transformation contract.
2. Verify that each source atom has a forward image in the result.
3. Hide the source and reconstruct its implied atoms from the result alone.
4. Compare reconstructed atoms with the locked set.
5. Classify omissions, inventions, and ambiguity introduced by the mapping.
6. Repair and repeat both directions.

## Always-Do Rules

- Keep forward and reverse judgments separately inspectable.
- Test material constraints, not merely wording overlap.

## Never-Do / Avoid Rules

- Infer reverse consistency from a passing forward check.
- Demand literal reversibility when the contract permits labeled compression.

## Interaction Rules

### `critical-atomic-verification`

Supplies atom-level units for the two directional passes.

### `citation-fidelity`

Provides evidence bindings that can be traced from source to claim and reconstructed from claim to source.

## Compatible Upgradeables

- `critical-atomic-verification` — Supplies atom-level units for the two directional passes.
- `citation-fidelity` — Provides evidence bindings that can be traced from source to claim and reconstructed from claim to source.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Prevents the reverse check from treating permitted abstraction as a defect.

## Potential Redundancy

### `multi-layer-consistency`

Multi-layer checks agreement across scales; bidirectional consistency checks the directionality of one transformation.

## Conflict / Precedence Rules

- The declared transformation contract determines which information may be lost.
- A reverse contradiction on a locked atom overrides stylistic forward plausibility.

## Failure Boundary

- Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition.

## Strong-Model Scaling

May skip:

- literal reverse paraphrase for trivial identity transformations

Keep mandatory:

- independent backward reconstruction for lossy or high-stakes transformations

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- review and quality assurance
- source-grounded research

## Example Composition

**Task context:** A pull-request implementation claims to satisfy six acceptance criteria.

**Why it activates:** The code-to-requirement story may be plausible without every criterion actually being entailed.

**Inputs/state:** Six locked criteria, changed code, and allowed implementation freedom.

**Action:** Maps criteria to behavior, then reconstructs satisfied criteria from observed behavior alone.

**Does not:** Count a criterion as satisfied because the PR description repeats it.

**Result/state change:** One missing error-handling criterion is found despite a plausible forward explanation.

**Companions:** ['critical-atomic-verification', 'citation-fidelity']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-18` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Interpretation rule for the frozen T2 registry (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.6 Global verification (historical_assistant_artifact)
