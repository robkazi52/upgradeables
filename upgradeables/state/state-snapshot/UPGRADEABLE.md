# State Snapshot

## Summary

Serialize a validated point-in-time state version for recovery, comparison, or handoff without turning the copy into a second live authority.

## Purpose

Create a stable checkpoint that can be resumed or audited after interruption.

## Problem Solved

Live state can change during a handoff, crash, or review, leaving no reproducible account of what was believed and pending at that moment.

## Where It Fits in the OS

Roles: checkpoint, recovery artifact, handoff package. Pipeline stages: milestone completion, before risky transition, handoff, recovery.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-session projects
- agent handoffs
- rollback-sensitive workflows
- audits

## When Not to Use

- a snapshot would persist prohibited sensitive data
- state is invalid or mid-transaction
- a one-turn task needs no recovery

## Scope

Canonical package: `state-snapshot@1.1.0`. ID: `O-03`. Functional classes: state, persistence. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a workflow pauses, hands off, or persists

## Non-Triggers

- a snapshot would persist prohibited sensitive data
- state is invalid or mid-transaction
- a one-turn task needs no recovery

## Inputs / Required State

- validated StateBlock version
- schema version
- provenance index
- unresolved obligations
- retention policy

## Outputs / Produced State

- immutable snapshot
- integrity and lineage metadata
- resume instructions

## Mechanism

At an explicit checkpoint, validate and freeze the canonical state version together with schema version, timestamp, task identity, provenance pointers, unresolved items, and a link to any previous snapshot. Consumers resume by verifying lineage and reconciling newer events; the snapshot itself remains immutable.

## Procedure

1. Choose a transaction-safe checkpoint.
2. Validate required fields and unresolved-state labels.
3. Serialize the state plus schema/version, time, identity, and provenance pointers.
4. Compute or record an integrity identifier and predecessor link.
5. On resume, verify integrity and reconcile all post-snapshot events before acting.

## Always-Do Rules

- freeze an identified state version
- record unresolved work
- verify lineage on restore
- apply retention and sensitivity policy

## Never-Do / Avoid Rules

- snapshot a half-applied transition
- mutate a stored snapshot
- resume without checking for newer authoritative events

## Interaction Rules

### `stateblock`

Captures one validated version of canonical state.

### `sequential-memory-state-engine`

Uses the snapshot as a checkpoint between ordered event transitions.

### `stable-long-context`

Provides a compact resume anchor for long work.

## Compatible Upgradeables

- `stateblock` — Captures one validated version of canonical state.
- `sequential-memory-state-engine` — Uses the snapshot as a checkpoint between ordered event transitions.
- `stable-long-context` — Provides a compact resume anchor for long work.

## Counterbalancing Upgradeables

### `selfblock-auto-update`

Returns restored state to controlled live updates after recovery.

### `scoped-loader`

Loads only snapshot-linked detail needed for the resumed task.

## Potential Redundancy

### `stateblock`

The snapshot is immutable history, never a parallel live StateBlock.

### `working-memory-lock-in`

The lock may be reconstructed from a snapshot but should not be snapshotted independently as another authority.

## Conflict / Precedence Rules

- A newer validated canonical state outranks an older snapshot.
- If snapshot identity or lineage fails verification, rebuild from authoritative events instead of guessing.

## Failure Boundary

- Do not restore when integrity, task identity, or schema compatibility cannot be established.
- Exclude or redact fields that cannot legally or safely persist.

## Strong-Model Scaling

May skip:

- durable snapshots for short disposable work
- full evidence embedding when stable pointers suffice

Keep mandatory:

- immutable version identity
- unresolved items
- provenance pointers
- resume reconciliation

## Recommended Skill Types

- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A research agent hands an unfinished review to another session.

**Why it activates:** The second session must know exactly which sources and claims were accepted at handoff.

**Inputs/state:** State version 21, schema v3, evidence index, open questions, and next action.

**Action:** Freezes those fields with integrity and predecessor metadata, then verifies new events on restore.

**Does not:** It does not treat the copy as live or omit unresolved questions.

**Result/state change:** The review resumes from a reproducible checkpoint.

**Companions:** ['stateblock', 'stable-long-context', 'sequential-memory-state-engine']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `O-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 4. State Growth (historical_assistant_artifact)
