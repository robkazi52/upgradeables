# Basic composition example

**Situation:** a workflow is long or multi-stage.

**Composition:** establish a task lock, activate `coherence-heartbeat`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
