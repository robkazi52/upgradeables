# QMS Variants

| Source ID | Mode | Name | Operational interpretation |
|---|---|---|---|
| `PQ-01` | `mirror` | Mirror QMS | Run mirrored independent checks and compare results. |
| `PQ-02` | `risk-tier-split` | Risk-Tier-Split QMS | Apply evaluative depth and criteria by risk tier. |
| `PQ-03` | `cross-phase` | Cross-Phase QMS | Check separation across factual, evaluative, framing, and hypothetical phases. |
| `PQ-04` | `redundancy` | Redundancy-QMS | Use independent validation passes with veto or abstention capability. |
| `PQ-05` | `exit-integrated` | ExIt-Integrated QMS | Combine scoring with bounded refinement and convergence. |
| `PQ-06` | `hierarchical` | Hierarchical QMS | Check atomic, section, and global consistency. |
| `PQ-07` | `transversal` | Transversal QMS | Check temporal, causal, logical, and modal dimensions. |
| `PQ-08` | `heterogeneous` | Heterogeneous QMS | Apply different evaluator perspectives to the same candidate. |
| `PQ-09` | `monte` | Monte QMS | Perturb assumptions and test stability; this is not formal Monte Carlo unless sampling is implemented. |
| `PQ-10` | `inversion` | Inversion QMS | Test whether a conclusion's implied evidence is actually present. |
| `PQ-11` | `conflict-resolution` | Conflict-Resolution QMS | Resolve evaluator or evidence conflicts with explicit priority rules. |
| `PQ-12` | `distributed` | Distributed QMS | Use real isolated evaluators when available, otherwise label independent sequential passes honestly. |
| `PQ-13` | `meta` | Meta-QMS | Evaluate the quality and agreement of other QMS evaluations. |
| `PQ-14` | `semantic-glass-box` | Semantic Glass-Box QMS | Emit an auditable semantic pass/fail map instead of only a score. |
| `PQ-15` | `ethical` | Ethical QMS | Apply an ethical or safety evaluator with explicit veto authority where applicable. |

Monte QMS is assumption perturbation unless stochastic sampling is actually
implemented. Distributed QMS must not claim distributed execution without a host
mechanism. All modes inherit the parent validator's no-invention boundary.
