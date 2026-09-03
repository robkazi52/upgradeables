# Attention Compression Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** Full repository context exceeds the active workspace.
- **Expect:** A compact debug context that can be expanded back to authoritative files.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the original context is already small
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Zero-drift and source-fidelity requirements override compression goals.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not activate the compressed view when a protected fact, conflict, or provenance link is lost or unverifiable.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** protected-atom preservation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A large corpus containing an exact number, an unresolved contradiction, and source locations.
- **Expect:** Preserve the number verbatim, retain the contradiction, and attach reload pointers in a smaller view.
- **Reject:** Smooth away the contradiction or lose the exact number/source link.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
