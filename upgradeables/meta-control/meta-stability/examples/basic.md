# Meta-Stability Mode — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Several agents edit a registry from different state versions and validations alternate between two failures.

## Why this Upgradeable activates

Repeated changes and divergent state threaten global coherence.

## Inputs / state

A last passing commit, agent diffs, current registry, and authority rules are available.

## What it does

Freezes new edits, compares each diff to the passing state, quarantines conflicting changes, rebuilds one authoritative state, validates it, then resumes changes sequentially.

## What it does not do

Delete all recent work or keep launching more repair agents.

## Result / state change

One coherent baseline and a controlled resume queue.

## Interaction with companion components

['stateblock', 'coherence-heartbeat', 'meta-supervisor']
