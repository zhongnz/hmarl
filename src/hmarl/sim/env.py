"""Minimal environment scaffold."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class MaritimeConfig:
    vessels: int = 8
    ports: int = 5
    episode_horizon: int = 100


class MaritimeEnv:
    """Simple environment scaffold compatible with future RL integrations."""

    def __init__(self, config: MaritimeConfig | None = None) -> None:
        self.config = config or MaritimeConfig()
        self.step_count = 0
        self._rng = Random(0)

    def sample_action(self) -> list[float]:
        return [self._rng.random(), self._rng.random()]

    def reset(self) -> tuple[list[float], dict[str, str]]:
        self.step_count = 0
        obs = [0.0, 0.0, 0.0, 0.0]
        return obs, {"phase": "reset"}

    def step(self, action: list[float]) -> tuple[list[float], float, bool, bool, dict[str, int]]:
        _ = action
        self.step_count += 1
        progress = min(1.0, self.step_count / self.config.episode_horizon)
        obs = [progress, progress, progress, progress]
        reward = 0.0
        terminated = self.step_count >= self.config.episode_horizon
        truncated = False
        info = {"step": self.step_count}
        return obs, reward, terminated, truncated, info
