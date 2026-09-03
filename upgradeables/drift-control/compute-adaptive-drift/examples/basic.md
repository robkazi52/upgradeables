# Basic composition example

**Situation:** compute/depth varies across a task.

**Composition:** establish a task lock, activate `compute-adaptive-drift`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
