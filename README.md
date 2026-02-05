# Hierarchical Multi-Agent RL for Congestion-Aware Vessel Scheduling

This repository contains the Spring 2026 independent study project supervised by **Prof. Aboussalah**:

> **Hierarchical Multi-Agent Reinforcement Learning for Congestion-Aware Vessel Scheduling with Predictive Port Coordination**

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r env/requirements.txt
pip install -r env/requirements-dev.txt
./scripts/check.sh
```

## What is ready now

- Python package scaffold under `src/hmarl/` with modules for simulation, agents, forecasting, training, and utilities.
- Baseline configuration in `configs/default.json`.
- Unit tests for config loading, forecasting baseline, and environment stepping.
- Dev tooling setup with Ruff, MyPy, Pytest, and pre-commit hooks.
- GitHub collaboration templates and CI workflow.

## Repository Layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── pull_request_template.md
├── configs/
│   └── default.json
├── docs/
│   └── research-proposal.md
├── env/
│   ├── requirements.txt
│   └── requirements-dev.txt
├── scripts/
│   └── check.sh
├── src/hmarl/
│   ├── agents/
│   ├── forecasting/
│   ├── sim/
│   ├── train/
│   ├── utils/
│   └── config.py
└── tests/
```

## Next build steps

1. Implement discrete-event simulator mechanics in `src/hmarl/sim/`.
2. Add heuristic baseline policies in `src/hmarl/agents/`.
3. Implement short- and medium-term forecasting models in `src/hmarl/forecasting/`.
4. Build MAPPO/CTDE training and evaluation loops in `src/hmarl/train/`.

## Documentation

- Full proposal: [`docs/research-proposal.md`](docs/research-proposal.md)

## License

For academic/research use in the Spring 2026 independent study. Add institutional licensing details before public release.
