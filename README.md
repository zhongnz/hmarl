# HMARL MVP (Minimal)

Smallest practical repository to start building the project.

## Current MVP contents
- `src/hmarl/sim/env.py` - tiny simulation environment scaffold
- `tests/test_env.py` - single smoke test
- `notebooks/mvp_demo.ipynb` - self-contained, Colab-compatible demo notebook
- `.github/workflows/ci.yml` - single CI job that runs tests only

## Run locally
```bash
PYTHONPATH=src pytest -q
```

## Run in Colab
Open `notebooks/mvp_demo.ipynb` in Colab and run all cells.
