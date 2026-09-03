# HYBRID Mode — Behavioral Expectations

## Positive Activation

- **Given:** Several architectures deserve exploration, but repository edits and publication require precise validated execution.
- **Expect:** Uses POWER for three architectures, collapses to one, records interfaces and rejected assumptions, then switches to SAFE for file edits, tests, and publication. Result: Broad design quality with a controlled, auditable execution path.
- **Reject:** Omitting the mechanism or instead doing this: Mix components from losing designs during implementation without reopening the design gate.

## Negative Activation

- **Given:** the task needs only narrow execution
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare HYBRID and define separate planning and execution completion criteria.
- **Reject:** Activating HYBRID Mode solely because its name appears relevant

## Precedence Or Conflict

- **Given:** No POWER branch may execute until one plan passes collapse and handoff validation.
- **Expect:** Honor the conflict rule and preserve this invariant: declare the active phase
- **Reject:** Silently violating the stated precedence for HYBRID Mode

## Failure Boundary

- **Given:** mode leakage
- **Expect:** Stop, narrow, abstain, or escalate while preserving: explicit collapse
- **Reject:** Claiming a successful HYBRID Mode result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit collapse
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A task needs broad design and consequential execution.
- **Expect:** The skill runs explicit POWER planning, collapse, supervised state handoff, then SAFE execution with a gated return path.
- **Reject:** The skill merely averages exploratory and conservative behavior or switches modes implicitly.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
