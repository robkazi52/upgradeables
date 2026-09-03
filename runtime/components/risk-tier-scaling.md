# Risk-Tier Scaling (`risk-tier-scaling@1.1.0`)

Purpose: Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling.

Activate when: task risk varies or must be classified.

Do not use when: a binding protocol already specifies the exact controls; the task is harmless and fully reversible.

Requires: none.

## Runtime mechanism

Classify the whole task and any higher-risk subregions using consequence, uncertainty, reversibility, scope of impact, and evidence quality. Map the result to explicit control floors: light single-path checks for routine work, stronger source and consistency checks for material work, and independent verification, hard vetoes, checkpointing, and fail-closed behavior for high-risk work. Reclassify when new evidence raises or lowers risk.

## Procedure

1. Identify potential harms, affected parties, uncertainty, reversibility, and blast radius.
2. Assign a risk tier to the task and separately to any exceptional subregion.
3. Select the tier's mandatory reasoning, evidence, independent-check, and veto controls.
4. Fund those controls through Cognitive Governor and route depth with DDA.
5. Reassess risk before irreversible action and whenever new evidence changes consequence or uncertainty.

## Guardrails

- Mandatory even on strong models: consequence and uncertainty assessment; high-risk independent checks; hard veto and fail-closed behavior.
- Conflict/precedence: A required tier cannot be lowered because of cost or deadline; When tier controls cannot be completed, return blocked or abstain.
- Stop or fail when: domain-label risk; budget-driven downgrading.

Full package and provenance: [`risk-tier-scaling`](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md).
