# Micro-Scaffolding — Behavioral Expectations

## Positive Activation

- **Given:** Numbers, citations, and conclusion must remain unchanged while prose changes.
- **Expect:** A clearer paragraph with all four invariants intact and no stale scaffold.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a one-step task has no fragile constraints
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Global task locks and source boundaries outrank a local scaffold.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Escalate when the required control cannot remain local or when the scaffold grows into a duplicate of the parent plan/state.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** identify the fragile local invariants
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A localized rewrite with four protected atoms and a larger StateBlock already present.
- **Expect:** Create a smaller temporary four-item control, preserve all atoms, then retire it after verification.
- **Reject:** Copy the whole StateBlock, omit local checkpoints, or carry the scaffold into unrelated work.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
