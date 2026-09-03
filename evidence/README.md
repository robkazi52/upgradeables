# Empirical Evidence

These are informal experiments from the repository author's own chats. Treat
them as ideas to try, challenge, and reproduce—not as a paper or a product claim.

This directory records experiments reported by the repository author. It is
separate from canonical Upgradeable definitions: a benchmark result may inform a
recipe, but it cannot rewrite historical provenance or prove a universal model
improvement.

## Evidence maturity

The current studies are **preliminary retrospective reports** from a 214-turn
April 2025 session. The source chat is linked, but raw prompts, task identifiers,
per-run outputs, grader code, decoding parameters, and immutable result files have
not yet been archived here. The results therefore have not been independently
reproduced and must not be described as a controlled public benchmark.

The ARC handoff also contains unreconciled totals. The evidence page preserves
the supplied values and identifies the discrepancies rather than choosing a
preferred number.

The handoff dates all results to April 2025 while naming model releases announced
later. That chronology is unresolved and blocks attribution of the reported runs
to those model versions.

## Studies

- [ARC-AGI benchmark report](arc-agi-benchmarks.md) — reported one-shot prompt
  scaffolding experiments on ARC-AGI-1 and ARC-AGI-2 grid puzzles.
- [Constraint puzzle report](constraint-puzzle-benchmarks.md) — reported
  multi-hop logical reasoning with three prompt strategies.

## Contribution standard

Future studies should archive a dataset/task manifest, prompts or prompt hashes,
model and parameter identifiers, raw outputs, grader implementation, per-run
results, dates, and a reproducible aggregation command. Separate exploratory,
confirmatory, and independently reproduced results.
