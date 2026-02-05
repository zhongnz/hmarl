#!/usr/bin/env bash
set -euo pipefail

if command -v ruff >/dev/null 2>&1; then
  ruff check src tests
else
  echo "ruff not installed; skipping lint"
fi

if command -v mypy >/dev/null 2>&1; then
  mypy src
else
  echo "mypy not installed; skipping type checks"
fi

PYTHONPATH=src pytest -q
