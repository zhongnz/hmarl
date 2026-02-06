# HMARL Project Setup (Planning + Colab First)

This repository is now optimized for the current priority:

1. Build a clear understanding of the project scope and research questions.
2. Plan implementation milestones that are feasible in one semester.
3. Use a Colab-first notebook workflow for rapid iteration and supervision updates.

## What to use first

- `notebooks/mvp_demo.ipynb`  
  Main planning + feasibility notebook (Colab-compatible).
- `docs/project-map.md`  
  One-page project map linking goals, modules, and outcomes.
- `docs/implementation-phases.md`  
  Step-by-step build plan from MVP to research experiments.

## Current code skeleton (kept minimal)

- `src/hmarl/sim/env.py`: simple environment with progress/fuel/congestion dynamics.
- `src/hmarl/sim/scenario.py`: baseline scenario constants (1 coordinator, 8 vessels, 5 ports).
- `src/hmarl/agents/policy.py`: baseline constant policy contract.
- `src/hmarl/forecasting/naive.py`: repeat-last-value forecast baseline.
- `src/hmarl/train/rollout.py`: one-episode rollout runner.

## Local checks

```bash
PYTHONPATH=src pytest -q
```

## Colab workflow

Open `notebooks/mvp_demo.ipynb` in Google Colab and run all cells.
The notebook includes:
- project framing,
- feasibility checklist,
- baseline simulation run,
- and next-step milestone planning.
