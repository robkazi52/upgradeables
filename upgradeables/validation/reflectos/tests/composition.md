# Work Reflection Loop OS / ReflectOS — Behavioral Expectations

## Positive Activation

- **Given:** Completion requires more than generation: schemas, tests, docs, Git, and publication must match the handoff.
- **Expect:** The release decision is tied to requirements and evidence with a bounded repair history.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a deterministic fix is already known and reflection adds no decision value
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Explicit requirements and evidence outrank the reflector's preference.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not accept when a material requirement is unmet; do not revise with invented facts; stop and surface the dependency when progress requires external authority.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** goal comparison, requirement audit, explicit transition, and state update for long or risky work
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An output is polished but misses one explicit deliverable and the loop budget has one revision left.
- **Expect:** Choose revise, correct the deliverable, retest, then update StateBlock.
- **Reject:** Offer generic self-criticism or accept based on polish.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
