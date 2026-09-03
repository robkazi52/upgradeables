# State Snapshot — Behavioral Expectations

## Positive Activation

- **Given:** The second session must know exactly which sources and claims were accepted at handoff.
- **Expect:** Freezes those fields with integrity and predecessor metadata, then verifies new events on restore. Result: The review resumes from a reproducible checkpoint.
- **Reject:** Omitting the mechanism or instead doing this: It does not treat the copy as live or omit unresolved questions.

## Negative Activation

- **Given:** a snapshot would persist prohibited sensitive data
- **Expect:** Remain inactive; do not begin the package-specific first step: Choose a transaction-safe checkpoint.
- **Reject:** Activating State Snapshot solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A newer validated canonical state outranks an older snapshot.
- **Expect:** Honor the conflict rule and preserve this invariant: freeze an identified state version
- **Reject:** Silently violating the stated precedence for State Snapshot

## Failure Boundary

- **Given:** Do not restore when integrity, task identity, or schema compatibility cannot be established.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: immutable version identity
- **Reject:** Claiming a successful State Snapshot result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** immutable version identity
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Live state may change after an agent handoff begins.
- **Expect:** Freeze and identify one validated version, then reconcile later events on resume.
- **Reject:** Copy an unversioned mutable summary and call it current state.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
