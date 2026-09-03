# Protected-Constraint Robustness Test (`invariance-stress-scaffold@1.1.0`)

Recovered name: Invariance Stress Scaffold

Purpose: Operationalize the recovered name without pretending the original January 2026 mechanics were recovered.

Activate when: a patch or rewrite must preserve invariants.

Do not use when: the transformed feature is itself decision-relevant; the invariants cannot be stated.

Requires: none.

## Runtime mechanism

Define the properties claimed invariant, generate a small controlled set of transformations that should preserve those properties—such as reordering independent facts, paraphrasing without modal change, or changing irrelevant formatting—and compare outputs. Any decision-relevant change is reported as sensitivity; this is a modern stress-test interpretation, not a recovered historical algorithm.

## Procedure

1. State the claimed invariant and observable pass condition.
2. Separate semantics-preserving perturbations from meaning-changing controls.
3. Construct a bounded perturbation set and preserve provenance.
4. Run the task independently on original and perturbed inputs.
5. Compare conclusions, confidence, constraints, and safety behavior.

## Guardrails

- Mandatory even on strong models: explicit invariant and at least one controlled counterfactual comparison when robustness is claimed.
- Conflict/precedence: Meaning-changing controls are not invariant breaches; Safety behavior must remain at least as conservative under semantics-preserving perturbations.
- Stop or fail when: Do not claim robustness when decision-relevant output changes under a justified semantics-preserving perturbation.

Full package and provenance: [`invariance-stress-scaffold`](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md).
