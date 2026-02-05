"""Base protocols for coordinator, vessel, and port agents."""

from typing import Protocol


class AgentPolicy(Protocol):
    def act(self, observation: dict) -> dict:
        """Return an action dictionary for the current observation."""
