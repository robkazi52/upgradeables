# Domain Core Builder

## Summary

Builds a versioned high-density domain reference containing knowledge anchors, reasoning maps, evidence architecture, and decision logic, separate from behavior instructions.

## Purpose

Give multiple behaviors a shared, sourced domain substrate without duplicating knowledge across Genes or turning a Core into an OS.

## Problem Solved

Domain facts, evidence standards, variables, and decision patterns become scattered through prompts, drift across versions, and cannot be independently validated.

## Where It Fits in the OS

Roles: domain knowledge compiler, Core schema enforcer. Pipeline stages: domain scoping, source and variable modeling, Core construction, interface validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- recurring specialist domains
- evidence-intensive decisions
- policy or technical reference systems
- multi-Gene domain bundles

## When Not to Use

- the need is purely behavioral
- the source corpus is too weak to support a domain model
- a small on-demand reference is sufficient

## Scope

Canonical package: `domain-core-builder@1.1.0`. ID: `C-00`. Functional classes: meta-control, context-retrieval. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a recurring domain needs structured knowledge and decision logic

## Non-Triggers

- the need is purely behavioral
- the source corpus is too weak to support a domain model
- a small on-demand reference is sufficient

## Inputs / Required State

- domain scope
- authoritative corpus
- entities and variables
- decision requirements
- Gene and validator needs

## Outputs / Produced State

- versioned Domain Core
- reasoning and evidence maps
- typed interfaces
- source-fidelity tests

## Mechanism

Compile sourced domain material into the recovered Core fields: scope, entities and variables, reasoning map, required data, evidence hierarchy, decision logic, failure modes, canonical examples, Gene and validator interfaces, and version provenance. Keep prescriptive behavior in Genes, expose queries and typed outputs rather than dumping the entire Core into every task, and validate both source fidelity and interface sufficiency. The C-00 builder wrapper is a modern normalization of the recovered Core schema.

## Procedure

1. Define domain boundaries, target decisions, and excluded neighboring domains.
2. Inventory authoritative sources, entities, variables, required data, and uncertainty.
3. Build reasoning and evidence maps with provenance at the smallest maintainable units.
4. Encode decision logic, failure modes, and canonical examples without adding behavioral voice rules.
5. Declare query interfaces for Genes and validation interfaces for truth and citation checks.
6. Test retrieval sufficiency, source fidelity, conflicting evidence, and version migration; publish with provenance.

## Always-Do Rules

- separate knowledge from behavior
- preserve source and version provenance
- state required data and evidence hierarchy
- declare interfaces rather than assume whole-Core loading

## Never-Do / Avoid Rules

- present generated domain inference as sourced knowledge
- embed writing style and task behavior into the Core
- load the whole Core when a narrow query suffices
- claim C-00 is a directly recovered historical ID

## Interaction Rules

### `behavior-gene-builder`

Behavior Genes consume Core knowledge through declared interfaces without owning it.

### `citation-fidelity`

Citation Fidelity validates that Core atoms remain tied to their sources.

### `scoped-loader`

The loader retrieves only the Core sections relevant to the active task.

## Compatible Upgradeables

- `behavior-gene-builder` — Behavior Genes consume Core knowledge through declared interfaces without owning it.
- `citation-fidelity` — Citation Fidelity validates that Core atoms remain tied to their sources.
- `scoped-loader` — The loader retrieves only the Core sections relevant to the active task.

## Counterbalancing Upgradeables

### `behavior-gene-builder`

The Gene boundary prevents the Core from accumulating behavioral instructions.

## Potential Redundancy

### `stateblock`

StateBlock stores current task state; a Domain Core stores reusable domain knowledge and decision structure.

## Conflict / Precedence Rules

- Source evidence outranks a convenient decision map.
- Conflicting authoritative sources remain represented with scope and uncertainty rather than silently merged.
- Genes may select presentation or procedure but may not mutate sourced Core atoms.

## Failure Boundary

- knowledge-behavior conflation
- unsourced compression
- overbroad domain scope
- whole-Core context dumping
- unstated evidence conflict

## Strong-Model Scaling

May skip:

- verbose explanatory prose around a compact machine-readable map
- loading examples when the query is fully specified

Keep mandatory:

- source provenance
- evidence hierarchy
- Core/Gene separation
- interface contract
- conflict representation

## Recommended Skill Types

- recurring specialist domains
- evidence-intensive decisions
- policy or technical reference systems
- multi-Gene domain bundles

## Example Composition

**Task context:** Build a Core for software supply-chain incident analysis.

**Why it activates:** Several investigation and reporting Genes need the same entities, evidence ranking, and causal map.

**Inputs/state:** Incident standards, signed attestations, build logs, dependency graphs, and reporting requirements are sourced.

**Action:** Encodes entities, evidence hierarchy, data requirements, causal graph, decision logic, failure modes, and interfaces for an investigation Gene and citation validator.

**Does not:** Hard-code an executive writing tone or invent facts for missing logs.

**Result/state change:** A reusable sourced Core queried by multiple behaviors.

**Companions:** ['behavior-gene-builder', 'citation-fidelity', 'loader-sequencing']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `C-00` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — PART X. REASONING / SINGULARITY CORES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 13. Reasoning / Singularity Cores (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 14. BEHAVIOR GENE + CORE SEPARATION — HISTORICAL GENESIS (historical_assistant_artifact)
