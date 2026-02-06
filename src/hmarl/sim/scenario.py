"""Scenario defaults for the HMARL MVP skeleton."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    """Static scenario values used across modules."""

    fleet_coordinators: int = 1
    vessels: int = 8
    ports: int = 5
