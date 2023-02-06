from qPusher import qPusher
import argparse
import os


def test_parse_args():
    """Test if parse_args returns an argparse.Namespace and fills required args"""
    # fill required args
    args = qPusher.parse_args(
        [
            "src/qPusher/qPusher.py",
            "--APP_TOKEN",
            "123",
            "--USER_KEY",
            "123",
            "--BEGIN",
            "0",
            "--END",
            "23",
            "--PERIOD",
            "1",
            "--QUESTIONS_DIR",
            "test",
        ]
    )

    # test if parse_args returns an argparse.Namespace
    assert type(args) == argparse.Namespace

    # test if required args are filled
    assert args.APP_TOKEN == "123"


def test_push():
    app_token = os.environ.get("APP_TOKEN")
    user_key = os.environ.get("USER_KEY")
    if not app_token or not user_key:
        print("environment variables APP_TOKEN or USER_KEY not set")
        assert False
    # test sending a message
    qPusher.push(
        "Test Message",
        app_token="ahi3s16dbk89fs7hv2tkxaaomvxgaa",
        user_key="udzgnk8o6p349vwctj6qvi4c5f7eo6",
    )
    # needs to be verified on different devices
    assert True


def test_berlin_now():
    # test if current time is in berlin timezone
    now = qPusher.berlin_now()
    assert now.tzinfo.zone == "Europe/Berlin"
