from hmarl.sim.env import MaritimeConfig, MaritimeEnv


def test_env_reset_and_step() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=2))
    obs, info = env.reset()
    assert len(obs) == 4
    assert info["phase"] == "reset"

    action = env.sample_action()
    _, _, terminated, truncated, info = env.step(action)
    assert not terminated
    assert not truncated
    assert info["step"] == 1

    _, _, terminated, truncated, _ = env.step(action)
    assert terminated
    assert not truncated
