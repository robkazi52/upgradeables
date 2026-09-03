# Clarification Gateway (`clarification-gateway@1.1.0`)

Purpose: Keep clarification proportional: ask only for materially blocking information, otherwise continue with the narrowest explicit assumption or bounded partial result.

Activate when: required variables are missing or instructions conflict.

Do not use when: the missing detail cannot change a valid result; the host forbids questions and a bounded assumption is safe.

Requires: none.

## Runtime mechanism

Classify each ambiguity by decision impact. If different plausible values would materially change correctness, authority, safety, or the requested deliverable, route to clarification when permitted. Otherwise choose the narrowest labeled assumption, preserve the unresolved field, or return the supported subset; do not turn every uncertainty into a user interruption.

## Procedure

1. Extract missing variables, ambiguous terms, and instruction conflicts before substantive execution.
2. For each item, compare plausible interpretations against the output contract and authority rules.
3. Mark an item blocking only when the interpretations lead to materially different valid actions or conclusions.
4. Ask one focused question for blocking items when interaction is available; otherwise state the narrow assumption or limit the result.
5. Record the answer or assumption in task state so the same ambiguity is not reopened without new evidence.

## Guardrails

- Mandatory even on strong models: materiality test; assumption labeling; authority-sensitive fallback.
- Conflict/precedence: A higher-authority instruction not to ask questions converts the gate into assumption selection, not permission to ignore ambiguity; If no safe bounded assumption exists for a consequential decision, return the supported subset or abstain.
- Stop or fail when: Stop or narrow when a required variable has multiple materially different interpretations and neither clarification nor a safe assumption is available.

Full package and provenance: [`clarification-gateway`](../../upgradeables/foundation/clarification-gateway/UPGRADEABLE.md).
