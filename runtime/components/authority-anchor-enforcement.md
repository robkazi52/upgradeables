# Authority Anchor Enforcement (`authority-anchor-enforcement@1.1.0`)

Purpose: Bind consequential decisions and state changes to an explicit governing authority so lower-priority modules cannot silently override them.

Activate when: multiple instruction authorities coexist and may conflict.

Do not use when: the workflow has no competing instruction or authority layers; the governing authority cannot be identified from available context.

Requires: none.

## Runtime mechanism

Modern operational interpretation: record the governing authority, its scope, and the decisions it controls in explicit state. Before a module changes protected state or acts externally, compare the proposed action with that anchor. Reject, narrow, or escalate any action that depends on lower-priority text overriding the anchor; never infer missing authorization.

## Procedure

1. Identify the governing system, organizational, domain, and user authority relevant to the task.
2. Store each authority anchor with scope, protected decisions, and expiration or change conditions.
3. Require modules to attach their proposed state change or action to an applicable anchor.
4. Block or escalate proposals that exceed scope or conflict with higher authority.
5. Update an anchor only through an explicitly authorized change and record the transition.

## Guardrails

- Mandatory even on strong models: no protected decision changes without explicit governing authority.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If the governing authority or its scope is missing or contradictory, stop or escalate rather than forcing a nominal success.
- Stop or fail when: the governing authority or its scope is missing or contradictory; an equal-authority conflict has no declared resolution rule.

Full package and provenance: [`authority-anchor-enforcement`](../../upgradeables/orchestration/authority-anchor-enforcement/UPGRADEABLE.md).
