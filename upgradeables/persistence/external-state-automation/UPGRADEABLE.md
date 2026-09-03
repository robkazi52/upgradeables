# External State Automation

## Summary

Serialize and restore important task state through real files, memory stores, databases, or project documents when the host supports persistence.

## Purpose

Serialize and restore important task state through real files, memory stores, databases, or project documents when the host supports persistence.

## Problem Solved

Long-running work loses decisions across sessions when state exists only in transient context, while false persistence claims make continuation unreliable.

## Where It Fits in the OS

Roles: persistence interface, continuation state management. Pipeline stages: state checkpoint, external write, session restoration, consistency verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-session projects
- durable agent workflows
- long document production

## When Not to Use

- the task ends in one session and needs no continuation
- the host exposes no authorized persistent storage

## Scope

Canonical package: `external-state-automation@1.1.0`. ID: `T2-20`. Functional classes: state, persistence. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- continuation requires real external state

## Non-Triggers

- the task ends in one session and needs no continuation
- the host exposes no authorized persistent storage

## Inputs / Required State

- explicit task state and continuation requirements
- authorized storage capability and policy
- state schema and provenance

## Outputs / Produced State

- verified persisted state reference
- validated restored state or explicit persistence failure

## Mechanism

Declare the actual storage capability and a versioned state schema, serialize only the minimum continuation fields with provenance and timestamp, write through an authorized host operation, and verify the write. On restoration, validate version and integrity before merging; never treat a requested or imagined write as persisted state.

## Procedure

1. Confirm an authorized storage mechanism, location, lifetime, and data policy.
2. Select the minimum state fields needed for continuation and serialize them with schema and provenance.
3. Write through the real host capability and verify the stored representation.
4. On resume, read and validate schema, integrity, freshness, and authority.
5. Reconcile restored state with current instructions and report any failed or stale persistence.

## Always-Do Rules

- Preserve the defining invariant: capability declaration, minimum-state serialization, write verification, and restore validation.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- claiming memory without a real write or storing unbounded conversation data
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `state-snapshot`

Produces the minimum continuation representation to serialize.

### `state-routing-bus`

Moves restored state to the authorized receiving module.

## Compatible Upgradeables

- `state-snapshot` — Produces the minimum continuation representation to serialize.
- `state-routing-bus` — Moves restored state to the authorized receiving module.

## Counterbalancing Upgradeables

### `authority-anchor-enforcement`

Limits sensitive or unnecessary fields before durable storage.

## Potential Redundancy

### `state-snapshot`

Snapshot defines the representation; External State Automation performs and verifies real persistence.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If no authorized storage capability is available, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- no authorized storage capability is available
- write verification, schema validation, integrity, freshness, or restoration reconciliation fails

## Strong-Model Scaling

May skip:

- durable writes for a short task with no continuation need

Keep mandatory:

- capability declaration, minimum-state serialization, write verification, and restore validation

## Recommended Skill Types

- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A multi-day literature review must resume after context resets.

**Why it activates:** Verified decisions and source pointers need durable continuation.

**Inputs/state:** State snapshot, project file permission, schema version, provenance, and retention policy.

**Action:** Writes the compact snapshot to an authorized file, verifies it, and validates it on resume.

**Does not:** Does not claim persistence before the write succeeds or store the whole conversation by default.

**Result/state change:** The next session restores traceable state or receives an explicit failure/staleness warning.

**Companions:** State Snapshot creates the payload; State Routing Bus delivers it after restore.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-20` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
