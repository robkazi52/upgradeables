# SelfBlock Auto-Update

## Summary

Apply a small, rule-governed state maintenance pass after meaningful actions so the canonical self/task block stays current without manual reconstruction.

## Purpose

Reduce stale state and forgotten deltas during iterative work.

## Problem Solved

A live state block becomes misleading when completed steps, new constraints, and invalidated assumptions are not incorporated promptly.

## Where It Fits in the OS

Roles: automatic state maintenance, checkpoint hook, staleness control. Pipeline stages: after meaningful action, after tool result, before handoff, before resume.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- agent loops
- long editing sessions
- tool-rich workflows
- multi-step investigations

## When Not to Use

- the host cannot write persistent state
- every token would trigger an update
- untrusted content could directly mutate authority-bearing fields

## Scope

Canonical package: `selfblock-auto-update@1.1.0`. ID: `T2-11`. Functional classes: state. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- the host can update explicit state after steps

## Non-Triggers

- the host cannot write persistent state
- every token would trigger an update
- untrusted content could directly mutate authority-bearing fields

## Inputs / Required State

- current state version
- action result
- mutable-field policy
- locked fields
- provenance

## Outputs / Produced State

- validated state delta
- updated SelfBlock version
- change record
- rejected-delta notice

## Mechanism

Attach an update hook to defined events, compute the smallest state delta, validate it against schema and authority, then atomically merge it into the live SelfBlock while retaining provenance or a change note. The updater may change status and observations but not silently rewrite locked goals, permissions, or immutable evidence.

## Procedure

1. Define update-triggering events and mutable fields.
2. After an event, derive only the factual delta from the result.
3. Reject or quarantine changes to locked or authority-bearing fields.
4. Validate the delta against schema, provenance, and current version.
5. Apply atomically and record timestamp/version or concise change note.

## Always-Do Rules

- update by delta
- protect locked fields
- validate before commit
- retain change provenance

## Never-Do / Avoid Rules

- rewrite the whole block from memory
- let retrieved text alter permissions
- mark work complete without supporting result state

## Interaction Rules

### `stateblock`

SelfBlock Auto-Update is the maintenance hook for a canonical block.

### `working-memory-lock-in`

Refreshes the critical subset after accepted state changes.

### `state-snapshot`

Snapshots stable versions at important checkpoints.

## Compatible Upgradeables

- `stateblock` — SelfBlock Auto-Update is the maintenance hook for a canonical block.
- `working-memory-lock-in` — Refreshes the critical subset after accepted state changes.
- `state-snapshot` — Snapshots stable versions at important checkpoints.

## Counterbalancing Upgradeables

### `drift-suppression`

Audits update deltas for semantic drift.

### `clarification-gateway`

Requires human clarification instead of auto-updating ambiguous authority fields.

## Potential Redundancy

### `sequential-memory-state-engine`

SMSE manages the broader ingest/update lifecycle; use its commit stage as the hook instead of a parallel updater.

### `stateblock`

The updater must not become a second state store.

## Conflict / Precedence Rules

- Locked goal, authority, and permission fields cannot be auto-mutated by lower-authority observations.
- Concurrent deltas require version checking or merge arbitration rather than last-write-wins.

## Failure Boundary

- Disable automatic writes when atomicity, schema validation, or authority checks are unavailable.
- Escalate ambiguous changes to task identity or permissions.

## Strong-Model Scaling

May skip:

- updates after semantically empty turns
- persistent writes in a short stateless exchange

Keep mandatory:

- delta discipline
- locked-field protection
- version/provenance checks

## Recommended Skill Types

- agent loops
- long editing sessions
- tool-rich workflows
- multi-step investigations

## Example Composition

**Task context:** An agent finishes validating dataset column types.

**Why it activates:** The completion and two discovered anomalies change live task state.

**Inputs/state:** State version 8, validation output, immutable objective, and mutable progress/anomaly fields.

**Action:** Writes a version-checked delta marking validation complete and adding cited anomalies.

**Does not:** It does not rewrite the objective or infer that the entire project is complete.

**Result/state change:** Version 9 accurately reflects progress and exceptions.

**Companions:** ['stateblock', 'sequential-memory-state-engine', 'working-memory-lock-in']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-11` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — SelfBlock Auto-Update (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.1 Kernel / State Block (historical_assistant_artifact)
