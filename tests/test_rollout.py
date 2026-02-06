from hmarl.agents.policy import ConstantSpeedPolicy
from hmarl.sim.env import MaritimeConfig, MaritimeEnv
from hmarl.train.rollout import run_rollout


def test_rollout_runs() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=5))
    reward = run_rollout(env, ConstantSpeedPolicy(speed=0.6, slot_request=0.4))
    assert isinstance(reward, float)
