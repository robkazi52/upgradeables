# Evidence-Confidence Gate (`epistemic-status-gating@1.1.0`)

Recovered name: Epistemic Status Gating

Purpose: Keep mixed-certainty reasoning auditable and stop conclusions from laundering inference or hypothesis into fact.

Activate when: claims of mixed certainty are present.

Do not use when: the task contains only direct transformation with no inferential claims; labels would be exposed as private chain-of-thought rather than concise epistemic status.

Requires: none.

## Runtime mechanism

Represent material propositions with an explicit status drawn from factual, evaluative/inferential, framing, or hypothetical phases, plus their evidence pointer and topic. A downstream conclusion may consume a proposition only under rules appropriate to that status; unsupported status promotion is rejected or surfaced as uncertainty.

## Procedure

1. Split the candidate reasoning product into material propositions.
2. Assign each proposition a status and evidence pointer.
3. Check whether downstream conclusions use each status permissibly.
4. Flag any inference or hypothesis presented as direct fact.
5. Downgrade, relabel, remove, or seek evidence for the offending proposition.

## Guardrails

- Mandatory even on strong models: the distinction between source fact, inference, framing, and hypothesis.
- Conflict/precedence: Direct source evidence outranks an unlabeled model inference; A domain policy may define finer statuses but may not silently promote unsupported content.
- Stop or fail when: If a decision-critical proposition has no defensible status or evidence pointer, it cannot support the conclusion.

Full package and provenance: [`epistemic-status-gating`](../../upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md).
