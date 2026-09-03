# Fermionic Veto Strengthening — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Five validators score a deployment highly, but one finds that rollback is impossible under the stated safety policy.

## Why this Upgradeable activates

Rollback capability is a declared non-compensable condition.

## Inputs / state

Validator reports, policy predicate, and deployment plan.

## What it does

Vetoes deployment and requires a tested rollback path before rescoring.

## What it does not do

Approve because four of five validators passed.

## Result / state change

The candidate remains quarantined until the fatal condition is removed.

## Interaction with companion components

['fail-closed-abstention', 'parallel-qms', 'multi-truth-gating']
