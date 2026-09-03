# Task Resolution

Input:

```text
Review this pull request for breaking changes to the exported Python API. Do not edit files.
```

Deterministic result, abridged for readability:

```text
Archetype: evaluation-audit
Subtype: code-review
Execution: direct-response
Complexity: L1-L2 (bounded review-only task)
Primary recipe: code-review
Required by recipe: grounding-no-invention, scoped-loader, task-set-lock-in
Conditional: citation-fidelity, critical-atomic-verification,
  fail-closed-abstention, invariance-stress-scaffold, stateblock
Excluded: parallel-qms (minimum L3 exceeds the L2 ceiling)
Authority: review only; no editing requested
```

This is selection output, not automatic activation. The completed project Skill
keeps the smallest composition justified by the concrete API contract and drops
unneeded candidates.
