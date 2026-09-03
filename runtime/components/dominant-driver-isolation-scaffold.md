# Dominant-Driver Isolation Scaffold (`dominant-driver-isolation-scaffold@1.1.0`)

Purpose: Separate high-leverage causes or constraints from correlated, downstream, or low-impact factors.

Activate when: many plausible causes compete for priority.

Do not use when: the system is known to require irreducibly joint causes; available evidence supports only correlation.

Requires: none.

## Runtime mechanism

Modern conservative interpretation: enumerate candidate drivers, define the target outcome, estimate each candidate's unique explanatory or intervention leverage, and test the leading driver against the strongest alternative and interaction effects. The historical sources recover only the scaffold's exact name.

## Procedure

1. Define the outcome and the time or system boundary.
2. List candidate drivers and distinguish causes, constraints, symptoms, and proxies.
3. Estimate each candidate's marginal effect using available comparisons, traces, or counterfactuals.
4. Test the leader against the strongest rival and check whether a pairwise interaction changes the ranking.
5. Select the dominant driver or report that no single driver is defensible; route effort accordingly.

## Guardrails

- Mandatory even on strong models: rival test; interaction check; causal-evidence label.
- Conflict/precedence: A safety-critical factor is not discarded solely because its probability or average effect is lower; If interaction terms dominate marginal effects, return a coupled-driver result rather than forcing one winner.
- Stop or fail when: correlation presented as cause; single-factor oversimplification.

Full package and provenance: [`dominant-driver-isolation-scaffold`](../../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md).
