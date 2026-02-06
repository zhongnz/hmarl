from hmarl.agents.policy import ConstantSpeedPolicy, VesselObservation


def test_constant_speed_policy() -> None:
    policy = ConstantSpeedPolicy(speed=0.7, slot_request=0.3)
    action = policy.act(VesselObservation(progress=0.2, congestion=0.5, fuel=80.0))
    assert action == [0.7, 0.3]
