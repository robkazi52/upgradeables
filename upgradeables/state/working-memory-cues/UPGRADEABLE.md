# Working-Memory Cues

## Summary

Place tiny, actionable reminders at decision points to re-surface a constraint, definition, or next check without reloading full state.

## Purpose

Keep easily forgotten but relevant information salient during execution.

## Problem Solved

Even when state is stored correctly, a model may fail to attend to the right item at the moment it matters.

## Where It Fits in the OS

Roles: attention prompt, state pointer, checkpoint reminder. Pipeline stages: before risky step, after context switch, before output, at known failure points.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long transformations
- repetitive tool loops
- tasks with a few recurring constraints
- review workflows

## When Not to Use

- the cue duplicates already salient text
- too many cues would become noise
- the cue would substitute for canonical state

## Scope

Canonical package: `working-memory-cues@1.1.0`. ID: `T1-09`. Functional classes: state. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- many constraints must remain active

## Non-Triggers

- the cue duplicates already salient text
- too many cues would become noise
- the cue would substitute for canonical state

## Inputs / Required State

- canonical state pointer
- known omission risk
- trigger step
- cue retirement condition

## Outputs / Produced State

- short contextual reminder
- state/source pointer
- cue lifecycle status

## Mechanism

Derive a very short cue from canonical state and attach it to the step where omission is likely: a field pointer, invariant, question, or validation instruction. Retire the cue when its trigger or risk disappears; changes to truth occur in canonical state, never inside the cue.

## Procedure

1. Identify a recurrent omission risk and its decision point.
2. Select the smallest canonical state item that prevents it.
3. Write an imperative cue with a stable field or source pointer.
4. Present it only at the triggering step.
5. Measure whether it prevents the omission and remove stale or redundant cues.

## Always-Do Rules

- keep cues short
- link them to canonical state
- scope them to a trigger
- remove stale cues

## Never-Do / Avoid Rules

- use cues as a second truth store
- flood every step with all constraints
- leave a cue active after its source changes

## Interaction Rules

### `stateblock`

Provides the authoritative value or pointer behind each cue.

### `working-memory-lock-in`

Cues can refresh locked critical items at specific moments.

### `stable-long-context`

Surfaces a detail from the long-context index without expanding all context.

## Compatible Upgradeables

- `stateblock` — Provides the authoritative value or pointer behind each cue.
- `working-memory-lock-in` — Cues can refresh locked critical items at specific moments.
- `stable-long-context` — Surfaces a detail from the long-context index without expanding all context.

## Counterbalancing Upgradeables

### `attention-compression-scaffold`

Provides a richer local view when one-line reminders are insufficient.

### `clarification-gateway`

Converts unresolved ambiguity into a question rather than an asserted cue.

## Potential Redundancy

### `working-memory-lock-in`

Use cues for momentary reminders and lock-in for continuously critical state; do not duplicate both verbatim everywhere.

### `mode-lock-in`

A cue may point to the mode but does not define or enforce it.

## Conflict / Precedence Rules

- Canonical state and higher-authority instructions override stale cues.
- When multiple cues compete, surface the one tied to the highest-risk immediate decision.

## Failure Boundary

- Do not cue an unverified claim as fact.
- Escalate to a larger state view when the decision cannot be represented safely in a short reminder.

## Strong-Model Scaling

May skip:

- explicit cues for a short simple task
- reminders for reliably salient constraints

Keep mandatory:

- highest-risk cue at transition points
- canonical pointer
- retirement discipline

## Recommended Skill Types

- long transformations
- repetitive tool loops
- tasks with a few recurring constraints
- review workflows

## Example Composition

**Task context:** Edit fifty contract clauses while preserving defined terms.

**Why it activates:** The same capitalization rule is easy to forget after many clauses.

**Inputs/state:** Canonical glossary field and a pre-clause validation trigger.

**Action:** Shows a one-line cue to verify defined-term capitalization before each clause is accepted.

**Does not:** It does not copy the whole glossary into every step or edit the glossary itself.

**Result/state change:** The recurring error is prevented with little context cost.

**Companions:** ['stateblock', 'working-memory-lock-in', 'drift-suppression']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-09` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 2. November 28, 2025 — frozen T1-Core Bundle v1 (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. Working-Memory Lock-In Heartbeats (historical_assistant_artifact)
