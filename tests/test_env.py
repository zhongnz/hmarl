from hmarl.sim.env import MaritimeConfig, MaritimeEnv


def test_env_runs_to_completion() -> None:
    env = MaritimeEnv(MaritimeConfig(episode_horizon=3))
    obs, info = env.reset()

    assert info["phase"] == "reset"
    assert len(obs) == 4

    terminated = False
    for _ in range(3):
        obs, reward, terminated, truncated, info = env.step(env.sample_action())
        assert not truncated
        assert len(obs) == 4
        assert isinstance(reward, float)
        assert "fuel_burn" in info

    assert terminated
