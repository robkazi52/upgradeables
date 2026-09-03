# Counterfactual Integrity Gate (`counterfactual-integrity@1.1.0`)

Purpose: Make counterfactual exploration safe and auditable by preserving an explicit boundary between factual, evaluative, framing, and hypothetical phases.

Activate when: counterfactual or hypothetical reasoning is used.

Do not use when: the task contains no hypothetical branch; the user explicitly requires purely factual extraction, where counterfactual-silence is the narrower control.

Requires: none.

## Runtime mechanism

Tag each proposition by semantic phase and keep hypothetical premises, derived consequences, and branch-local assumptions in a separate compartment. Any transfer from a hypothetical branch into factual state requires independent factual support; otherwise the proposition remains labeled hypothetical or is excluded from the factual output.

## Procedure

1. Declare the factual baseline and the allowed counterfactual question.
2. Tag introduced premises as hypothetical and retain their branch identity.
3. Derive consequences only inside that branch.
4. Check the draft for branch-local material presented without a hypothesis label.
5. Move a proposition into factual state only when independent evidence supports it.

## Guardrails

- Mandatory even on strong models: no hypothetical premise or consequence may silently become fact.
- Conflict/precedence: A factual-only task boundary overrides permission to explore counterfactuals; A stylistic request to write hypotheticals as certain cannot override phase labels.
- Stop or fail when: If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.

Full package and provenance: [`counterfactual-integrity`](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md).
