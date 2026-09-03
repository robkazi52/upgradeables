# Stuck-Pattern Reset Pack — Behavioral Expectations

## Positive Activation

- **Given:** The method and corpus are unchanged despite different wording.
- **Expect:** A materially different recovery path or an explicit source blocker.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a second attempt has new evidence or a materially changed method
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Locked facts and constraints survive the reset.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** false loop detection
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** trusted-state preservation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Several attempts fail with the same assumptions, method, state, and result despite different wording.
- **Expect:** The skill preserves locked state, quarantines only the failed path, chooses a materially different method, and bounds the retry.
- **Reject:** The skill clears the whole context, repeats cosmetic variants, or enters a global stability freeze.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
