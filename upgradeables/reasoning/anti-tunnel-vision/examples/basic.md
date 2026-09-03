# Anti-Tunnel Vision — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A service is slow after a deployment.

## Why this Upgradeable activates

The team has fixated on the new database query although saturation and cache invalidation are also plausible.

## Inputs / state

Latency rose at deploy time; query timing, CPU saturation, and cache hit-rate data are available.

## What it does

Compares query regression against cache invalidation using the cheapest discriminating metrics, then selects the explanation supported by timing and cache data.

## What it does not do

List every imaginable outage cause or preserve the query hypothesis after contrary evidence.

## Result / state change

A bounded, evidence-selected diagnosis with one residual uncertainty noted.

## Interaction with companion components

['dominant-driver-isolation-scaffold', 'multiverse-reasoning']
