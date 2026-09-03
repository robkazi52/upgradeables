# Drift Suppression

## Summary

Detect deviation from locked task meaning or allowed corridors, diagnose its source, and restore the work to the last validated state.

## Purpose

Keep execution aligned after distracting context, repeated transformation, or model error.

## Problem Solved

Goals, claims, terminology, and constraints can shift gradually without an obvious single failure point.

## Where It Fits in the OS

Roles: drift detection, semantic correction, recovery control. Pipeline stages: before action, after transformation, at checkpoints, final acceptance.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long agent workflows
- high-fidelity editing
- multi-stage synthesis
- policy-bound generation

## When Not to Use

- no semantic baseline or allowed corridor exists
- creative divergence is the explicit objective
- the checker would use the same unsupported summary as the generator

## Scope

Canonical package: `drift-suppression@1.1.0`. ID: `T1-02`. Functional classes: drift-control, validation. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- long, branching, or iterative work

## Non-Triggers

- no semantic baseline or allowed corridor exists
- creative divergence is the explicit objective
- the checker would use the same unsupported summary as the generator

## Inputs / Required State

- locked task and state anchors
- authoritative sources
- corridor map
- current artifact
- last validated version

## Outputs / Produced State

- drift classification
- minimal repair or rollback
- tightened control
- drift incident record

## Mechanism

Compare current plan, state, or artifact against locked task fields, authoritative source anchors, and region-specific corridor tests. Classify each deviation as authorized change, benign variation, or drift; for drift, restore the smallest affected region from the last validated state, reapply the transform under tighter constraints, and record the cause so recurrence can be prevented.

## Procedure

1. Establish baseline anchors and permitted drift corridors before substantive transformation.
2. Run checks at risk-based checkpoints and after context transitions.
3. Compare objective, entities, claims, quantities, obligations, uncertainty, and required structure.
4. Classify discrepancies using authority and corridor rules.
5. Rollback the smallest affected region, tighten the relevant control, and regenerate or request review.
6. Validate the repaired result and record the drift signature.

## Always-Do Rules

- compare to authoritative baselines
- distinguish authorized change from drift
- repair minimally
- record recurring drift signatures

## Never-Do / Avoid Rules

- declare drift from stylistic difference alone
- correct toward a stale summary
- silently accept a failed invariant
- rewrite unaffected regions during repair

## Interaction Rules

### `task-set-lock-in`

Provides objective and acceptance anchors.

### `controlled-drift-corridors`

Defines which deviations are actually outside bounds.

### `zero-drift-zones`

Supplies immutable items requiring exact or equivalence checks.

## Compatible Upgradeables

- `task-set-lock-in` — Provides objective and acceptance anchors.
- `controlled-drift-corridors` — Defines which deviations are actually outside bounds.
- `zero-drift-zones` — Supplies immutable items requiring exact or equivalence checks.

## Counterbalancing Upgradeables

### `drift-sink-scaffold`

Quarantines recurring stale branches identified as drift causes.

### `compute-adaptive-drift`

Scales checkpoint frequency and scaffolding while preserving tests.

## Potential Redundancy

### `mode-lock-in`

Mode lock prevents silent regime shifts; suppression is the general detect/repair loop and can enforce that lock.

### `working-memory-lock-in`

WM Lock prevents omission through salience; suppression corrects deviations that still occur.

## Conflict / Precedence Rules

- Latest authorized task/source state defines the baseline, not the oldest lock by default.
- When automated checks and cited source inspection disagree, hold the output and resolve the checker or source version.

## Failure Boundary

- Stop publication when a high-impact deviation cannot be repaired or adjudicated.
- Do not claim suppression if no independent baseline survives the transformation.

## Strong-Model Scaling

May skip:

- high-frequency low-risk checks after demonstrated stability
- verbose drift logs for trivial corrected style variance

Keep mandatory:

- source/task baseline
- risk-based checks
- minimal rollback
- high-impact stop condition

## Recommended Skill Types

- document and code transformation
- high-stakes evidence work
- long-context workflows
- review and quality assurance

## Example Composition

**Task context:** Repeated summarization makes a vendor's conditional warranty sound unconditional.

**Why it activates:** The qualification is a narrow-corridor claim and the output crossed it.

**Inputs/state:** Cited source clause, claim corridor, summary draft, and last validated version.

**Action:** Flags the lost condition, restores that claim, regenerates locally, and records qualification loss as a drift signature.

**Does not:** It does not rewrite the whole report or accept the smoother but inaccurate claim.

**Result/state change:** The repaired summary preserves the source condition.

**Companions:** ['controlled-drift-corridors', 'zero-drift-zones', 'task-set-lock-in']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-02` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `DRIFT_MONITOR_T1` (historical_assistant_artifact)
