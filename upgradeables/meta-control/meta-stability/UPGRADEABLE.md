# Meta-Stability Mode

## Summary

Temporarily freezes optional change and restores a coherent checkpoint when repeated edits, long context, or module conflict destabilizes the workflow.

## Purpose

Preserve a trusted task state while isolating drift sources and resuming from one explicit authority-consistent configuration.

## Problem Solved

A workflow can become progressively less coherent as state versions diverge, optional modules compete, and repeated changes invalidate assumptions faster than validation catches them.

## Where It Fits in the OS

Roles: stability-preserving operating mode, coherence recovery boundary. Pipeline stages: instability detection, change freeze, checkpoint restoration, controlled resume.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long-context drift
- conflicting module activation
- repeated change cycles
- multi-agent state divergence

## When Not to Use

- one local defect can be repaired directly
- the trusted checkpoint is itself invalid
- freezing would delay urgent containment

## Scope

Canonical package: `meta-stability@1.1.0`. ID: `T4-15`. Functional classes: meta-control, state. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- coherence degrades under repeated change

## Non-Triggers

- one local defect can be repaired directly
- the trusted checkpoint is itself invalid
- freezing would delay urgent containment

## Inputs / Required State

- instability evidence
- current state
- last verified checkpoint
- module and authority map
- exit criteria

## Outputs / Produced State

- stabilized checkpoint
- quarantined delta set
- resolved authority configuration
- controlled resume plan

## Mechanism

On a defined instability signal, freeze optional activations and structural changes, select the latest verified state snapshot, and compare active goals, modules, decisions, and open issues against that checkpoint. Quarantine conflicting deltas, re-establish one authority order and next step, run a coherence check, then resume changes one at a time with observation; MSM stabilizes state, not content by force.

## Procedure

1. Confirm an instability trigger such as state divergence, repeated regression, or unresolved module conflict.
2. Pause optional changes and capture the current state without overwriting the last verified checkpoint.
3. Compare goals, decisions, modules, sources, and open issues with the verified snapshot.
4. Quarantine unverified deltas and resolve authority conflicts explicitly.
5. Run coherence, state-version, and invariant checks on the restored configuration.
6. Resume one bounded change at a time and exit MSM only after consecutive stable checkpoints.

## Always-Do Rules

- preserve the last verified checkpoint
- freeze optional change before diagnosis
- quarantine rather than erase disputed deltas
- define exit evidence

## Never-Do / Avoid Rules

- call ordinary uncertainty instability
- restore an unverified snapshot
- silently discard user-approved changes
- remain permanently frozen after exit criteria pass

## Interaction Rules

### `coherence-heartbeat`

The heartbeat supplies global coherence evidence before exit.

### `drift-suppression`

Drift Suppression holds task and source boundaries while state is stabilized.

### `stateblock`

StateBlock provides explicit versioned snapshots for comparison and restoration.

## Compatible Upgradeables

- `coherence-heartbeat` — The heartbeat supplies global coherence evidence before exit.
- `drift-suppression` — Drift Suppression holds task and source boundaries while state is stabilized.
- `stateblock` — StateBlock provides explicit versioned snapshots for comparison and restoration.

## Counterbalancing Upgradeables

### `adapter-first-experimentation`

Experiments should pause during instability and resume only after the base state is stable.

## Potential Redundancy

### `stuck-pattern-reset`

Reset abandons one failed reasoning path; Meta-Stability freezes and reconciles the whole active configuration.

### `safe-mode`

SAFE governs consequential execution; Meta-Stability governs recovery from scaffold and state instability.

## Conflict / Precedence Rules

- A user-approved newer decision is not rolled back solely because an older checkpoint is internally coherent.
- Urgent safety containment may proceed through a predeclared minimal path while optional work remains frozen.
- If no verified checkpoint exists, build one from authoritative state rather than fabricate restoration.

## Failure Boundary

- stability theater
- loss of newer valid state
- permanent freeze
- unverified rollback
- resuming all changes simultaneously

## Strong-Model Scaling

May skip:

- formal mode activation for a single reversible regression

Keep mandatory:

- verified checkpoint
- optional-change freeze
- authority reconciliation
- exit test

## Recommended Skill Types

- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Several agents edit a registry from different state versions and validations alternate between two failures.

**Why it activates:** Repeated changes and divergent state threaten global coherence.

**Inputs/state:** A last passing commit, agent diffs, current registry, and authority rules are available.

**Action:** Freezes new edits, compares each diff to the passing state, quarantines conflicting changes, rebuilds one authoritative state, validates it, then resumes changes sequentially.

**Does not:** Delete all recent work or keep launching more repair agents.

**Result/state change:** One coherent baseline and a controlled resume queue.

**Companions:** ['stateblock', 'coherence-heartbeat', 'meta-supervisor']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-15` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: MSM.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.1 SMSE — Sequential Memory State Engine (historical_assistant_artifact)
