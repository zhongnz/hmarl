"""Baseline forecasting utilities."""


def naive_last_value(series: list[float], horizon: int) -> list[float]:
    """Repeat the last observed value over a forecast horizon."""
    if not series:
        return [0.0 for _ in range(horizon)]
    return [float(series[-1]) for _ in range(horizon)]
