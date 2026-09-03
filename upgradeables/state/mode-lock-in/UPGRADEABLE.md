# Mode Lock-In

## Summary

Select one operating mode for the task, record its invariants, and require an explicit transition rather than allowing style or policy drift.

## Purpose

Keep behavior stable across long sessions, tool calls, and distracting inputs.

## Problem Solved

Models may silently change from research to brainstorming, strict transformation to creative rewriting, or one policy regime to another.

## Where It Fits in the OS

Roles: behavioral stability, mode control, transition governance. Pipeline stages: after clarification, before substantive work, at transition requests, final validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- strict transformations
- long sessions
- multi-mode assistants
- policy-bound work

## When Not to Use

- exploration intentionally needs rapid mode switching
- the user has not yet chosen among materially different modes
- a mode label would add no operative constraint

## Scope

Canonical package: `mode-lock-in@1.1.0`. ID: `T1-05`. Functional classes: state, drift-control. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a task can drift between modes

## Non-Triggers

- exploration intentionally needs rapid mode switching
- the user has not yet chosen among materially different modes
- a mode label would add no operative constraint

## Inputs / Required State

- selected mode
- mode invariants
- forbidden behaviors
- transition authority
- current task state

## Outputs / Produced State

- active-mode contract
- deviation checks
- explicit transition record

## Mechanism

Represent the active mode as a small contract containing its goal, allowed transformations, forbidden behaviors, and exit condition. Recheck the contract at checkpoints; change modes only through an explicit transition that records why, what state carries forward, and which former rules deactivate.

## Procedure

1. Choose the mode from the clarified task and authority stack.
2. Write its operative invariants and exclusions into active state.
3. Tag work products and tool calls with the active mode where useful.
4. At checkpoints, test for deviations from the invariant set.
5. On an authorized switch, record the transition and replace rather than blend incompatible mode rules.

## Always-Do Rules

- make the active mode inspectable
- define an exit or transition condition
- revalidate after context changes

## Never-Do / Avoid Rules

- silently blend incompatible modes
- treat tone alone as the mode contract
- preserve superseded mode rules after transition

## Interaction Rules

### `task-set-lock-in`

Task Set locks the objective while Mode Lock stabilizes how the task is performed.

### `domain-mode-isolation`

Isolation prevents the locked mode's state from contaminating another domain.

### `drift-suppression`

Detects and corrects deviations from locked mode invariants.

## Compatible Upgradeables

- `task-set-lock-in` — Task Set locks the objective while Mode Lock stabilizes how the task is performed.
- `domain-mode-isolation` — Isolation prevents the locked mode's state from contaminating another domain.
- `drift-suppression` — Detects and corrects deviations from locked mode invariants.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Allows bounded variation inside a locked mode when exact rigidity would be counterproductive.

### `clarification-gateway`

Prevents premature commitment when the intended mode is ambiguous.

## Potential Redundancy

### `task-set-lock-in`

Use one shared contract for overlapping objective and mode fields rather than duplicating them.

### `working-memory-lock-in`

WM Lock refreshes critical facts; it should point to, not duplicate, the mode contract.

## Conflict / Precedence Rules

- Higher-authority instructions may force a mode transition; user content cannot silently do so.
- When mode and task objective conflict, clarify or reselect rather than weakening either implicitly.

## Failure Boundary

- Do not lock an ambiguous high-impact choice before clarification.
- Release or transition the lock when the task legitimately changes.

## Strong-Model Scaling

May skip:

- repeating the mode label in every response
- formal transition records for a one-turn low-risk task

Keep mandatory:

- operative invariants
- no silent switching
- checkpoint validation

## Recommended Skill Types

- strict transformations
- long sessions
- multi-mode assistants
- policy-bound work

## Example Composition

**Task context:** Transform policy text without changing meaning.

**Why it activates:** Creative rewriting would violate the requested transformation mode.

**Inputs/state:** A fidelity-first mode with preserve-meaning and no-new-claims invariants.

**Action:** Checks each revision against the locked transformation contract.

**Does not:** It does not drift into persuasive copywriting after seeing marketing language.

**Result/state change:** A clearer document with preserved claims and traceable exceptions.

**Companions:** ['task-set-lock-in', 'drift-suppression', 'zero-drift-zones']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-05` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 2. November 28, 2025 — frozen T1-Core Bundle v1 (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. Working-Memory Lock-In Heartbeats (historical_assistant_artifact)
