from hmarl.forecasting.naive import repeat_last


def test_repeat_last() -> None:
    assert repeat_last([1.0, 2.0], 3) == [2.0, 2.0, 2.0]
    assert repeat_last([], 2) == [0.0, 0.0]
    assert repeat_last([1.0], 0) == []
