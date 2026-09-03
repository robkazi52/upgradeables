# SAFE Mode — Behavioral Expectations

## Positive Activation

- **Given:** File changes and remote publication require exact state, credentials, and validation.
- **Expect:** A grounded public release or a precise fail-closed blocker.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the primary need is broad architecture discovery
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A missing required source, permission, or checkpoint blocks execution.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** speculative execution
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** scope and state lock
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A plan is selected and consequential execution must begin.
- **Expect:** The skill locks state and permitted delta, verifies prerequisites, executes atomically, checks results, and fails closed.
- **Reject:** The skill broadens alternatives like POWER, treats conservative as shallow, or continues on missing evidence.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
