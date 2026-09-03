# Multi-Layer Consistency (`multi-layer-consistency@1.1.0`)

Purpose: Maintain vertical consistency from local facts and operations to the overall conclusion or system behavior.

Activate when: multiple authority layers are composed.

Do not use when: the artifact has only one meaningful level; levels are intentionally alternative rather than nested.

Requires: none.

## Runtime mechanism

Define nested levels and invariants linking them, then validate both upward and downward: atoms must support their containing unit, units must compose into section or subsystem claims, and the global result must not assert anything contradicted below; conversely global constraints must be realized in the relevant lower layers. A pass requires agreement across boundaries, not independent passes at each level.

## Procedure

1. Map the artifact into atom, local unit, intermediate group, and global levels.
2. State invariants and claimed summaries at each boundary.
3. Check upward support from atoms to local and global claims.
4. Check downward realization of global constraints in lower levels.
5. Locate contradictions, orphan claims, and locally valid but globally incompatible parts.

## Guardrails

- Mandatory even on strong models: at least one upward and one downward boundary check in hierarchical work.
- Conflict/precedence: A lower-level verified contradiction defeats an unsupported global summary; An explicit global hard constraint requires lower-layer implementation or a documented exception.
- Stop or fail when: Do not certify when a global claim lacks lower-layer support or a lower-layer fact violates an undeclared global exception.

Full package and provenance: [`multi-layer-consistency`](../../upgradeables/validation/multi-layer-consistency/UPGRADEABLE.md).
