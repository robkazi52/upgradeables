# Reasoning Budget / Cognitive Governor

## Summary

Sets the total reasoning budget and continuation policy from task complexity, risk, and expected value.

## Purpose

Prevent both expensive overthinking of trivial work and unsafe underchecking of consequential work.

## Problem Solved

Without a governor, reasoning effort follows habit or artifact size instead of the value and consequence of additional analysis.

## Where It Fits in the OS

Roles: global reasoning-budget controller, continuation governor. Pipeline stages: task triage, budget assignment, mid-run budget review, exit decision.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- mixed-risk queues
- bounded research
- iterative authoring
- cost-sensitive agent workflows

## When Not to Use

- a mandatory protocol fixes the review budget
- the task is a trivial deterministic transformation
- budget estimation would cost more than execution

## Scope

Canonical package: `cognitive-governor@1.1.0`. ID: `T3-17`. Functional classes: meta-control, planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- effort allocation materially affects cost or quality

## Non-Triggers

- a mandatory protocol fixes the review budget
- the task is a trivial deterministic transformation
- budget estimation would cost more than execution

## Inputs / Required State

- task complexity
- uncertainty
- risk and irreversibility
- cost and latency constraints
- mandatory validation floor

## Outputs / Produced State

- total reasoning envelope
- phase budgets
- budget adjustments
- continue, exit, or blocked decision

## Mechanism

Estimate a total effort envelope from complexity, uncertainty, consequence, irreversibility, and the expected value of another check. Allocate caps for planning, execution, and validation, reserve extra capacity for high-risk unknowns, and periodically compare remaining defect or uncertainty value with remaining cost. The governor owns how much total reasoning is justified; it does not choose which regions receive that effort or how much work flows concurrently.

## Procedure

1. Classify task complexity, uncertainty, consequence, and reversibility.
2. Set an effort envelope and mandatory validation floor.
3. Divide the envelope among planning, execution, verification, and contingency.
4. Track evidence gained, defects removed, and budget consumed at milestones.
5. Increase the envelope only when newly exposed risk has positive expected value; otherwise invoke the exit rule.
6. Report blocked rather than declare completion if mandatory checks exceed the available budget.

## Always-Do Rules

- preserve a validation floor
- tie budget changes to risk or expected value
- distinguish optional polish from required verification
- make exit or escalation explicit

## Never-Do / Avoid Rules

- spend the whole budget on planning
- use cost pressure to waive a hard check
- treat a longer artifact as automatically higher risk
- micromanage per-region depth when Dynamic Depth owns that allocation

## Interaction Rules

### `dynamic-depth-allocation`

Dynamic Depth distributes the governor's total envelope among unequal task regions.

### `reasoning-throughput-governor`

Throughput controls the rate and breadth of work performed under the envelope.

### `risk-tier-scaling`

Risk Tier sets the mandatory verification floor that the budget must fund.

## Compatible Upgradeables

- `dynamic-depth-allocation` — Dynamic Depth distributes the governor's total envelope among unequal task regions.
- `reasoning-throughput-governor` — Throughput controls the rate and breadth of work performed under the envelope.
- `risk-tier-scaling` — Risk Tier sets the mandatory verification floor that the budget must fund.

## Counterbalancing Upgradeables

### `bounded-exit`

Bounded ExIt operationalizes the stop decision when marginal improvement falls below cost.

## Potential Redundancy

### `dynamic-depth-allocation`

Both concern effort, but Cognitive Governor chooses total budget and stop policy; Dynamic Depth redistributes it locally.

### `reasoning-throughput-governor`

Throughput tunes execution pace and concurrency, not total justified effort.

## Conflict / Precedence Rules

- Risk-mandated validation overrides a lower convenience budget.
- If the envelope cannot cover hard checks, return an explicit resource or evidence blocker.
- A local region may receive extra depth only by reallocation or justified budget expansion.

## Failure Boundary

- over-polishing
- premature exit
- validation starvation
- unbounded budget expansion
- confusing global budget with local depth

## Strong-Model Scaling

May skip:

- visible token accounting for a simple task
- formal phase budgets when one pass is clearly sufficient

Keep mandatory:

- risk-based validation floor
- marginal-value review
- explicit stop or escalation

## Recommended Skill Types

- mixed-risk queues
- bounded research
- iterative authoring
- cost-sensitive agent workflows

## Example Composition

**Task context:** Review 200 generated package descriptions before release.

**Why it activates:** Complete line-by-line deep review is expensive, but schema and source accuracy are mandatory.

**Inputs/state:** Automated validators, risk categories, and a fixed review window exist.

**Action:** Funds full schema validation, deeper review for source-gap and high-risk packages, sampled review for routine packages, and stops optional polishing when marginal value falls.

**Does not:** Give every package equal manual time or skip required provenance checks to meet the clock.

**Result/state change:** A risk-funded review plan with a defensible completion boundary.

**Companions:** ['dynamic-depth-allocation', 'risk-tier-scaling', 'bounded-exit']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-17` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-17. Reasoning Budget / Cognitive Governor (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 9. BOUNDED EXIT — DEEPER HISTORICAL USE (historical_assistant_artifact)
