# Immutable Content Zones (`zero-drift-zones@1.1.0`)

Recovered name: Zero-Drift Zones

Purpose: Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift.

Activate when: content contains fidelity-locked atoms.

Do not use when: the user explicitly authorizes change to the marked content; immutability scope cannot be identified.

Requires: none.

## Runtime mechanism

Identify minimal semantic atoms whose alteration would invalidate the task, assign stable IDs and source spans, and specify their preservation rule: exact text, exact value/unit, or meaning-equivalent statement with required qualifiers. Carry the IDs through all transforms and require a deterministic check or source-grounded review before acceptance.

## Procedure

1. Locate high-consequence atoms such as names, numbers, negations, conditions, quotations, obligations, and safety thresholds.
2. Minimize each zone so surrounding exposition can still change.
3. Choose exact-string, structured-value, or semantic-equivalence preservation rules.
4. Attach stable source pointers and propagate the zone contract downstream.
5. Validate every derivative and block or repair failures.

## Guardrails

- Mandatory even on strong models: minimal immutable atoms; qualifier/unit preservation; source pointers.
- Conflict/precedence: Latest authorized source correction may replace a zone, with version history retained; When exact wording and required target format conflict, preserve the semantic atom and surface the formatting exception for authority review.
- Stop or fail when: Block release when a required zone fails validation; Do not claim semantic equivalence where domain expertise or source context is insufficient.

Full package and provenance: [`zero-drift-zones`](../../upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md).
