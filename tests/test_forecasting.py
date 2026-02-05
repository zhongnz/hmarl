from hmarl.forecasting.baseline import naive_last_value


def test_naive_last_value_non_empty() -> None:
    series = [1.0, 2.5, 3.0]
    pred = naive_last_value(series, horizon=4)
    assert pred == [3.0, 3.0, 3.0, 3.0]


def test_naive_last_value_empty() -> None:
    pred = naive_last_value([], horizon=3)
    assert pred == [0.0, 0.0, 0.0]
