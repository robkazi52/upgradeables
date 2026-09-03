# External State Automation — Behavioral Expectations

## Positive Activation

- **Given:** Verified decisions and source pointers need durable continuation.
- **Expect:** Writes the compact snapshot to an authorized file, verifies it, and validates it on resume. Result: The next session restores traceable state or receives an explicit failure/staleness warning.
- **Reject:** Omitting the mechanism or instead doing this: Does not claim persistence before the write succeeds or store the whole conversation by default.

## Negative Activation

- **Given:** the task ends in one session and needs no continuation
- **Expect:** Remain inactive; do not begin the package-specific first step: Confirm an authorized storage mechanism, location, lifetime, and data policy.
- **Reject:** Activating External State Automation solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** Honor the conflict rule and preserve this invariant: Preserve the defining invariant: capability declaration, minimum-state serialization, write verification, and restore validation.
- **Reject:** Silently violating the stated precedence for External State Automation

## Failure Boundary

- **Given:** no authorized storage capability is available
- **Expect:** Stop, narrow, abstain, or escalate while preserving: capability declaration, minimum-state serialization, write verification, and restore validation
- **Reject:** Claiming a successful External State Automation result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** capability declaration, minimum-state serialization, write verification, and restore validation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a task must continue across sessions using an actual storage system
- **Expect:** state is minimally serialized, written, verified, restored, and reconciled
- **Reject:** claiming memory without a real write or storing unbounded conversation data

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
