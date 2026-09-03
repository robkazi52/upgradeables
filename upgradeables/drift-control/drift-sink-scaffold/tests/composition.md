# Drift Sink Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The branch consumes attention and contaminates new summaries.
- **Expect:** Places the theory in a reversible task-local sink with its disproof, pointer, and restore condition. Result: Automatic retrieval stops resurfacing the disproven branch while auditability remains.
- **Reject:** Omitting the mechanism or instead doing this: It does not delete the branch or sink unresolved evidence that challenges the current theory.

## Negative Activation

- **Given:** the branch is unresolved rather than rejected
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify a branch that repeatedly causes drift and classify it as superseded, rejected, irrelevant, or low-authority.
- **Reject:** Activating Drift Sink Scaffold solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Higher-authority evidence or audit obligations can force restoration.
- **Expect:** Honor the conflict rule and preserve this invariant: make quarantine reversible
- **Reject:** Silently violating the stated precedence for Drift Sink Scaffold

## Failure Boundary

- **Given:** Do not quarantine unresolved contrary evidence or safety-critical information.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: reversibility
- **Reject:** Claiming a successful Drift Sink Scaffold result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** reversibility
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A formally superseded branch repeatedly re-enters active retrieval but must remain auditable.
- **Expect:** Quarantine it reversibly with authority, provenance, dependencies, and a restore trigger, then retire the local scaffold at task end.
- **Reject:** Delete it, hide contrary evidence, or claim an undocumented ECL algorithm.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
