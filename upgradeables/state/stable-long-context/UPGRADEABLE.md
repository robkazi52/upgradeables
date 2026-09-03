# Stable Long-Context

## Summary

Keep a long task coherent by maintaining a small anchored current-state core, indexed evidence pointers, and explicit treatment of superseded material.

## Purpose

Extend usable context duration without treating the entire transcript as equally current or important.

## Problem Solved

Long contexts accumulate stale decisions, duplicate facts, buried constraints, and recency bias that can displace the task's real invariants.

## Where It Fits in the OS

Roles: long-horizon context control, semantic anchoring, memory compaction. Pipeline stages: initial anchoring, periodic compaction, context re-entry, final consistency check.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long research projects
- large document synthesis
- multi-session builds
- extended agent runs

## When Not to Use

- all relevant material fits clearly in one short exchange
- lossless verbatim retention is required for every item
- no reliable source pointers exist for compressed material

## Scope

Canonical package: `stable-long-context@1.1.0`. ID: `T2-07`. Functional classes: state, drift-control. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- large corpus or long-running workflow

## Non-Triggers

- all relevant material fits clearly in one short exchange
- lossless verbatim retention is required for every item
- no reliable source pointers exist for compressed material

## Inputs / Required State

- task anchors
- versioned state
- indexed evidence
- supersession markers
- retrieval need

## Outputs / Produced State

- compact current context
- stable evidence index
- superseded-state ledger
- resume package

## Mechanism

Maintain an invariant anchor containing task, authority, definitions, accepted decisions, and open obligations; keep detailed material behind stable indexed pointers; periodically reconcile new state, mark superseded items, and regenerate a compact current view. Retrieval expands only the region needed for the next step, and final validation checks output against the anchors rather than conversational recency.

## Procedure

1. Establish task, authority, terminology, and zero-drift facts as anchors.
2. Index detailed evidence and prior artifacts with stable identifiers.
3. At checkpoints, merge accepted deltas and mark replaced state as superseded.
4. Compact the active view while preserving pointers and unresolved items.
5. On resume, load the anchor first, then retrieve only the relevant detail.
6. Validate major outputs against the current anchors and source records.

## Always-Do Rules

- distinguish current, superseded, and unresolved state
- keep stable retrieval pointers
- re-anchor after major transitions

## Never-Do / Avoid Rules

- summarize away locked constraints
- treat the newest statement as automatically authoritative
- carry the full transcript as active working state

## Interaction Rules

### `stateblock`

Holds the compact current-state anchor.

### `sequential-memory-state-engine`

Supplies ordered deltas and current/history distinction.

### `attention-compression-scaffold`

Builds a smaller task-local view from the indexed long context.

## Compatible Upgradeables

- `stateblock` — Holds the compact current-state anchor.
- `sequential-memory-state-engine` — Supplies ordered deltas and current/history distinction.
- `attention-compression-scaffold` — Builds a smaller task-local view from the indexed long context.

## Counterbalancing Upgradeables

### `scoped-loader`

Prevents resume from eagerly loading the entire archive.

### `drift-suppression`

Detects meaning changes introduced by repeated compaction.

## Potential Redundancy

### `working-memory-lock-in`

WM Lock should be the critical active subset of the long-context anchor, not a parallel truth store.

### `state-snapshot`

Snapshots preserve versions; stable context manages which version and detail remain active.

## Conflict / Precedence Rules

- Explicit authority and accepted state transitions outrank recency.
- If compaction cannot preserve a high-impact nuance, retain the original excerpt or pointer in the active view.

## Failure Boundary

- Do not compact evidence beyond recoverability when precise citation is required.
- Rebuild from canonical sources when anchor integrity or version lineage is uncertain.

## Strong-Model Scaling

May skip:

- formal compaction in a short task
- persistent indices when source set is tiny

Keep mandatory:

- anchored invariants
- current-versus-superseded distinction
- retrievable provenance
- resume validation

## Recommended Skill Types

- long research projects
- large document synthesis
- multi-session builds
- extended agent runs

## Example Composition

**Task context:** A policy rewrite spans weeks and hundreds of source pages.

**Why it activates:** The working context must stay small without losing binding definitions and decisions.

**Inputs/state:** Locked scope, approved glossary, decision log, source index, and outstanding issues.

**Action:** Keeps those anchors active, compacts resolved discussion, and retrieves page-level detail only for the current section.

**Does not:** It does not reload every conversation or let the latest draft redefine approved terms.

**Result/state change:** Each session resumes coherently with traceable detail.

**Companions:** ['stateblock', 'scoped-loader', 'drift-suppression']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-07` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Long-Context Coherence.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Interpretation rule for the frozen T2 registry (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.4 Long-context source fidelity (historical_assistant_artifact)
