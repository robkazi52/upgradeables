# Unsupported Precision Gate (`specificity-penalty-gate@1.1.0`)

Recovered name: Specificity Penalty Gate

Purpose: Provide a conservative modern interpretation of the recovered name while keeping the historical source gap explicit.

Activate when: precise details may be plausible but unsupported.

Do not use when: exact values are directly provided and verified; a formal specification requires exactness and the evidence supports it.

Requires: none.

## Runtime mechanism

Tag specificity-bearing atoms—numbers, dates, named causes, unique identities, fine-grained scope, and certainty language—and compare each with the resolution of available evidence and actual task need. Unsupported precision receives a penalty that forces one of four actions: cite stronger evidence, widen to a supported range or class, label the detail provisional, or remove it. This scoring/gating procedure is not claimed as historical reconstruction.

## Procedure

1. Identify all atoms whose precision materially narrows the claim.
2. Record the evidence resolution and confidence for each atom.
3. Ask whether the task outcome requires that degree of precision.
4. Flag atoms more precise than evidence or need.
5. Resolve each flag by stronger evidence, supported generalization, explicit provisional labeling, or removal.

## Guardrails

- Mandatory even on strong models: support-versus-resolution comparison for generated dates, numbers, causes, and identities.
- Conflict/precedence: A verified decision-critical exact atom is not penalized merely for being specific; When evidence supports only a bound or category, that weaker form outranks a fluent point estimate.
- Stop or fail when: Do not release a material exact claim when the available evidence supports only a broader range, class, or uncertainty state.

Full package and provenance: [`specificity-penalty-gate`](../../upgradeables/validation/specificity-penalty-gate/UPGRADEABLE.md).
