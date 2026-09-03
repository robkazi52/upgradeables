# Fermionic Veto Strengthening

## Summary

A hard exclusion rule under which one decisive contradiction, unsafe state, or impossible coexistence blocks an otherwise high-scoring candidate.

## Purpose

Preserve non-compensable constraints during aggregation and synthesis.

## Problem Solved

Weighted scores and majority agreement can conceal a fatal defect by averaging it with many positive attributes.

## Where It Fits in the OS

Roles: non-compensable-veto, hard-constraint-enforcer. Pipeline stages: candidate evaluation, QMS collapse, pre-action safety gate.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- safety reviews
- constraint-heavy planning
- security decisions
- branch collapse
- truth-conflict resolution

## When Not to Use

- the alleged defect is merely a soft preference
- the veto predicate cannot be defined or evidenced

## Scope

Canonical package: `fermionic-veto@1.1.0`. ID: `T3-09`. Functional classes: validation, meta-control. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a defined critical condition must have veto authority

## Non-Triggers

- the alleged defect is merely a soft preference
- the veto predicate cannot be defined or evidenced

## Inputs / Required State

- candidate
- declared veto predicates
- evidence
- aggregate evaluation

## Outputs / Produced State

- veto/clear status
- predicate evidence record
- repair requirement
- quarantine decision

## Mechanism

Declare a narrow set of exclusion predicates before scoring. Evaluate them independently of aggregate quality; if any predicate is evidenced, quarantine the candidate and require removal of the disqualifying state plus revalidation. The fermionic metaphor is operational only: incompatible states do not share the certified result, and the veto is never diluted by votes or averages.

## Procedure

1. Define non-compensable predicates and required evidence.
2. Run veto checks independently from quality scoring.
3. Record the exact predicate, evidence, and affected candidate.
4. Exclude or quarantine any triggered candidate.
5. Permit repair only if the disqualifying state is removed rather than relabeled.
6. Rerun the veto check before reconsidering certification.

## Always-Do Rules

- Keep veto predicates narrow and inspectable.
- Preserve minority evidence of a decisive defect.
- Require proof of removal before clearing a veto.

## Never-Do / Avoid Rules

- Average a triggered veto into a composite score.
- Use the metaphor as a scientific claim.
- Turn aesthetic disagreement into a hard veto.

## Interaction Rules

### `fail-closed-abstention`

Defines the safe response when a veto cannot be repaired or resolved.

### `parallel-qms`

Preserves hard failures during global validator collapse.

### `cross-universe-consistency`

Blocks branch hybrids with impossible coexisting assumptions.

## Compatible Upgradeables

- `fail-closed-abstention` — Defines the safe response when a veto cannot be repaired or resolved.
- `parallel-qms` — Preserves hard failures during global validator collapse.
- `cross-universe-consistency` — Blocks branch hybrids with impossible coexisting assumptions.

## Counterbalancing Upgradeables

### `multi-truth-gating`

Tests whether an apparent truth contradiction can be resolved before permanent exclusion.

## Potential Redundancy

### `fail-closed-abstention`

Fermionic Veto detects non-compensable exclusion; Fail-Closed determines action under unresolved safety.

## Conflict / Precedence Rules

- Verified veto evidence outranks aggregate score or validator majority.
- If veto evidence conflicts, quarantine pending targeted adjudication rather than silently clearing it.

## Failure Boundary

- Do not certify or execute a candidate while a verified non-compensable predicate remains active.

## Strong-Model Scaling

May skip:

- veto layer for consequence-free creative alternatives

Keep mandatory:

- independent hard-constraint check whenever aggregate scoring is used

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- multi-step task execution
- review and quality assurance

## Example Composition

**Task context:** Five validators score a deployment highly, but one finds that rollback is impossible under the stated safety policy.

**Why it activates:** Rollback capability is a declared non-compensable condition.

**Inputs/state:** Validator reports, policy predicate, and deployment plan.

**Action:** Vetoes deployment and requires a tested rollback path before rescoring.

**Does not:** Approve because four of five validators passed.

**Result/state change:** The candidate remains quarantined until the fatal condition is removed.

**Companions:** ['fail-closed-abstention', 'parallel-qms', 'multi-truth-gating']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-09` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.4 Variables / Criteria / MCDM (historical_assistant_artifact)
