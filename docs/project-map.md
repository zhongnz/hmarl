# Project Map (Planning First)

## Objective
Develop a hierarchical multi-agent RL framework for congestion-aware vessel scheduling with predictive port coordination.

## Core entities
- Fleet coordinator (strategic decisions)
- Vessel agents (speed + arrival behavior)
- Port agents (dock and queue management)

## What success looks like
- Lower delay
- Lower fuel/emissions
- Better queue/dock efficiency
- Better reliability and cost stability

## Minimal architecture path
1. Single-environment MVP (current)
2. Add explicit vessel + port state structures
3. Add coordinator directives and role-specific observations/actions
4. Add forecast injection points
5. Add baseline comparisons
6. Add MARL training loop (CTDE/MAPPO)

## Current repository mapping
- `src/hmarl/sim/`: environment and scenario assumptions
- `src/hmarl/agents/`: policy contracts and baselines
- `src/hmarl/forecasting/`: forecast placeholders
- `src/hmarl/train/`: rollout/training entry points
- `notebooks/`: planning + feasibility + quick demos
- `tests/`: smoke checks for each module
