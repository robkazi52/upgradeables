# Truth Priority Hierarchy (`truth-priority-hierarchy@1.1.0`)

Purpose: Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority.

Activate when: evidence classes or authorities conflict.

Do not use when: no material evidence or authority conflict exists; the domain lacks an authorized hierarchy and inventing one would decide the outcome.

Requires: none.

## Runtime mechanism

Before resolving a conflict, declare a domain-appropriate ordering such as host safety over task optimization, direct source fact over inference, and verified evidence over stylistic fluency. Map each conflicting claim to its evidence and authority class, apply the ordering, and preserve unresolved ties rather than silently choosing.

## Procedure

1. Identify the conflicting propositions or validator outcomes.
2. Record the source, authority, epistemic status, and domain applicability of each.
3. Load or declare the authorized domain hierarchy.
4. Apply the hierarchy and any hard vetoes.
5. Document the winning, narrowed, or unresolved result.

## Guardrails

- Mandatory even on strong models: evidence and authority, not fluency or optimization, determine conflict resolution.
- Conflict/precedence: Host/system safety and organization policy remain above repository-level truth ordering; If no authorized rule distinguishes materially conflicting claims, return unresolved rather than fabricate priority.
- Stop or fail when: If a material conflict has no defensible domain/authority ordering, the resolver must not select a winner.

Full package and provenance: [`truth-priority-hierarchy`](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md).
