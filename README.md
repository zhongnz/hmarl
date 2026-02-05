# Hierarchical Multi-Agent RL for Congestion-Aware Vessel Scheduling

This repository contains the Spring 2026 independent study project supervised by **Prof. Aboussalah**:

> **Hierarchical Multi-Agent Reinforcement Learning for Congestion-Aware Vessel Scheduling with Predictive Port Coordination**

## Project Goals

- Build a hierarchical MARL framework with:
  - 1 Fleet Coordinator agent
  - 8 Vessel agents
  - 5 Port agents
- Integrate medium- and short-term congestion forecasting for proactive coordination.
- Evaluate operational outcomes: delay, fuel consumption, emissions, and system-wide cost.
- Analyze economic outcomes related to shipping reliability and effective transport pricing.

## Repository Layout

```text
.
├── .github/                    # Issue/PR templates + CI workflow
├── configs/                    # Experiment and environment configs
├── data/
│   ├── raw/                    # Immutable source datasets (AIS, etc.)
│   ├── external/               # Third-party/alternative data
│   └── processed/              # Generated feature tables and simulation inputs
├── docs/
│   └── research-proposal.md    # Full project proposal and timeline
├── env/                        # Environment and dependency manifests
├── notebooks/                  # Exploratory analysis and reporting notebooks
├── results/
│   ├── figures/
│   ├── logs/
│   └── tables/
├── scripts/                    # Utility scripts for training/evaluation pipelines
└── src/                        # Core simulation, forecasting, and MARL modules
```

## Initial Milestones

1. Implement the discrete-event maritime simulation environment.
2. Add heuristic baselines for fleet, vessel, and port decision-making.
3. Implement forecasting pipelines (short-term and medium-term).
4. Train and compare MARL settings:
   - Independent agents
   - Reactive coordinated agents
   - Forecast-informed coordinated agents
   - Oracle upper bound

## Development Workflow

- Open an issue for each major experiment or infrastructure change.
- Use small PRs tied to clear milestones.
- Keep experiment configs versioned under `configs/`.
- Store run metadata and metrics in `results/logs/`.

## Documentation

- Full proposal: [`docs/research-proposal.md`](docs/research-proposal.md)
- Use pull request template for methodology and evaluation checklists.

## License

For academic/research use in the Spring 2026 independent study. Add institutional licensing details before public release.
