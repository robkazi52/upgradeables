# Adapter-First Experimentation — Behavioral Expectations

## Positive Activation

- **Given:** Search may improve discovery but could add latency and unstable ranking to a working deterministic loader.
- **Expect:** Routes a test cohort through the adapter, compares it with deterministic resolution, tests fallback, and promotes only the stable query interface after thresholds pass. Result: Evidence-backed adoption or clean retirement with the original loader intact.
- **Reject:** Omitting the mechanism or instead doing this: Replace the base resolver before evaluation or let the adapter mutate registry records.

## Negative Activation

- **Given:** the change is a mandatory security repair
- **Expect:** Remain inactive; do not begin the package-specific first step: State the hypothesis, acceptance metrics, test cohort, and non-negotiable invariants.
- **Reject:** Activating Adapter-First Experimentation solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Security and integrity repairs follow their mandated path rather than waiting for experimental promotion.
- **Expect:** Honor the conflict rule and preserve this invariant: keep the base path available during evaluation
- **Reject:** Silently violating the stated precedence for Adapter-First Experimentation

## Failure Boundary

- **Given:** base contamination
- **Expect:** Stop, narrow, abstain, or escalate while preserving: detachable boundary
- **Reject:** Claiming a successful Adapter-First Experimentation result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** detachable boundary
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A promising new capability may destabilize a working workflow.
- **Expect:** The skill creates an isolated adapter, keeps a base control and rollback, evaluates predeclared metrics, and gates promotion.
- **Reject:** The skill directly rewrites the base or calls an informal prototype sufficient evidence.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
