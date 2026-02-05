from hmarl import load_config


def test_load_default_config() -> None:
    cfg = load_config("configs/default.json")
    assert cfg["project"]["name"] == "hmarl"
    assert cfg["environment"]["vessels"] == 8
