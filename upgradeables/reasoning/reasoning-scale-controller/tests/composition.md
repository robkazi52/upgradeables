# Reasoning-Scale Controller — Behavioral Expectations

## Positive Activation

- **Given:** The surrounding artifact is large, but the actual defect is local and source-verifiable.
- **Expect:** A proportional local correction with an explicit escalation condition.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a governing workflow already fixes the required scale
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Risk-mandated review overrides the desire to stay at a cheaper scale.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** scale theater
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** smallest-adequate-scope selection
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A large artifact contains a narrow defect but might hide broader dependencies.
- **Expect:** The skill chooses a local scale, states the signal for escalation, and returns from any global review to local execution.
- **Reject:** The skill always applies maximum depth or treats scale names as decorative labels.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
