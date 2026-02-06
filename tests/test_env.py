from hmarl.sim.env import MaritimeConfig, MaritimeEnv


def test_env_runs_to_completion() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=3))
    env.reset()

    terminated = False
    for _ in range(3):
        _, _, terminated, truncated, _ = env.step(env.sample_action())
        assert not truncated

    assert terminated
