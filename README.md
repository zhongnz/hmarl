# HMARL MVP Repository

Minimal starter repo for the Spring 2026 independent study:

**Hierarchical Multi-Agent Reinforcement Learning for Congestion-Aware Vessel Scheduling with Predictive Port Coordination**

## MVP Goal
Build only what is needed first:
1. A tiny simulation loop
2. A baseline policy
3. A notebook/script to inspect one run

## Run (local)
```bash
PYTHONPATH=src pytest -q
python notebooks/mvp_demo.py
```

## Minimal structure
- `src/hmarl/sim/env.py` - tiny simulation scaffold
- `tests/test_env.py` - smoke test
- `notebooks/mvp_demo.py` - quick run + print summary
- `docs/research-proposal.md` - project reference document

## Next step
Implement real maritime state transitions in `src/hmarl/sim/env.py`.
