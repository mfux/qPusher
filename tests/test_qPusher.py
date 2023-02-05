from qPusher import qPusher
import argparse


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


def test_main():
    argv = [
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

    qPusher.main(argv)
