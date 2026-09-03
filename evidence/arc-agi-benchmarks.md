# ARC-AGI Benchmark Report

## Status and provenance

This is an author-reported retrospective summary from a 214-turn April 2025
experimental session titled “Token masking for selective document reasoning.”
The linked [source chat](https://claude.ai/chat/290987c7-34cf-444f-9e66-d1ce70970519)
was not accessible for independent verification during repository integration.
No raw run artifacts or grader are included, so the figures below are reported
observations, not independently verified benchmark results.

The archived [integration handoff](../archive/build-spec/CODEX_HANDOFF_UPGRADEABLES.md)
states that all data came from April 2025. That cannot describe runs on all named
models as written: Anthropic's announcements date
[Claude Sonnet 4 to May 2025](https://www.anthropic.com/news/activating-asl3-protections),
[Claude Haiku 4.5 to October 2025](https://www.anthropic.com/news/claude-haiku-4-5),
and [Claude Opus 4.6 to February 2026](https://www.anthropic.com/news/claude-opus-4-6).
The session date, run dates, or later retrospective additions require correction
before results can be attributed to these versions.

The handoff describes six prompt versions (v2–v6), Claude Sonnet 4, Opus 4.6,
and Haiku 4.5, with one response per prompt and no refinement or code execution.
It reports cell-level auto-grading and defines a solved task as 100% cell accuracy.

## Reconciliation warning

The supplied ARC-AGI-1 summaries conflict with the supplied row table:

- Narrative: 13 of 25 tasks solved by at least one model and 23 of 75 runs solved.
- Model summary: 8 Sonnet + 10 Opus + 15 Haiku = 33 solved runs.
- Counting checkmarks in the supplied table: 14 tasks solved by at least one
  model and 31 solved runs (9 Sonnet, 10 Opus, 12 Haiku).

The statement that Haiku uniquely solved four tasks also names only three in the
table. Until raw results resolve these discrepancies, do not aggregate these data,
claim a 52% solve rate as verified, or derive a 3–10× improvement factor.

## Supplied ARC-AGI-1 row table

| Task | Grid size | Sonnet | Opus | Haiku | Supplied status |
|---|---|:---:|:---:|:---:|:---:|
| Largest Rect | 2×2 | ✓ | ✓ | ✓ | Yes |
| Scatter→Grid | 3×3 | ✓ | ✓ | ✓ | Yes |
| Shape Compare | 3×3 | — | ✓ | ✓ | Yes |
| Scatter→Grid2 | 3×3 | — | — | ✓ | Yes |
| De-tile | 4×3 | ✓ | ✓ | ✓ | Yes |
| Mirror (6×3) | 6×3 | — | — | ✓ | Yes |
| AND Compare | 5×4 | ✓ | ✓ | ✓ | Yes |
| Replace Color | 6×4 | — | — | ✓ | Yes |
| 4-Rotate Tile | 6×6 | ✓ | — | — | Yes |
| Peel Layers | 6×6 | — | ✓ | — | Yes |
| Mirror4 | 6×6 | ✓ | ✓ | ✓ | Yes |
| Cross Extend | 6×6 | ✓ | ✓ | ✓ | Yes |
| Fill+Extend | 10×10 | ✓ | ✓ | ✓ | Yes |
| Keep Center Col | 7×7 | ✓ | ✓ | ✓ | Yes |
| 180° Rotate | 3×3 | — | — | — | No |
| Transpose | varies | — | — | — | No |
| Extract Shape | varies | — | — | — | No |
| Sudoku Fill | varies | — | — | — | No |
| Mirror Tile | varies | — | — | — | No |
| L-Line | varies | — | — | — | No |
| NOR Gate | 4×4 | — | — | — | No |
| Double Shape | 3×6 | — | ✓ | — | Partial |
| OR Gate | 4×5 | — | — | — | No |
| Checkerboard | 6×6 | — | — | — | No |
| 180° Blocks | 7×7 | — | — | — | No |

The handoff separately supplied model totals of Sonnet 8/25 (32%), Opus 10/25
(40%), and Haiku 15/25 (60%). These are retained as source claims but conflict
with the checkmark counts above.

## Supplied ARC-AGI-2 results

The handoff reports zero exact task solves across five tasks. It supplied these
best cell accuracies:

| Task | Reported no-OS result | Best prompt | Reported best | Model |
|---|---:|---|---:|---|
| Nested Borders | 90% | v5+ | 97% | Haiku |
| Ring Swap | 84% | v4 | 94% | Opus |
| Compass Pull | 94% | v4 | 98% | Opus |
| Corner Extend | 89% | v5+ | 92% | Haiku |
| Spiral Collapse | 69% | v5+ | 95% | Opus |

The corresponding reported within-session differences were +7, +10, +4, +3,
and +26 percentage points. “No OS” is the session comparator, not an externally
reproduced base-LLM benchmark.

The handoff variously summarizes ARC-AGI-2 cell accuracy as 88–98% and 82–98%,
while the complete version table spans 67–98% and the best-per-task table spans
92–98%. It also appears to compare an approximately 0% **exact task solve rate**
with 69–94% **cell accuracy**. Those metrics are not interchangeable.

### Supplied prompt-version comparison

| Task | v2 | v3 | v4 | v5 Base | v5+ | v6 |
|---|---:|---:|---:|---:|---:|---:|
| Nested Borders | 93% | 91% | 95% | 95% | **97%** | 96% |
| Ring Swap | 90% | 88% | **94%** | 93% | 94% | 84% |
| Compass Pull | 93% | 93% | **98%** | 93% | 94% | 93% |
| Corner Extend | 92% | 92% | 90% | 90% | **92%** | 90% |
| Spiral Collapse | 79% | 79% | 82% | 67% | **95%** | 76% |

## Preliminary design signal

Within this small reported sample, the directive-oriented v5+ prompt matched or
exceeded the more elaborate v4 prompt on three of five ARC-AGI-2 tasks. This is a
hypothesis-generating observation, not proof that directives generally outperform
structured prompts. It motivates testing three focused controls:

1. Anti-failure rules naming a concrete error to avoid.
2. Falsification before committing to a transformation rule.
3. Stepwise output construction with local verification.

Reported failure analysis suggests scaffolding may help when a rule is discoverable
but application discipline is weak. It cannot supply spatial insight absent from
the model, remove context limits, or guarantee correct execution.

## Reproduction gaps

Required before treating the result as a reproducible benchmark: exact ARC task
IDs and split, prompt texts/hashes, model snapshots, inference parameters, raw
responses, grid parser, grader source, retry policy, per-run results, contamination
analysis, and citations for any external baseline comparison.
