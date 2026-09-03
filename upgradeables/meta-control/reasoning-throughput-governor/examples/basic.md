# Reasoning Throughput Governor — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Generate and review profiles for 200 independent packages.

## Why this Upgradeable activates

Generation can run in parallel, but source review and schema validation can become bottlenecks.

## Inputs / state

Package dependencies, four worker slots, review capacity, error rates, and a fixed budget are known.

## What it does

Limits active package batches, keeps validation one batch behind, reduces concurrency when rework rises, and reports accepted profiles per hour.

## What it does not do

Launch all 200 at once or count unvalidated drafts as throughput.

## Result / state change

Steady validated output without queue or review collapse.

## Interaction with companion components

['cognitive-governor', 'dynamic-depth-allocation', 'meta-awareness']
