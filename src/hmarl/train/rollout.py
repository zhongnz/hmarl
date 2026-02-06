"""Training skeleton: run one rollout with a provided policy."""

from hmarl.agents.policy import ConstantSpeedPolicy, VesselObservation
from hmarl.sim.env import MaritimeEnv


def run_rollout(env: MaritimeEnv, policy: ConstantSpeedPolicy) -> float:
    """Run one episode and return total reward."""
    obs, _ = env.reset()
    done = False
    total_reward = 0.0

    while not done:
        action = policy.act(
            VesselObservation(
                progress=obs[0],
                fuel=obs[1],
                congestion=obs[2],
            )
        )
        obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        done = terminated or truncated

    return total_reward
