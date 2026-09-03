# Dynamic Depth Allocation

## Summary

Redistributes a fixed or governed reasoning budget so difficult, uncertain, or consequential regions receive deeper work than routine regions.

## Purpose

Concentrate analysis and verification where local marginal value is highest instead of applying uniform depth across a task.

## Problem Solved

Uniform review wastes effort on obvious units and leaves bottlenecks, uncertain claims, or high-risk boundaries underexamined.

## Where It Fits in the OS

Roles: within-task depth allocator, hotspot router. Pipeline stages: task decomposition, regional scoring, depth routing, reallocation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- heterogeneous documents
- mixed-risk code changes
- large research corpora
- multi-stage plans with uneven uncertainty

## When Not to Use

- every unit has the same mandated review depth
- the task is one atomic operation
- regional scores cannot be observed or estimated

## Scope

Canonical package: `dynamic-depth-allocation@1.1.0`. ID: `T4-12`. Functional classes: meta-control, planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- task regions vary in difficulty or risk

## Non-Triggers

- every unit has the same mandated review depth
- the task is one atomic operation
- regional scores cannot be observed or estimated

## Inputs / Required State

- task regions
- global reasoning envelope
- regional uncertainty and consequence
- dependency map
- mandatory depth floors

## Outputs / Produced State

- regional depth map
- method and check assignment
- reallocation log
- coverage or budget blocker

## Mechanism

Partition the task into meaningful regions, score each on difficulty, uncertainty, consequence, dependency centrality, and current evidence deficit, and assign depth bands under the Cognitive Governor's total envelope. Re-score after discoveries and move effort toward unresolved hotspots while maintaining a minimum pass everywhere. DDA decides where depth goes, not the total budget or execution concurrency.

## Procedure

1. Decompose the task into independently inspectable regions or claims.
2. Score each region for uncertainty, consequence, coupling, novelty, and evidence deficit.
3. Reserve a minimum validation pass for all regions.
4. Allocate the remaining governed budget to high-score regions and choose appropriate methods for each.
5. Re-score when a local finding changes dependencies or risk.
6. Stop reallocating when all mandatory regional thresholds pass or escalate if the global budget is insufficient.

## Always-Do Rules

- maintain a minimum pass everywhere
- use explicit hotspot signals
- reallocate when evidence changes the map
- stay within or explicitly renegotiate the global budget

## Never-Do / Avoid Rules

- equate length with difficulty
- starve low-score regions of mandatory checks
- hide budget overruns as local depth
- confuse more parallel workers with deeper reasoning

## Interaction Rules

### `cognitive-governor`

The governor supplies the total envelope that DDA redistributes.

### `risk-tier-scaling`

Risk tiers set mandatory regional floors.

### `reasoning-throughput-governor`

Throughput schedules regional work at an efficient rate after depth is assigned.

## Compatible Upgradeables

- `cognitive-governor` — The governor supplies the total envelope that DDA redistributes.
- `risk-tier-scaling` — Risk tiers set mandatory regional floors.
- `reasoning-throughput-governor` — Throughput schedules regional work at an efficient rate after depth is assigned.

## Counterbalancing Upgradeables

### `meta-awareness`

Meta-Awareness detects whether depth allocation itself is causing neglect, loops, or module conflict.

## Potential Redundancy

### `cognitive-governor`

Governor determines total effort; DDA determines local concentration.

### `reasoning-throughput-governor`

Throughput chooses pace and breadth; DDA chooses analytical depth per region.

## Conflict / Precedence Rules

- A high-risk mandatory check receives its floor even if its estimated uncertainty is low.
- When every region exceeds the available envelope, escalate the budget or narrow scope rather than fabricate coverage.
- Reallocation cannot erase already discovered unresolved defects.

## Failure Boundary

- uniform-depth default
- hotspot tunnel vision
- mandatory-check starvation
- constant reallocation thrash
- depth confused with concurrency

## Strong-Model Scaling

May skip:

- printing numeric scores when relative depth is obvious
- multiple bands for a small task

Keep mandatory:

- minimum regional pass
- hotspot-driven allocation
- budget-bound re-scoring

## Recommended Skill Types

- heterogeneous documents
- mixed-risk code changes
- large research corpora
- multi-stage plans with uneven uncertainty

## Example Composition

**Task context:** Review a migration plan with 40 routine steps and three irreversible cutovers.

**Why it activates:** The plan's risk and uncertainty are sharply uneven.

**Inputs/state:** A fixed review envelope, dependency graph, rollback data, and cutover owners exist.

**Action:** Runs a baseline check on all steps, assigns deep failure and rollback analysis to the three cutovers, and reallocates when one exposes a shared dependency.

**Does not:** Spend equal time on renaming a label and switching production data.

**Result/state change:** Depth concentrated on consequential bottlenecks without losing baseline coverage.

**Companions:** ['cognitive-governor', 'risk-tier-scaling']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-12` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: DDA.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T4-12. Dynamic Depth Allocation (DDA) (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.2 QMS-RTS — Risk-Tier-Split QMS (historical_assistant_artifact)
