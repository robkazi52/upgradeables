# Cross-Context Relationship Guard (`cross-context-resonance-lock@1.1.0`)

Recovered name: Cross-Context Resonance Lock

Purpose: Preserve an explicitly declared relationship between related contexts without blending their facts, authority, or unresolved assumptions.

Activate when: related contexts must stay aligned across a long task.

Do not use when: the contexts are unrelated; the relationship is speculative or would require merging incompatible authority domains.

Requires: none.

## Runtime mechanism

Modern operational interpretation: represent each context as a separately identified state with its own source and authority, then store only the declared relationship as a typed link between them. On update or synthesis, refresh the link if both endpoints still support it and reject transfers that copy unverified facts or authority across the boundary.

## Procedure

1. Identify each context, its source boundary, authority, and current state.
2. State the exact relationship that must remain aligned across contexts.
3. Store a typed link without copying the full contents of either context.
4. Revalidate both endpoints and the relationship when either context changes.
5. During synthesis, transfer only explicitly supported fields and preserve provenance.

## Guardrails

- Mandatory even on strong models: separate provenance and authority for every linked context.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If the relationship cannot be supported independently in both contexts, stop or escalate rather than forcing a nominal success.
- Stop or fail when: the relationship cannot be supported independently in both contexts; maintaining alignment would require transferring incompatible authority or unverified state.

Full package and provenance: [`cross-context-resonance-lock`](../../upgradeables/orchestration/cross-context-resonance-lock/UPGRADEABLE.md).
