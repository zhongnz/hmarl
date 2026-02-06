# Implementation Phases

## Phase 0 — Understanding and feasibility (now)
- Clarify scope and boundaries.
- Validate that environment + policy + rollout are wired.
- Use Colab to document assumptions and run sanity checks.

Deliverables:
- Colab notebook with planning and baseline run.
- Passing smoke tests.

## Phase 1 — Role-aware simulation
- Represent multiple vessels and ports explicitly.
- Introduce port queue and dock occupancy logic.
- Expand reward into vessel/port/coordinator components.

Deliverables:
- Multi-entity state update loop.
- Unit tests for queue and docking transitions.

## Phase 2 — Forecast-aware control
- Add short-term and medium-term forecast interfaces.
- Make vessel/port actions condition on forecasts.
- Add no-forecast vs forecast ablation hooks.

Deliverables:
- Forecast feature pipeline contract.
- Baseline forecast-injection experiments.

## Phase 3 — Learning and baselines
- Add baseline policies: heuristic, reactive, independent.
- Add MARL training loop scaffold for CTDE.
- Track metrics (delay, fuel, emissions, queue, throughput).

Deliverables:
- Comparable baseline runs.
- Feasibility report for full study training budget.

## Phase 4 — Study execution
- Run ablations and horizon tests.
- Compare coordinated vs reactive vs independent.
- Summarize practical and economic findings.
