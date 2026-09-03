# Sequential Memory State Engine (SMSE)

## Summary

Process each new event through an ordered state transition pipeline so memory evolves by validated deltas rather than uncontrolled accumulation.

## Purpose

Preserve sequence, provenance, relevance, and current truth across long-running work.

## Problem Solved

Appending everything to context loses temporal order, retains superseded facts, and makes concurrent or contradictory updates hard to reconcile.

## Where It Fits in the OS

Roles: state transition engine, memory lifecycle, provenance and conflict control. Pipeline stages: ingest, normalize, classify, compare, resolve, commit, project, checkpoint.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long-lived agents
- case management
- iterative research
- multi-source evolving records

## When Not to Use

- a one-shot task has no state evolution
- event ordering cannot be established and ordering is safety-critical
- the host needs a simpler immutable evidence log

## Scope

Canonical package: `sequential-memory-state-engine@1.1.0`. ID: `T2-10`. Functional classes: state, persistence. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- state changes across steps or source chunks

## Non-Triggers

- a one-shot task has no state evolution
- event ordering cannot be established and ordering is safety-critical
- the host needs a simpler immutable evidence log

## Inputs / Required State

- ordered events
- current state version
- schema
- authority hierarchy
- conflict policy

## Outputs / Produced State

- new state version
- transition record
- resolved current view
- consumer projections
- unresolved-conflict flags

## Mechanism

For each event, preserve source and time, normalize it into the state schema, classify affected fields, compare with the current version, resolve contradiction by authority and recency rules, commit an atomic delta, derive consumer-specific projections, and emit a checkpoint. History remains available, but only the resolved current state drives action.

## Procedure

1. Ingest one event with source, time, and authority metadata.
2. Normalize it without discarding the original payload pointer.
3. Classify affected state fields and compare against the current version.
4. Resolve additions, updates, contradictions, and retractions using explicit precedence.
5. Commit the delta atomically and increment the version.
6. Refresh downstream projections and checkpoint the transition.

## Always-Do Rules

- preserve event order and provenance
- distinguish current state from history
- resolve contradictions before projection
- version commits

## Never-Do / Avoid Rules

- append contradictory facts as simultaneously current
- let arrival order override higher authority
- erase prior state without a trace

## Interaction Rules

### `stateblock`

SMSE evolves the canonical StateBlock.

### `selfblock-auto-update`

Can implement the bounded commit hook after each accepted event.

### `state-snapshot`

Serializes milestone versions for recovery.

## Compatible Upgradeables

- `stateblock` — SMSE evolves the canonical StateBlock.
- `selfblock-auto-update` — Can implement the bounded commit hook after each accepted event.
- `state-snapshot` — Serializes milestone versions for recovery.

## Counterbalancing Upgradeables

### `stable-long-context`

Adds lifecycle pruning and salience controls when history grows.

### `drift-suppression`

Checks that normalized transitions retain source meaning.

## Potential Redundancy

### `selfblock-auto-update`

Use Auto-Update as SMSE's commit hook, not a competing transition engine.

### `working-memory-lock-in`

WM Lock should derive its active subset from SMSE state.

## Conflict / Precedence Rules

- Authority outranks recency unless the authoritative source explicitly delegates update power.
- Unresolvable contradictions remain labeled and block dependent actions rather than being averaged.

## Failure Boundary

- Stop dependent actions when a safety-critical contradiction cannot be resolved.
- Do not assert chronological correctness when timestamps or event identity are missing.

## Strong-Model Scaling

May skip:

- persistent event machinery for short linear work
- materialized projections when one consumer uses the full safe state

Keep mandatory:

- ordered transitions
- provenance
- current/history separation
- explicit conflict resolution

## Recommended Skill Types

- long-lived agents
- case management
- iterative research
- multi-source evolving records

## Example Composition

**Task context:** A support case receives a user correction after an earlier automated classification.

**Why it activates:** The new event supersedes part of current state but history must remain auditable.

**Inputs/state:** Version 12, both events, timestamps, and an authority rule favoring user-confirmed account facts.

**Action:** Normalizes the correction, resolves the conflict, commits version 13, and refreshes the support-agent view.

**Does not:** It does not delete the earlier classification or keep both values current.

**Result/state change:** Current state is corrected with a traceable transition.

**Companions:** ['stateblock', 'state-snapshot', 'stable-long-context']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-10` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: SMSE.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.1 SMSE — Sequential Memory State Engine (historical_assistant_artifact)
