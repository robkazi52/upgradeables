# Constraint Puzzle Benchmark Report

## Status

This is an author-reported retrospective observation from the same April 2025
session described in the [evidence index](README.md). The puzzle, prompts, raw
outputs, grader, and per-run records are not archived, so the result is not yet
independently auditable.

## Reported experiment

A logical constraint puzzle with nine or more reasoning hops, conditional rules,
arithmetic inference, and combinatorial propagation was tried with:

1. A plain task description.
2. A phased chain-of-knowledge prompt.
3. A code-shaped “Solver OS v2” with commit/veto terminology, tracked domains,
   bounded propagation, deferred condition evaluation, and a QMS gate.

The handoff reports that all three strategies reached 100% on Sonnet, making that
model/task pairing non-discriminating. It also reports that scaffolding enabled
Haiku to solve constraints missed with the plain prompt, but supplies no run count
or score table. Treat that result as a qualitative observation until artifacts are
available.

## Claimed diagnostic step

The reported puzzle required combining `Alice + Bob = 8`, `Alice > 5`, and “Bob
is odd” to infer Alice = 7 and Bob = 1. The session interpretation was that
explicit commitment and bounded propagation discouraged a plausible-sounding
jump over this arithmetic step.

## What this study can and cannot support

It can motivate a preregistered comparison of explicit state/verification against
a plain prompt on weaker models. It cannot establish causality, generalization,
or a model-capability compensation effect without the missing puzzle, outputs,
grader, repetitions, and scoring data.
