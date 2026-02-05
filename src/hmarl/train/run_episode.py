"""Episode runner scaffolding."""

from hmarl.sim.env import MaritimeEnv


def run_random_episode(env: MaritimeEnv) -> float:
    """Roll out one episode with random actions and return cumulative reward."""
    env.reset()
    done = False
    total_reward = 0.0
    while not done:
        action = env.sample_action()
        _, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        done = terminated or truncated
    return total_reward
