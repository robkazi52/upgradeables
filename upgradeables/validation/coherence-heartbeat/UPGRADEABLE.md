# Global Coherence Heartbeat

## Summary

A lightweight periodic pulse that rechecks whether current work still agrees with the active objective, constraints, state, and accepted decisions.

## Purpose

Detect long-horizon drift early without rerunning a full review after every step.

## Problem Solved

Extended work can remain locally competent while silently departing from the task, overwriting earlier decisions, or losing state continuity.

## Where It Fits in the OS

Roles: continuous-coherence-monitor, drift-early-warning. Pipeline stages: during long execution, after milestones, before irreversible steps.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long coding sessions
- multi-stage research
- agent orchestration
- large document production

## When Not to Use

- the task completes in one obvious operation
- a full coherence loop is already required at the same boundary

## Scope

Canonical package: `coherence-heartbeat@1.1.0`. ID: `A-04`. Functional classes: validation, state. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a workflow is long or multi-stage

## Non-Triggers

- the task completes in one obvious operation
- a full coherence loop is already required at the same boundary

## Inputs / Required State

- baseline snapshot
- current state
- checkpoint trigger
- accepted change log

## Outputs / Produced State

- aligned/warning/repair signal
- state delta
- loop escalation request

## Mechanism

At predefined cadence or meaningful state transitions, compare a compact current-state snapshot against four anchors: objective, hard constraints, accepted decisions, and outstanding obligations. Emit a small delta signal—aligned, warning, or repair-required—and escalate to a full coherence loop only when the pulse detects material divergence.

## Procedure

1. Capture a compact baseline of objective, constraints, decisions, and open obligations.
2. Choose event-based or interval checkpoints proportional to task length.
3. At each checkpoint, compare current state with every anchor.
4. Classify differences as intended progress, harmless update, or drift.
5. Repair small drift immediately; invoke a coherence loop for systemic mismatch.
6. Refresh the baseline only after the change is explicitly accepted.

## Always-Do Rules

- Keep the pulse cheap enough to run repeatedly.
- Distinguish authorized state change from drift.
- Escalate material discrepancies.

## Never-Do / Avoid Rules

- Silently rewrite the baseline to match current behavior.
- Use the heartbeat as a substitute for deep final validation.

## Interaction Rules

### `state-snapshot`

Provides the compact state compared on each pulse.

### `coherence-loops`

Receives escalations when a pulse finds systemic drift.

### `stable-long-context`

Supplies persistent anchors over long execution.

## Compatible Upgradeables

- `state-snapshot` — Provides the compact state compared on each pulse.
- `coherence-loops` — Receives escalations when a pulse finds systemic drift.
- `stable-long-context` — Supplies persistent anchors over long execution.

## Counterbalancing Upgradeables

### `dynamic-depth-allocation`

Keeps routine pulses lightweight and spends depth only on detected risk.

## Potential Redundancy

### `coherence-loops`

Heartbeat is frequent detection; loops are bounded diagnosis and repair.

## Conflict / Precedence Rules

- Hard constraints and explicit user updates outrank the stored baseline.
- Do not accept a baseline refresh merely to clear an unresolved warning.

## Failure Boundary

- Escalate when a hard constraint, core objective, or accepted decision no longer matches current work.

## Strong-Model Scaling

May skip:

- scheduled pulses during very short tasks

Keep mandatory:

- event-triggered pulse after major state changes in long work

## Recommended Skill Types

- long coding sessions
- multi-stage research
- agent orchestration
- large document production

## Example Composition

**Task context:** An agent is implementing a repository across several hours and many files.

**Why it activates:** Local edits can drift from the handoff while still passing narrow tests.

**Inputs/state:** A baseline naming public-community use, canonical sources, and no invented history.

**Action:** After generation, notices several files imply unsupported provenance and triggers repair.

**Does not:** Rerun every test suite after each file edit.

**Result/state change:** Drift is caught before release while routine checkpoints remain cheap.

**Companions:** ['state-snapshot', 'coherence-loops', 'stable-long-context']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-04. Global Coherence Heartbeat (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — A-04. Global Coherence Heartbeat (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — Coherence Heartbeat (historical_assistant_artifact)
