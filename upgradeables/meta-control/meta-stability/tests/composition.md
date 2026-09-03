# Meta-Stability Mode — Behavioral Expectations

## Positive Activation

- **Given:** Repeated changes and divergent state threaten global coherence.
- **Expect:** Freezes new edits, compares each diff to the passing state, quarantines conflicting changes, rebuilds one authoritative state, validates it, then resumes changes sequentially. Result: One coherent baseline and a controlled resume queue.
- **Reject:** Omitting the mechanism or instead doing this: Delete all recent work or keep launching more repair agents.

## Negative Activation

- **Given:** one local defect can be repaired directly
- **Expect:** Remain inactive; do not begin the package-specific first step: Confirm an instability trigger such as state divergence, repeated regression, or unresolved module conflict.
- **Reject:** Activating Meta-Stability Mode solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A user-approved newer decision is not rolled back solely because an older checkpoint is internally coherent.
- **Expect:** Honor the conflict rule and preserve this invariant: preserve the last verified checkpoint
- **Reject:** Silently violating the stated precedence for Meta-Stability Mode

## Failure Boundary

- **Given:** stability theater
- **Expect:** Stop, narrow, abstain, or escalate while preserving: verified checkpoint
- **Reject:** Claiming a successful Meta-Stability Mode result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** verified checkpoint
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Repeated changes and module conflicts cause state versions to diverge.
- **Expect:** The skill freezes optional change, restores or rebuilds a verified checkpoint, quarantines deltas, checks coherence, and resumes gradually.
- **Reject:** The skill only retries the failed action, enters SAFE, or permanently halts work.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
