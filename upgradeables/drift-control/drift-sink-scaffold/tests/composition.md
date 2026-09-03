# Drift Sink Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The branch consumes attention and contaminates new summaries.
- **Expect:** Automatic retrieval stops resurfacing the disproven branch while auditability remains.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the branch is unresolved rather than rejected
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Higher-authority evidence or audit obligations can force restoration.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not quarantine unresolved contrary evidence or safety-critical information.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** reversibility
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A formally superseded branch repeatedly re-enters active retrieval but must remain auditable.
- **Expect:** Quarantine it reversibly with authority, provenance, dependencies, and a restore trigger, then retire the local scaffold at task end.
- **Reject:** Delete it, hide contrary evidence, or claim an undocumented ECL algorithm.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
