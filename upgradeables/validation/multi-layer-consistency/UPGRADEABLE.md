# Multi-Layer Consistency

## Summary

Checks that atom, paragraph or component, section or subsystem, and global-artifact representations agree without hiding contradictions between levels.

## Purpose

Maintain vertical consistency from local facts and operations to the overall conclusion or system behavior.

## Problem Solved

Each local unit can look valid while their aggregate contradicts the stated architecture, thesis, policy, or global constraint.

## Where It Fits in the OS

Roles: vertical-consistency-validator, cross-scale-invariant-check. Pipeline stages: integration, hierarchical validation, pre-release.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- large documents
- modular software
- policy hierarchies
- multi-step analytical conclusions

## When Not to Use

- the artifact has only one meaningful level
- levels are intentionally alternative rather than nested

## Scope

Canonical package: `multi-layer-consistency@1.1.0`. ID: `T2-05`. Functional classes: validation, orchestration. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- multiple authority layers are composed

## Non-Triggers

- the artifact has only one meaningful level
- levels are intentionally alternative rather than nested

## Inputs / Required State

- layer map
- local facts or tests
- intermediate claims
- global objective and constraints

## Outputs / Produced State

- cross-layer trace
- boundary mismatch list
- coherent hierarchy or repair request

## Mechanism

Define nested levels and invariants linking them, then validate both upward and downward: atoms must support their containing unit, units must compose into section or subsystem claims, and the global result must not assert anything contradicted below; conversely global constraints must be realized in the relevant lower layers. A pass requires agreement across boundaries, not independent passes at each level.

## Procedure

1. Map the artifact into atom, local unit, intermediate group, and global levels.
2. State invariants and claimed summaries at each boundary.
3. Check upward support from atoms to local and global claims.
4. Check downward realization of global constraints in lower levels.
5. Locate contradictions, orphan claims, and locally valid but globally incompatible parts.
6. Repair at the earliest causal level and rerun affected boundaries.

## Always-Do Rules

- Check boundary relationships, not only each level in isolation.
- Trace global claims to lower-level support.
- Propagate lower-level uncertainty upward.

## Never-Do / Avoid Rules

- Infer global consistency from all local tests passing.
- Force consistency by deleting legitimate local exceptions without explanation.

## Interaction Rules

### `parallel-qms`

HQMS is the specialized QMS mode that runs these hierarchical checks.

### `bidirectional-consistency`

Strengthens upward support with downward realization.

### `coherence-loops`

Repairs contradictions that span multiple layers.

## Compatible Upgradeables

- `parallel-qms` — HQMS is the specialized QMS mode that runs these hierarchical checks.
- `bidirectional-consistency` — Strengthens upward support with downward realization.
- `coherence-loops` — Repairs contradictions that span multiple layers.

## Counterbalancing Upgradeables

### `domain-mode-isolation`

Prevents constraints from one domain layer leaking into an unrelated one.

## Potential Redundancy

### `cross-universe-consistency`

Multi-Layer checks nested scales within one artifact; CUCM checks alternative branch worlds.

## Conflict / Precedence Rules

- A lower-level verified contradiction defeats an unsupported global summary.
- An explicit global hard constraint requires lower-layer implementation or a documented exception.

## Failure Boundary

- Do not certify when a global claim lacks lower-layer support or a lower-layer fact violates an undeclared global exception.

## Strong-Model Scaling

May skip:

- formal four-level labeling for a tiny artifact

Keep mandatory:

- at least one upward and one downward boundary check in hierarchical work

## Recommended Skill Types

- large documents
- modular software
- policy hierarchies
- multi-step analytical conclusions

## Example Composition

**Task context:** Every module test passes, but the application claims all writes are transactional.

**Why it activates:** The global guarantee depends on cross-module composition.

**Inputs/state:** Module behaviors, integration flow, and transactional invariant.

**Action:** Traces the invariant down and finds one inter-module path committing before validation.

**Does not:** Approve because each module is locally correct.

**Result/state change:** A cross-layer mismatch blocks the global guarantee until integration behavior changes.

**Companions:** ['parallel-qms', 'bidirectional-consistency', 'coherence-loops']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-05` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-05. Multi-Layer Consistency (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — T2-05. Multi-Layer Consistency (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.6 HQMS — Hierarchical QMS (historical_assistant_artifact)
