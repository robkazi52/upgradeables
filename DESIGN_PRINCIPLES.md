# Design Principles

## When scaffolding may help most

Current exploratory evidence suggests useful hypotheses, not universal laws.
Upgradeable composition is worth testing when:

- a smaller model can identify an approach but loses execution discipline;
- early commitment to a plausible wrong hypothesis is the observed failure;
- multi-step work drops constraints or state; or
- a task has checkable local invariants that catch execution errors.

It is less likely to help when:

- the task is already reliably within the host model's capability;
- success requires an insight or sensory capability the host lacks;
- the task is simple and single-step; or
- context/token limits dominate regardless of instruction structure.

Prefer short directives that target an observed failure over an elaborate simulated
operating system. Add state, iteration, orchestration, or validation only when its
distinctive mechanism has an active trigger. As models improve, retain specialized
invariants and remove scaffolding the host can already satisfy reliably.

These are design hypotheses informed by the preliminary reports in
[`evidence/`](evidence/). They require broader, reproducible evaluation and must
not be presented as proof of model improvement.
