# Bounded ExIt

## Summary

Runs evaluate-and-repair passes only while the next pass has more expected value than cost or risk.

## Purpose

Turn iterative improvement into a terminating control loop with explicit quality, budget, and diminishing-return gates.

## Problem Solved

Revision loops either stop too early with a known high-impact defect or continue polishing low-value details indefinitely.

## Where It Fits in the OS

Roles: refinement controller, reasoning-budget governor. Pipeline stages: draft review, iterative repair, release decision.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- document revision
- code or prompt refinement
- multi-pass synthesis
- quality-controlled drafting

## When Not to Use

- a mandatory validator has not yet passed
- a hard defect requires escalation rather than iteration
- the artifact is already accepted and no new requirement exists

## Scope

Canonical package: `bounded-exit@1.1.0`. ID: `T2-01`. Functional classes: planning-reasoning, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a draft needs iterative improvement

## Non-Triggers

- a mandatory validator has not yet passed
- a hard defect requires escalation rather than iteration
- the artifact is already accepted and no new requirement exists

## Inputs / Required State

- artifact
- locked goals
- quality criteria
- iteration budget
- repair cost estimates

## Outputs / Produced State

- improved artifact
- pass-by-pass defect decisions
- explicit exit reason

## Mechanism

Each pass evaluates the artifact against locked goals, chooses the single highest-value remaining defect, repairs it, and re-evaluates. Exit occurs on threshold satisfaction, budget exhaustion, or diminishing expected improvement; the historical acronym expansion is deliberately left unrecovered.

## Procedure

1. Lock acceptance criteria and a maximum pass or cost budget.
2. Score the current artifact against those criteria.
3. Choose the highest-impact repair that can be completed without reopening accepted decisions.
4. Apply the repair and record whether the target metric improved.
5. Stop when criteria pass, no repair has positive expected value, or the budget is reached; otherwise repeat.

## Always-Do Rules

- define the exit condition before iterating
- repair the highest-value defect first
- re-evaluate after every pass

## Never-Do / Avoid Rules

- iterate merely because another rewrite is possible
- use a quality score to waive a mandatory truth or safety check
- invent an expansion for ExIt

## Interaction Rules

### `micro-repair`

Micro-Repair supplies the smallest correction for the defect selected by the loop.

### `structured-refinement`

Structured Refinement separates defect classes; Bounded ExIt decides whether another class-specific pass is worth doing.

### `parallel-qms`

Parallel-QMS can score candidates or revisions on multiple quality dimensions before the exit decision.

## Compatible Upgradeables

- `micro-repair` — Micro-Repair supplies the smallest correction for the defect selected by the loop.
- `structured-refinement` — Structured Refinement separates defect classes; Bounded ExIt decides whether another class-specific pass is worth doing.
- `parallel-qms` — Parallel-QMS can score candidates or revisions on multiple quality dimensions before the exit decision.

## Counterbalancing Upgradeables

### `reasoning-scale-controller`

The scale controller can increase depth when risk justifies it, while Bounded ExIt prevents that depth from becoming unbounded.

## Potential Redundancy

### `structured-refinement`

Both organize revision, but Structured Refinement orders defect classes and Bounded ExIt owns continuation and termination.

## Conflict / Precedence Rules

- Mandatory acceptance checks outrank a pass budget; if budget expires first, return blocked rather than pass.
- A newly discovered architecture failure hands off to Surgery or Regenerative Rewrite instead of repeating local passes.

## Failure Boundary

- endless recursive polishing
- stopping with a known blocking defect
- changing accepted decisions during a repair pass
- optimizing an easy metric instead of the task

## Strong-Model Scaling

May skip:

- verbose pass logs for a one-pass correction
- formal scoring when the next defect is obvious and low-risk

Keep mandatory:

- predeclared exit rule
- post-repair re-evaluation
- mandatory-gate precedence

## Recommended Skill Types

- analysis and decision support
- document and code transformation
- high-stakes evidence work
- review and quality assurance

## Example Composition

**Task context:** Revise a policy memo before publication.

**Why it activates:** The memo is sound but can absorb an unknown number of polish passes.

**Inputs/state:** Accuracy and required sections pass; one unclear paragraph and several optional style improvements remain; two passes are budgeted.

**Action:** Repairs the unclear paragraph, rechecks the criteria, and exits because the remaining style gain is below its review cost.

**Does not:** Rewrite the whole memo or continue polishing synonyms after acceptance.

**Result/state change:** A publishable memo and an explicit diminishing-return exit.

**Companions:** ['structured-refinement', 'micro-repair']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 9. BOUNDED EXIT — DEEPER HISTORICAL USE (historical_assistant_artifact)
