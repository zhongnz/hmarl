"""Very small demo script (notebook-friendly) for MVP validation."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hmarl.sim.env import MaritimeConfig, MaritimeEnv


def main() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=5))
    obs, info = env.reset()
    print("reset:", obs, info)

    done = False
    total_reward = 0.0
    while not done:
        action = env.sample_action()
        obs, reward, terminated, truncated, step_info = env.step(action)
        total_reward += reward
        done = terminated or truncated
        print("step:", step_info["step"], "obs:", obs)

    print("total_reward:", total_reward)


if __name__ == "__main__":
    main()
