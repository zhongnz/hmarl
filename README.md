# HMARL MVP Skeleton

This repository now contains a minimal but usable skeleton for building the project incrementally.

## Step-by-step skeleton (what + why)

1. **Simulation core (`src/hmarl/sim/env.py`)**
   - **What**: A tiny environment with `reset`, `step`, and `sample_action`.
   - **Why**: All future MARL logic needs a stable environment API first.

2. **Scenario defaults (`src/hmarl/sim/scenario.py`)**
   - **What**: A dataclass with base counts (1 coordinator, 8 vessels, 5 ports).
   - **Why**: Keep project assumptions in one place to avoid hardcoding values.

3. **Agent policy skeleton (`src/hmarl/agents/policy.py`)**
   - **What**: A baseline constant-speed policy and observation type.
   - **Why**: Gives a deterministic baseline to test the training/evaluation pipeline.

4. **Forecasting skeleton (`src/hmarl/forecasting/naive.py`)**
   - **What**: A repeat-last forecaster.
   - **Why**: Provides a simple placeholder to wire forecast inputs before real models.

5. **Training/rollout skeleton (`src/hmarl/train/rollout.py`)**
   - **What**: A single-episode runner that uses a policy with the environment.
   - **Why**: Connects env + policy in one path you can later replace with MAPPO loops.

6. **Tests (`tests/`)**
   - **What**: Smoke tests for env, policy, forecasting, and rollout.
   - **Why**: Confirms each layer works before adding complexity.

7. **Colab demo (`notebooks/mvp_demo.ipynb`)**
   - **What**: Self-contained runnable notebook.
   - **Why**: Quick reproducible demo without local setup friction.

## Run locally

```bash
PYTHONPATH=src pytest -q
```
