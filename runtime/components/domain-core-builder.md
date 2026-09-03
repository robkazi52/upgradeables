# Shared Domain Knowledge Component Builder (`domain-core-builder@1.1.0`)

Recovered name: Domain Core Builder

Purpose: Give multiple behaviors a shared, sourced domain substrate without duplicating knowledge across Genes or turning a Core into an OS.

Activate when: a recurring domain needs structured knowledge and decision logic.

Do not use when: the need is purely behavioral; the source corpus is too weak to support a domain model.

Requires: none.

## Runtime mechanism

Compile sourced domain material into the recovered Core fields: scope, entities and variables, reasoning map, required data, evidence hierarchy, decision logic, failure modes, canonical examples, Gene and validator interfaces, and version provenance. Keep prescriptive behavior in Genes, expose queries and typed outputs rather than dumping the entire Core into every task, and validate both source fidelity and interface sufficiency. The C-00 builder wrapper is a modern normalization of the recovered Core schema.

## Procedure

1. Define domain boundaries, target decisions, and excluded neighboring domains.
2. Inventory authoritative sources, entities, variables, required data, and uncertainty.
3. Build reasoning and evidence maps with provenance at the smallest maintainable units.
4. Encode decision logic, failure modes, and canonical examples without adding behavioral voice rules.
5. Declare query interfaces for Genes and validation interfaces for truth and citation checks.

## Guardrails

- Mandatory even on strong models: source provenance; evidence hierarchy; Core/Gene separation.
- Conflict/precedence: Source evidence outranks a convenient decision map; Conflicting authoritative sources remain represented with scope and uncertainty rather than silently merged.
- Stop or fail when: knowledge-behavior conflation; unsourced compression.

Full package and provenance: [`domain-core-builder`](../../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md).
