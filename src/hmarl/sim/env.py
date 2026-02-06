"""Minimal but meaningful maritime environment scaffold.

This environment is intentionally simple:
- one aggregate vessel state (progress + fuel)
- one aggregate congestion signal in [0, 1]
- two continuous actions in [0, 1]: speed and slot request

It is designed to be easy to replace with a richer multi-agent simulator later.
"""

from __future__ import annotations

from dataclasses import dataclass
from random import Random

from hmarl.sim.scenario import Scenario


@dataclass
class MaritimeConfig:
    """Config for the MVP simulator."""

    vessels: int = Scenario().vessels
    ports: int = Scenario().ports
    episode_horizon: int = 100
    base_fuel_budget: float = 100.0


class MaritimeEnv:
    """Simple environment scaffold compatible with future RL integrations."""

    def __init__(self, config: MaritimeConfig | None = None) -> None:
        self.config = config or MaritimeConfig()
        self.step_count = 0
        self._rng = Random(0)
        self.progress = 0.0
        self.fuel = self.config.base_fuel_budget
        self.congestion = 0.0

    def sample_action(self) -> list[float]:
        """Sample [speed, slot_request] in [0, 1]."""
        return [self._rng.random(), self._rng.random()]

    def reset(self) -> tuple[list[float], dict[str, str]]:
        """Reset episode state and return first observation."""
        self.step_count = 0
        self.progress = 0.0
        self.fuel = self.config.base_fuel_budget
        self.congestion = 0.2
        obs = [self.progress, self.fuel, self.congestion, 1.0]
        return obs, {"phase": "reset"}

    def step(self, action: list[float]) -> tuple[list[float], float, bool, bool, dict[str, float | int]]:
        """Advance one step.

        Args:
            action: [speed, slot_request], each in [0, 1].
        """
        speed = max(0.0, min(1.0, action[0]))
        slot_request = max(0.0, min(1.0, action[1]))

        self.step_count += 1

        # Deterministic congestion trend (bounded) for reproducible MVP behavior.
        self.congestion = min(1.0, 0.15 + 0.7 * (self.step_count / self.config.episode_horizon))

        # Progress improves with speed but is reduced by congestion.
        progress_gain = speed * (1.0 - 0.6 * self.congestion)
        self.progress = min(1.0, self.progress + progress_gain / self.config.episode_horizon)

        # Fuel burn grows with speed and congestion; slot request has coordination overhead.
        fuel_burn = 0.2 + 0.5 * speed + 0.2 * self.congestion + 0.1 * slot_request
        self.fuel = max(0.0, self.fuel - fuel_burn)

        # Reward: progress is good; fuel burn and congestion are costly.
        reward = 2.0 * progress_gain - 0.3 * fuel_burn - 0.2 * self.congestion

        terminated = self.progress >= 1.0 or self.step_count >= self.config.episode_horizon
        truncated = False

        steps_left_ratio = max(0.0, (self.config.episode_horizon - self.step_count) / self.config.episode_horizon)
        obs = [self.progress, self.fuel, self.congestion, steps_left_ratio]
        info: dict[str, float | int] = {
            "step": self.step_count,
            "progress_gain": progress_gain,
            "fuel_burn": fuel_burn,
            "slot_request": slot_request,
        }
        return obs, reward, terminated, truncated, info
