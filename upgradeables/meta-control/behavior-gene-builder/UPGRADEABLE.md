# Behavior Gene Builder

## Summary

Builds compact, versioned modules that specify how a system should reason and write for a recurring task without embedding the task's domain knowledge store.

## Purpose

Turn repeatable behavior, logic, evidence handling, and output contracts into swappable components that compose with Cores and validators.

## Problem Solved

Behavior rules become duplicated, monolithic, or entangled with domain facts, making reuse, testing, versioning, and conflict resolution unreliable.

## Where It Fits in the OS

Roles: behavior-module factory, composition schema enforcer. Pipeline stages: recurrence analysis, gene specification, validation, versioned publication.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- recurring reasoning patterns
- domain-specific writing behavior
- tone or risk-emphasis modules
- research synthesis behaviors

## When Not to Use

- the content is primarily domain knowledge
- the behavior occurs only once
- the proposed gene duplicates a general invariant better kept global

## Scope

Canonical package: `behavior-gene-builder@1.1.0`. ID: `BG-00`. Functional classes: meta-control, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a recurring task family needs reusable behavior

## Non-Triggers

- the content is primarily domain knowledge
- the behavior occurs only once
- the proposed gene duplicates a general invariant better kept global

## Inputs / Required State

- recurring task pattern
- behavior examples and failures
- Gene schema
- Core and validator interfaces
- authority rules

## Outputs / Produced State

- versioned Behavior Gene
- activation and non-trigger rules
- composition contract
- behavioral tests

## Mechanism

Extract the invariant behavior shared by a task family and encode it in the recovered Gene schema: name/version, purpose, scope, triggers, always and avoid rules, reasoning pattern, evidence handling, Core interface, output contract, and compatibility notes. Test activation and non-activation cases, conflict precedence, and behavior with representative Cores; publish the behavior separately from knowledge and loader policy.

## Procedure

1. Collect repeated successful and failed task instances and isolate the stable behavior rather than domain facts.
2. Define scope, activation conditions, and explicit non-triggers.
3. Specify always-do, never-do, reasoning pattern, evidence handling, and output contract.
4. Declare Core, validator, and other-Gene interfaces plus authority and conflict rules.
5. Test positive activation, false activation, missing-Core, and conflicting-Gene cases.
6. Version and publish the Gene with provenance and composition notes.

## Always-Do Rules

- keep behavior separate from domain knowledge
- make activation and output contracts testable
- declare compatibility and precedence
- version behavioral changes

## Never-Do / Avoid Rules

- turn a Gene into a full OS
- copy a domain corpus into behavior instructions
- collapse materially distinct task families into one giant Gene
- claim hidden behavior outside the loaded module

## Interaction Rules

### `domain-core-builder`

The Gene queries or consumes a Core while remaining responsible only for behavior and output shape.

### `architect-orchestrator`

The architect loads and composes the right Gene for the task.

### `resonance-gene-builder`

Resonance Gene Builder creates a special coupling Gene when recurring cross-module coordination, not task behavior alone, is the target.

## Compatible Upgradeables

- `domain-core-builder` — The Gene queries or consumes a Core while remaining responsible only for behavior and output shape.
- `architect-orchestrator` — The architect loads and composes the right Gene for the task.
- `resonance-gene-builder` — Resonance Gene Builder creates a special coupling Gene when recurring cross-module coordination, not task behavior alone, is the target.

## Counterbalancing Upgradeables

### `domain-core-builder`

The Core boundary prevents behavior modules from becoming knowledge dumps.

## Potential Redundancy

### `resonance-gene-builder`

Both emit Genes, but the Resonance builder is limited to stable coupling rules among modules; this builder covers task and writing behaviors generally.

## Conflict / Precedence Rules

- Global truth, safety, and authorization rules outrank any Gene.
- A Gene may query a Core but cannot silently redefine its sourced domain facts.
- Conflicting Genes require declared precedence or explicit orchestration rather than blended instructions.

## Failure Boundary

- behavior-knowledge conflation
- monolithic Gene
- vague activation
- undeclared conflicts
- untested output contract

## Strong-Model Scaling

May skip:

- long narrative rationale when the schema fields and tests are self-explanatory

Keep mandatory:

- behavior/Core separation
- trigger contract
- always/avoid rules
- compatibility tests
- version metadata

## Recommended Skill Types

- recurring reasoning patterns
- domain-specific writing behavior
- tone or risk-emphasis modules
- research synthesis behaviors

## Example Composition

**Task context:** Create a compare-and-contrast behavior used across legal, medical, and technical Cores.

**Why it activates:** The comparison logic and output shape recur, while the evidence and entities differ by domain.

**Inputs/state:** Successful comparison examples, three Core interfaces, and truth validators are available.

**Action:** Encodes dimension selection, symmetric treatment, conflict surfacing, evidence rules, and output table contract without copying any domain facts.

**Does not:** Bundle the medical and legal corpora into the Gene.

**Result/state change:** One reusable behavior module that composes with several domain Cores.

**Companions:** ['domain-core-builder', 'architect-orchestrator']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `BG-00` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Behavior Gene OS.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — PART IX. BEHAVIOR GENE OS (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 12. Behavior Gene OS and known Genes (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 14. BEHAVIOR GENE + CORE SEPARATION — HISTORICAL GENESIS (historical_assistant_artifact)
