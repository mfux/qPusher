import os
import http.client, urllib
from pathlib import Path
import logging
import pytz
from datetime import datetime as dt
import datetime
import argparse
import sys
from random import choice
from time import sleep
from random import randint


def parse_args(argv):
    """
    Runtime args parser
    """
    parser = argparse.ArgumentParser("""Runtime args controlling the qPusher""")

    parser.add_argument(
        "--APP_TOKEN",
        help="pushOVER app token",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--USER_KEY",
        help="pushOVER user key",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--BEGIN",
        help="push questions beginning at this hour. 0-23",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--END",
        help="push questions ending at this hour. 0-23",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--PERIOD",
        help="push questions every PERIOD minutes. 1-60",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--QUESTIONS_DIR",
        help="path to directory containing questions txt files",
        type=Path,
        required=True,
    )

    args = parser.parse_args(argv[1:])

    return args


##################
#   FUNCTIONS    #
##################


def berlin_now() -> dt:
    """Returns the current time in Berlin timezone"""
    return dt.now(tz=pytz.timezone("Europe/Berlin"))


def push(msg: str, app_token: str, user_key: str) -> None:
    """Sends a message to the Pushover API"""
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": app_token,
                "user": user_key,
                "message": msg,
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()
    # log message
    logging.info(f"Pushed message: {msg} at {berlin_now().strftime('%H:%M:%S')}")


def time_is_appropriate(begin: int, end: int) -> bool:
    """Checks if current time is inside of defined boundaries"""
    # get the current time
    now = berlin_now()
    # return True/False whether time is inside of defined boundaries
    return now.hour >= begin and now.hour < end


def schedule_push(period: int) -> dt:
    """
    Calculate a datetime Object that points to
    the time in x minutes with some deviation
    """
    # get the current time
    now = berlin_now()
    # 15% random time deviation
    deviation = randint(int(-period * 0.15), int(period * 0.15))
    # return datetime object
    next_push = now + datetime.timedelta(minutes=period + deviation)
    return next_push


def select_question(q_dir: Path) -> str:
    """Picks a Random question from the Question Directory"""

    # pick a random file from directory
    question_file_path = choice(list(q_dir.glob("*.txt")))

    # pick a random line from file
    question = choice(question_file_path.read_text().split("\n\n"))

    return question


def run(args):
    # schedule first push
    next_push = schedule_push(args.PERIOD)

    # start loop
    while True:
        try:
            # if next push is due and time is appropriate
            if berlin_now() >= next_push and time_is_appropriate(args.BEGIN, args.END):
                # select a question
                question = select_question(args.QUESTIONS_DIR)
                # push the question
                try:
                    push(question, args.APP_TOKEN, args.USER_KEY)
                except Exception as e:
                    logging.error(f"Push failed: {e}")
                # schedule next push
                next_push = schedule_push(args.PERIOD)

            # calculate time to sleep
            sleep_time = (next_push - berlin_now()).total_seconds()
            # sleep
            sleep(max(sleep_time, 0))

        # break on keyboard interrupt and end program
        except KeyboardInterrupt:
            logging.info("Keyboard Interrupt. Exiting...")
            break


###################
#      MAIN       #
###################


def main():
    # parse args
    args = parse_args(sys.argv)
    # run the program
    sys.exit(run(args))


if __name__ == "__main__":
    main()
