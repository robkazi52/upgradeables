# Meta-Supervisor Bundle

## Summary

Supervises the health of an active scaffold by collecting process observations and routing bounded repairs for loops and contradictions.

## Purpose

Coordinate Meta-Awareness, Stuck-Pattern Reset, and Contradiction Micro-Repair without becoming the suite-wide mode and architecture authority.

## Problem Solved

Health monitors and repair packs can detect different failures but conflict, duplicate work, or act without a common diagnosis and repair boundary.

## Where It Fits in the OS

Roles: scaffold health orchestrator, diagnostic repair router. Pipeline stages: health intake, failure classification, repair routing, recheck.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- complex iterative scaffolds
- multi-module reasoning
- repeated failures
- runtime process-health supervision

## When Not to Use

- the task needs suite-wide mode declaration and Core-stack governance
- one module can handle an obvious local issue
- no observable process-health signal exists

## Scope

Canonical package: `meta-supervisor@1.1.0`. ID: `T4-01`. Functional classes: meta-control, orchestration, validation. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- complex scaffolding itself needs supervision

## Non-Triggers

- the task needs suite-wide mode declaration and Core-stack governance
- one module can handle an obvious local issue
- no observable process-health signal exists

## Inputs / Required State

- process-health snapshot
- active module and state map
- locked constraints
- repair-pack capabilities
- escalation rules

## Outputs / Produced State

- failure classification
- bounded repair route
- repair ownership
- post-repair health decision

## Mechanism

Collect evidence from Meta-Awareness, classify it as loop/stale path, localized contradiction, broader state instability, or unverifiable, and activate only the smallest matching repair pack. Preserve locked state, serialize repair ownership so packs do not race, then re-observe the affected process. Meta-Supervisor manages health diagnosis and repair; Ultimate Suite Supervisor remains responsible for global modes, stack enforcement, edit-class selection, and suite conflicts.

## Procedure

1. Request or read an evidence-bearing process-health snapshot.
2. Classify the failure and identify the smallest responsible state or reasoning region.
3. Select no action, Stuck-Pattern Reset, Contradiction Micro-Repair, or escalation to Meta-Stability or suite supervision.
4. Lock facts, constraints, and unaffected modules; assign one repair owner.
5. Run the bounded repair and request a fresh health observation.
6. Close on pass, repeat only with new evidence, or escalate when the failure crosses the scaffold boundary.

## Always-Do Rules

- route from observable diagnosis
- choose the smallest repair pack
- preserve locked state
- recheck after repair
- escalate suite-wide conflicts

## Never-Do / Avoid Rules

- declare global operating modes
- rewrite architecture under a health-repair pretext
- run competing repair packs on the same region
- anthropomorphize process failures

## Interaction Rules

### `meta-awareness`

Meta-Awareness supplies observable health status and evidence.

### `stuck-pattern-reset`

Reset handles repeated failed reasoning paths selected by the supervisor.

### `contradiction-micro-repair`

Contradiction repair handles localized incompatible claims.

### `ultimate-suite-supervisor`

Ultimate Suite receives mode, Core-stack, duration, and cross-pack authority conflicts beyond health routing.

## Compatible Upgradeables

- `meta-awareness` — Meta-Awareness supplies observable health status and evidence.
- `stuck-pattern-reset` — Reset handles repeated failed reasoning paths selected by the supervisor.
- `contradiction-micro-repair` — Contradiction repair handles localized incompatible claims.
- `ultimate-suite-supervisor` — Ultimate Suite receives mode, Core-stack, duration, and cross-pack authority conflicts beyond health routing.

## Counterbalancing Upgradeables

### `reasoning-throughput-governor`

Throughput prevents supervision and repair checks from consuming the entire work budget.

## Potential Redundancy

### `ultimate-suite-supervisor`

Meta-Supervisor is the health-and-repair bundle; Ultimate Suite is the top-level operating authority across modes, stacks, editing classes, and final health.

## Conflict / Precedence Rules

- Suite-wide mode or authority conflicts escalate to Ultimate Suite Supervisor.
- One repair owner controls a failed region at a time.
- An unverifiable health signal cannot authorize mutation.
- Locked truth and safety constraints survive every routed repair.

## Failure Boundary

- supervisor recursion
- repair-pack races
- suite-authority overreach
- mutation from unverifiable diagnosis
- health checks without termination

## Strong-Model Scaling

May skip:

- formal routing when one obvious repair pack is already explicitly requested

Keep mandatory:

- diagnosis-before-repair
- smallest-pack selection
- locked-state preservation
- post-repair observation

## Recommended Skill Types

- complex iterative scaffolds
- multi-module reasoning
- repeated failures
- runtime process-health supervision

## Example Composition

**Task context:** A planner repeats the same rejected deployment approach and also contains one inconsistent date.

**Why it activates:** Two distinct health defects require ordered bounded repairs.

**Inputs/state:** The repeated path, rejection reason, date sources, and locked plan constraints are visible.

**Action:** Routes the loop to Stuck-Pattern Reset, rechecks progress, then routes the local date conflict to Contradiction Micro-Repair without changing the global mode.

**Does not:** Activate every pack or redesign the deployment architecture.

**Result/state change:** Scoped repairs coordinated under one health supervisor.

**Companions:** ['meta-awareness', 'stuck-pattern-reset', 'contradiction-micro-repair']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T4-01. Meta-Supervisor Bundle (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
