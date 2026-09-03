# Non-Authoritative Branch Suppression (`non-authoritative-branch-suppression@1.1.0`)

Purpose: Prevent attractive but non-governing alternatives from overriding the authoritative task branch.

Activate when: obsolete alternatives conflict with locked decisions.

Do not use when: authority is unresolved; a lower-authority branch contains material contrary evidence that must be evaluated.

Requires: none.

## Runtime mechanism

A modern authority-gating interpretation is to label branches by source, authority, status, scope, and version; only the currently authorized branch may supply operative instructions or state. Other branches remain available as evidence or alternatives but are excluded from action selection, and any promotion requires an explicit authority/version transition.

## Procedure

1. Enumerate branches that could influence the next action.
2. Attach provenance, authority level, status, scope, and version to each.
3. Select the operative branch using the declared authority hierarchy.
4. Mask non-authoritative branches from instruction and state mutation paths while retaining relevant evidence access.
5. Before action, verify that every governing premise traces to the operative branch.

## Guardrails

- Mandatory even on strong models: instruction-versus-evidence distinction; provenance and version; explicit promotion.
- Conflict/precedence: System, explicit task, and declared source authority order govern branch selection; topical relevance never creates authority; When authority is tied or unclear and the outcome matters, preserve branches and request adjudication.
- Stop or fail when: Do not suppress unresolved contrary evidence or fabricate an authority ranking; Treat the distinctive mechanism as provisional pending recovery of original documentation.

Full package and provenance: [`non-authoritative-branch-suppression`](../../upgradeables/drift-control/non-authoritative-branch-suppression/UPGRADEABLE.md).
