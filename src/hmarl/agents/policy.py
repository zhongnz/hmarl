"""Simple policy skeletons for coordinator/vessel/port roles."""

from dataclasses import dataclass


@dataclass
class VesselObservation:
    """MVP vessel-side observation used by simple baseline policies."""

    progress: float
    congestion: float
    fuel: float


class ConstantSpeedPolicy:
    """MVP baseline policy with fixed speed + slot-request actions."""

    def __init__(self, speed: float = 0.5, slot_request: float = 0.5) -> None:
        self.speed = speed
        self.slot_request = slot_request

    def act(self, observation: VesselObservation) -> list[float]:
        _ = observation
        return [self.speed, self.slot_request]
