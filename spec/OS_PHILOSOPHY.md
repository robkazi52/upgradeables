# OS Philosophy

The model is the general reasoning substrate; an OS is a compositional operating
layer that supplies task identity, authority, routing, explicit state, domain
structure, evidence handling, safety, and quality control. It should shape work
without pretending to replace native model capability.

The architecture is layered and nonmonolithic:

```text
Global OS -> Project kernel -> Task shell
          -> Behavior Gene + Core + Upgradeables
          -> Loader + State + Orchestrator + Validators -> Output
```

## Historical tier model

T1 was the always-on kernel: a frozen 28-item bundle is confirmed, but only 18
exact frozen member IDs are proven. Newly recovered pre-freeze T1 library items
must not fill the ten gaps by inference. T2 was a 67-item, 12-family composable
capability library. T3 was an opt-in alignment/verification layer activated by
risk, evidence sensitivity, or mode—not a command to run every expensive check.
T4 supervises the scaffolding itself: drift width, depth, throughput, stability,
mode selection, and model-capability scaling.

Load the minimum necessary context. Separate behavior from knowledge. Prefer
orchestration over prompt accumulation, explicit state over hidden assumptions,
truth before fluency, local repair before global rewrite, and bounded iteration.
Preserve factual (`Lf`), evaluative (`Le`), framing (`Lp`), and hypothetical
(`Lh`) phase boundaries where risk makes leakage consequential.

Risk and consequence determine reasoning depth and validation. Design may use
broader bounded exploration; execution collapses to a narrower grounded path.
Stronger models should need less scaffolding, while integrity controls remain
whenever the task still requires them.
