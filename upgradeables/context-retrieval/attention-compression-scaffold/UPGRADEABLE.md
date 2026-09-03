# Attention Compression Scaffold

## Summary

A provisional scaffold for replacing bulky active context with a smaller, indexed, meaning-preserving representation.

## Purpose

Reduce attention burden while retaining the facts, constraints, provenance, and retrieval pointers required by the current subtask.

## Problem Solved

Addresses a workspace that is too large to reason over reliably, without treating lossy summarization as equivalent to source preservation.

## Where It Fits in the OS

Roles: context-retrieval, state projection, attention control. Pipeline stages: post-retrieval, pre-synthesis, context refresh.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long-context analysis
- large codebase navigation
- multi-document synthesis
- stateful agent workflows

## When Not to Use

- the original context is already small
- exact source wording must remain live
- no provenance pointers exist for re-expansion

## Scope

Canonical package: `attention-compression-scaffold@1.1.0`. ID: `JAN26-02`. Functional classes: context-retrieval, state. Activation: `U1-common-conditional`. Mechanism basis: `provisional`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- source volume exceeds the active workspace

## Non-Triggers

- the original context is already small
- exact source wording must remain live
- no provenance pointers exist for re-expansion

## Inputs / Required State

- large source or state context
- current task
- protected atoms
- source pointers
- compression budget

## Outputs / Produced State

- compact indexed context
- verbatim protected subset
- reload pointers
- compression validation status

## Mechanism

Modern operational interpretation: select task-relevant facts, locked literals, decisions, open questions, and source pointers from a larger context; encode them in a compact indexed view; validate that protected meaning and provenance remain recoverable; and keep a route back to the original material. Compression changes representation size, not truth status or authority.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Define the current subtask and protected atoms that compression must preserve.
2. Partition context into retain verbatim, summarize with provenance, pointer-only, and retire classes.
3. Build a compact indexed view with stable source references.
4. Check every locked atom and decision against the original context.
5. Use the compact view for the subtask while retaining reload pointers.
6. Refresh or invalidate the view when the task, source, or authoritative state changes.

## Always-Do Rules

- Preserve exact literals that cannot tolerate paraphrase.
- Retain source pointers for every compressed factual unit.
- Label the mechanism as a modern interpretation because only the historical name is recovered.

## Never-Do / Avoid Rules

- Do not treat a summary as an immutable source.
- Do not drop unresolved conflicts to make the view smaller.
- Do not claim the historical procedure was recovered.

## Interaction Rules

### `activation-budget-funnel`

ABF determines when captured evidence should leave the live pull set; compression creates the compact representation it enters.

### `stateblock`

Provides canonical fields and locked atoms that the compressed view must preserve.

## Compatible Upgradeables

- `activation-budget-funnel` — ABF determines when captured evidence should leave the live pull set; compression creates the compact representation it enters.
- `stateblock` — Provides canonical fields and locked atoms that the compressed view must preserve.

## Counterbalancing Upgradeables

### `zero-drift-zones`

Marks content that must stay verbatim rather than be compressed semantically.

## Potential Redundancy

### `structured-state-projection`

Projection limits fields for one consumer; compression reduces the representation of a broader relevant set.

### `working-memory-cues`

Cues are a few reminders, while this scaffold can carry a larger indexed evidence/state view.

## Conflict / Precedence Rules

- Zero-drift and source-fidelity requirements override compression goals.
- If meaning preservation cannot be verified, use the original context or a pointer rather than a lossy substitute.

## Failure Boundary

- Do not activate the compressed view when a protected fact, conflict, or provenance link is lost or unverifiable.

## Strong-Model Scaling

May skip:

- explicit compression for contexts that fit reliably
- verbose category labels when preservation can be demonstrated compactly

Keep mandatory:

- protected-atom preservation
- provenance and reloadability
- invalidation on state change

## Recommended Skill Types

- document and code transformation
- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Analyze a 200-file codebase while debugging one service.

**Why it activates:** Full repository context exceeds the active workspace.

**Inputs/state:** Relevant interfaces, failing trace, service dependencies, and file paths.

**Action:** Keeps exact signatures and errors, summarizes surrounding behavior with file pointers, and retires unrelated modules.

**Does not:** It does not rewrite signatures, discard conflicting traces, or pretend summaries are source files.

**Result/state change:** A compact debug context that can be expanded back to authoritative files.

**Companions:** ['activation-budget-funnel', 'zero-drift-zones']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-02` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeables_Historical_Recovery_Inventory.md — Initial named Upgradeables (historical_recovery_inventory)
- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — T2-040 — Attention Corridor Narrowing (historical_assistant_artifact)
