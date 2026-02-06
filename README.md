# HMARL MVP Skeleton

This repository is a **working skeleton** for your hierarchical maritime RL project.
It is intentionally small, but each part is now connected and testable.

## What has been implemented (step-by-step)

### Step 1 — Environment API (`src/hmarl/sim/env.py`)
**What it does**
- Defines `MaritimeConfig` for episode settings.
- Defines `MaritimeEnv` with `reset`, `step`, and `sample_action`.
- Tracks four observable values: `progress`, `fuel`, `congestion`, and `steps_left_ratio`.

**Why this matters**
- Every RL pipeline depends on a stable environment interface.
- We can now train/evaluate policies without changing API contracts later.

### Step 2 — Scenario defaults (`src/hmarl/sim/scenario.py`)
**What it does**
- Centralizes baseline study assumptions: 1 coordinator, 8 vessels, 5 ports.

**Why this matters**
- Prevents hardcoding project constants in multiple places.

### Step 3 — Policy baseline (`src/hmarl/agents/policy.py`)
**What it does**
- Introduces `VesselObservation`.
- Implements `ConstantSpeedPolicy` that returns `[speed, slot_request]`.

**Why this matters**
- Provides a deterministic baseline policy for debugging and comparisons.

### Step 4 — Forecasting placeholder (`src/hmarl/forecasting/naive.py`)
**What it does**
- `repeat_last(values, horizon)` returns a simple naive forecast.

**Why this matters**
- Lets you wire forecast-dependent logic before building complex models.

### Step 5 — Rollout connector (`src/hmarl/train/rollout.py`)
**What it does**
- `run_rollout(env, policy)` executes one complete episode.
- Converts environment observations into policy observations.

**Why this matters**
- This is the minimum training loop backbone you will later replace with MARL updates.

### Step 6 — Test coverage (`tests/`)
**What it does**
- Validates environment step loop.
- Validates policy action output.
- Validates naive forecasting behavior.
- Validates rollout execution.

**Why this matters**
- Keeps the skeleton reliable while you expand complexity.

### Step 7 — Colab demo (`notebooks/mvp_demo.ipynb`)
**What it does**
- Self-contained notebook that runs in Google Colab directly.

**Why this matters**
- Quick demo path for supervision/review without local environment setup.

## Local command

```bash
PYTHONPATH=src pytest -q
```
