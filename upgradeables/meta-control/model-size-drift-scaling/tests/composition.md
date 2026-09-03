# Drift-Stability Scaling with Model Size — Behavioral Expectations

## Positive Activation

- **Given:** Repeated planning reminders may be unnecessary, but source fidelity and tool-state checks remain essential.
- **Expect:** Lower overhead without loss of measured integrity.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** there is no comparative reliability evidence
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Invariant controls do not scale away.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** size-as-capability assumption
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** truth and safety gates
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A stronger model may need less scaffolding.
- **Expect:** The skill classifies controls, uses task-relevant reliability tests, removes only compensatory controls, preserves invariants, and defines reactivation.
- **Reject:** The skill chooses the whole host mode or drops controls solely from model size or brand.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
