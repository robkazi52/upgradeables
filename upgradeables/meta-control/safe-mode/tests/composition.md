# SAFE Mode — Behavioral Expectations

## Positive Activation

- **Given:** File changes and remote publication require exact state, credentials, and validation.
- **Expect:** Applies only planned changes, verifies tests and diff, confirms remote target and visibility, publishes, and checks the public URL. Result: A grounded public release or a precise fail-closed blocker.
- **Reject:** Omitting the mechanism or instead doing this: Invent credentials, redesign the repository during push, or claim publication before remote verification.

## Negative Activation

- **Given:** the primary need is broad architecture discovery
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare SAFE and load the committed plan, authoritative state, permitted delta, and risk controls.
- **Reject:** Activating SAFE Mode solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A missing required source, permission, or checkpoint blocks execution.
- **Expect:** Honor the conflict rule and preserve this invariant: lock state and scope
- **Reject:** Silently violating the stated precedence for SAFE Mode

## Failure Boundary

- **Given:** speculative execution
- **Expect:** Stop, narrow, abstain, or escalate while preserving: scope and state lock
- **Reject:** Claiming a successful SAFE Mode result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** scope and state lock
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A plan is selected and consequential execution must begin.
- **Expect:** The skill locks state and permitted delta, verifies prerequisites, executes atomically, checks results, and fails closed.
- **Reject:** The skill broadens alternatives like POWER, treats conservative as shallow, or continues on missing evidence.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
