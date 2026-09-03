# Adapter-First Experimentation — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Try semantic search in a repository skill loader.

## Why this Upgradeable activates

Search may improve discovery but could add latency and unstable ranking to a working deterministic loader.

## Inputs / state

The current resolver, a candidate search adapter, representative queries, and latency and precision thresholds are available.

## What it does

Routes a test cohort through the adapter, compares it with deterministic resolution, tests fallback, and promotes only the stable query interface after thresholds pass.

## What it does not do

Replace the base resolver before evaluation or let the adapter mutate registry records.

## Result / state change

Evidence-backed adoption or clean retirement with the original loader intact.

## Interaction with companion components

['architect-orchestrator', 'meta-stability']
