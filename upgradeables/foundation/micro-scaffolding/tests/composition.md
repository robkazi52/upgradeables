# Micro-Scaffolding — Behavioral Expectations

## Positive Activation

- **Given:** Numbers, citations, and conclusion must remain unchanged while prose changes.
- **Expect:** Creates the four-item local checklist, rewrites, verifies each item, promotes no new global state, and retires the checklist. Result: A clearer paragraph with all four invariants intact and no stale scaffold.
- **Reject:** Omitting the mechanism or instead doing this: It does not reload the full paper, invent a new outline, or keep the checklist active for later sections.

## Negative Activation

- **Given:** a one-step task has no fragile constraints
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the current subtask and the specific failure risks within it.
- **Reject:** Activating Micro-Scaffolding solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Global task locks and source boundaries outrank a local scaffold.
- **Expect:** Honor the conflict rule and preserve this invariant: Keep the scaffold task-local and smaller than canonical workflow state.
- **Reject:** Silently violating the stated precedence for Micro-Scaffolding

## Failure Boundary

- **Given:** Escalate when the required control cannot remain local or when the scaffold grows into a duplicate of the parent plan/state.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: identify the fragile local invariants
- **Reject:** Claiming a successful Micro-Scaffolding result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** identify the fragile local invariants
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A localized rewrite with four protected atoms and a larger StateBlock already present.
- **Expect:** Create a smaller temporary four-item control, preserve all atoms, then retire it after verification.
- **Reject:** Copy the whole StateBlock, omit local checkpoints, or carry the scaffold into unrelated work.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
