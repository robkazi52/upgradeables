# Domain-Normalized Drift Field — Behavioral Expectations

## Positive Activation

- **Given:** The artifact crosses a precision domain and a low-stakes expressive region.
- **Expect:** Domain-appropriate drift limits across one mixed artifact.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** domain is ambiguous and stakes are high
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Explicit task/source authority outranks the domain profile.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not select a permissive profile when domain classification or consequence is uncertain.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** consequence assessment
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** The same paraphrase operation is applied to legal obligations and fictional dialogue.
- **Expect:** Choose different domain baselines, then refine them with task-specific corridors.
- **Reject:** Use one universal tolerance or treat the domain default as overriding explicit instructions.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
