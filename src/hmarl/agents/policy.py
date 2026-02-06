"""Simple policy skeletons for coordinator/vessel/port roles."""

from dataclasses import dataclass


@dataclass
class VesselObservation:
    progress: float


class ConstantSpeedPolicy:
    """MVP baseline policy: always return the same speed pair."""

    def __init__(self, speed: float = 0.5) -> None:
        self.speed = speed

    def act(self, observation: VesselObservation) -> list[float]:
        _ = observation
        return [self.speed, self.speed]
