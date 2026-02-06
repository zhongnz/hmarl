from hmarl.agents.policy import ConstantSpeedPolicy
from hmarl.sim.env import MaritimeConfig, MaritimeEnv
from hmarl.train.rollout import run_rollout


def test_rollout_runs() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=3))
    reward = run_rollout(env, ConstantSpeedPolicy())
    assert reward == 0.0
