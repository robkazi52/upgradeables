# Surgery Editing

## Summary

Replaces or reorganizes architecture-level structures through an explicit cutover and migration plan when a bounded CRISPR patch cannot work.

## Purpose

Make macro changes to layers, cores, workflows, or incompatible interfaces without losing invariants, dependents, or rollback control.

## Problem Solved

Large structural changes fail when treated as accumulated local edits: hidden interfaces break, old and new architectures coexist ambiguously, and rollback becomes impossible.

## Where It Fits in the OS

Roles: macro-architecture editor, structural migration operator. Pipeline stages: structural diagnosis, interface inventory, replacement design, migration and cutover, global validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- layer reorganization
- Core replacement
- major workflow change
- large incompatible refactor
- schema or public interface migration

## When Not to Use

- a localized invariant-preserving patch suffices
- the replacement architecture lacks acceptance criteria
- migration or rollback cannot be made safe
- the desired outcome is only prose polish

## Scope

Canonical package: `surgery-edit@1.1.0`. ID: `A-08`. Functional classes: editing-repair, orchestration. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- layers, Cores, or workflows require major replacement

## Non-Triggers

- a localized invariant-preserving patch suffices
- the replacement architecture lacks acceptance criteria
- migration or rollback cannot be made safe
- the desired outcome is only prose polish

## Inputs / Required State

- current architecture
- failure evidence
- interface and dependency inventory
- replacement design
- invariants
- migration and rollback constraints

## Outputs / Produced State

- responsibility and interface map
- replacement architecture
- migration plan
- validated cutover
- retirement audit

## Mechanism

Declare the failing structural boundary and why CRISPR cannot preserve it, inventory every inbound and outbound interface, and define a replacement architecture with mapped invariants. Plan old-to-new state migration, adapters, staged cutover, observability, and rollback; change the structure in bounded phases, validate each dependent contract, then remove the old path only after the replacement passes global checks.

## Procedure

1. Document the architecture-level failure and evidence that local editing is insufficient.
2. Inventory components, state, public and internal interfaces, dependents, precedence rules, and invariants.
3. Design the replacement structure and map every old responsibility and interface to retain, adapt, retire, or explicitly reject.
4. Define migration order, compatibility adapters, checkpoints, observability, rollback, and cutover criteria.
5. Implement or specify the replacement in stages while validating each interface and state transfer.
6. Cut over only when criteria pass; remove the old structure, audit for orphaned references, and record irreversible decisions.

## Always-Do Rules

- prove macro scope
- inventory interfaces before cutting
- map invariants and state migration
- stage cutover with rollback
- audit orphaned dependents

## Never-Do / Avoid Rules

- invoke Surgery for a local defect
- replace structure without a responsibility map
- run old and new precedence rules ambiguously
- remove the old path before dependent contracts pass

## Interaction Rules

### `regenerative-rewrite`

Regenerative Rewrite can repopulate a replaced structure from locked truth after Surgery defines the new architecture.

### `task-set-lock-in`

Task-Set Lock-In preserves objectives and non-negotiable invariants across the migration.

### `forethought-checkpoints`

Forethought gates irreversible cutover and retirement steps.

## Compatible Upgradeables

- `regenerative-rewrite` — Regenerative Rewrite can repopulate a replaced structure from locked truth after Surgery defines the new architecture.
- `task-set-lock-in` — Task-Set Lock-In preserves objectives and non-negotiable invariants across the migration.
- `forethought-checkpoints` — Forethought gates irreversible cutover and retirement steps.

## Counterbalancing Upgradeables

### `crispr-edit`

CRISPR is preferred when the change fits a bounded invariant-preserving patch and prevents unnecessary surgery.

### `micro-repair`

Micro-Repair handles isolated defects without architecture disruption.

## Potential Redundancy

### `regenerative-rewrite`

Both operate globally; Surgery changes structural components and interfaces, while Regenerative Rewrite rebuilds content against a locked ledger.

## Conflict / Precedence Rules

- Use CRISPR when all required behavior can coexist with current interfaces inside a bounded patch.
- A hard invariant without a valid old-to-new mapping blocks cutover.
- If rollback is impossible, raise the validation threshold and obtain explicit authority before commitment.

## Failure Boundary

- macro edit disguised as patch accumulation
- unmapped dependents
- dual-authority old and new paths
- state loss
- irreversible cutover without evidence
- architecture astronautics

## Strong-Model Scaling

May skip:

- a heavyweight migration document for an internal, versioned, fully reversible refactor

Keep mandatory:

- CRISPR-insufficiency proof
- interface inventory
- old-to-new mapping
- cutover and rollback gates

## Recommended Skill Types

- layer reorganization
- Core replacement
- major workflow change
- large incompatible refactor
- schema or public interface migration

## Example Composition

**Task context:** Replace a monolithic skill loader with scoped loading and a registry.

**Why it activates:** The change alters selection, dependency resolution, package interfaces, and state migration across the repository.

**Inputs/state:** Current loader contracts, package metadata, callers, tests, and rollback version are known.

**Action:** Maps every loader responsibility, designs registry adapters, migrates callers in stages, validates resolution and fallback, then removes the monolith after cutover checks.

**Does not:** Patch conditionals into the old loader until it accidentally behaves like two architectures.

**Result/state change:** One coherent loader architecture with migrated dependents and an auditable retirement.

**Companions:** ['forethought-checkpoints', 'task-set-lock-in', 'regenerative-rewrite']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-08` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-08. Surgery Editing (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.5 OS / Skill construction (historical_assistant_artifact)
