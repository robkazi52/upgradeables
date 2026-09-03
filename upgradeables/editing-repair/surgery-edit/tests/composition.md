# Surgery Editing — Behavioral Expectations

## Positive Activation

- **Given:** The change alters selection, dependency resolution, package interfaces, and state migration across the repository.
- **Expect:** Maps every loader responsibility, designs registry adapters, migrates callers in stages, validates resolution and fallback, then removes the monolith after cutover checks. Result: One coherent loader architecture with migrated dependents and an auditable retirement.
- **Reject:** Omitting the mechanism or instead doing this: Patch conditionals into the old loader until it accidentally behaves like two architectures.

## Negative Activation

- **Given:** a localized invariant-preserving patch suffices
- **Expect:** Remain inactive; do not begin the package-specific first step: Document the architecture-level failure and evidence that local editing is insufficient.
- **Reject:** Activating Surgery Editing solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Use CRISPR when all required behavior can coexist with current interfaces inside a bounded patch.
- **Expect:** Honor the conflict rule and preserve this invariant: prove macro scope
- **Reject:** Silently violating the stated precedence for Surgery Editing

## Failure Boundary

- **Given:** macro edit disguised as patch accumulation
- **Expect:** Stop, narrow, abstain, or escalate while preserving: CRISPR-insufficiency proof
- **Reject:** Claiming a successful Surgery Editing result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** CRISPR-insufficiency proof
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A requested change reorganizes layers and breaks several current interfaces.
- **Expect:** The skill proves local insufficiency, inventories interfaces, maps responsibilities, stages migration and rollback, validates cutover, and retires the old path.
- **Reject:** The skill applies an expanding local patch, produces only a new diagram, or removes the old structure before dependents pass.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
