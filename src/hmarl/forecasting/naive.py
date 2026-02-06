"""Naive forecasting skeleton used to wire future congestion models."""


def repeat_last(values: list[float], horizon: int) -> list[float]:
    if horizon <= 0:
        return []
    if not values:
        return [0.0] * horizon
    return [values[-1]] * horizon
