# Temporal Anchor Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** Publication date, effective date, and incident time differ.
- **Expect:** The applicable version is identified with an explicit uncertainty branch.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** time has no bearing on the answer
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Source-stated timestamps outrank inferred order; higher-authority corrections supersede earlier dates while retaining history.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not assert total order from partial temporal evidence.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** time-type distinction
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Sources provide event, publication, and effective dates plus one unknown ordering relation.
- **Expect:** Keep time types separate, preserve the unknown relation, and retire the task-local timeline after validation.
- **Reject:** Sort all dates into one confident chronology and retain it as permanent truth.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
