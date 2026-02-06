from hmarl.agents.policy import ConstantSpeedPolicy, VesselObservation


def test_constant_speed_policy() -> None:
    policy = ConstantSpeedPolicy(speed=0.7)
    action = policy.act(VesselObservation(progress=0.2))
    assert action == [0.7, 0.7]
