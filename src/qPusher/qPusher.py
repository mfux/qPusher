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
import markdown
from qPusher.qTutor import qTutor


def parse_args(argv: list) -> argparse.Namespace:
    """
    Runtime args parser
    """
    parser = argparse.ArgumentParser("""Runtime args controlling the qPusher""")

    parser.add_argument(
        "--APP_TOKEN",
        help="pushOVER app token",
        type=str,
        required=False,
        default=os.environ.get("APP_TOKEN"),
    )

    parser.add_argument(
        "--USER_KEY",
        help="pushOVER user key",
        type=str,
        required=False,
        default=os.environ.get("USER_KEY"),
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

    parser.add_argument(
        "--markdown",
        help="converts the question to markdown",
        type=bool,
        required=False,
        default=False,
    )

    parser.add_argument(
        "--tutor",
        help="tutor mode",
        type=bool,
        required=False,
        default=False,
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

    # convert message from markdown to html
    msg = markdown.markdown(msg)

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": app_token,
                "user": user_key,
                "message": msg,
                "html": "1",
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()
    # log message
    logging.info(f"Pushed message: {msg} at {berlin_now().strftime('%H:%M:%S')}")


def time_is_appropriate(begin: int, end: int, scheduled_push: dt) -> bool:
    """Checks if current time is inside of defined boundaries"""
    # return True/False whether time is inside of defined boundaries
    return scheduled_push.hour >= begin and scheduled_push.hour < end


def schedule_push(args: argparse.Namespace, last_push: dt) -> dt:
    """
    Calculate a datetime Object that points to
    the time in x minutes with some deviation
    """
    # get period from args
    period = args.PERIOD
    # 15% random time deviation
    deviation = randint(int(-period * 0.15), int(period * 0.15))
    # calculate next push
    next_push = last_push + datetime.timedelta(minutes=period + deviation)
    # increase time to next push until time is appropriate
    while not time_is_appropriate(args.BEGIN, args.END, next_push):
        next_push = next_push + datetime.timedelta(minutes=period + deviation)
    return next_push


def select_question(q_dir: Path, markdown: bool, tutor: bool) -> str:
    """Picks a Random question from the Question Directory"""

    # pick a random question card from a random file in the question directory
    def cards(q_dir: Path):
        # collect all cards from all txt files
        cards = []
        for file in q_dir.glob("*.txt"):
            cards += [q.strip() for q in file.read_text().split("\n\n") if q]
        # collect markdown cards
        for file in q_dir.glob("*.md"):
            cards += [q.strip() for q in file.read_text().split("\n---\n") if q]
        return cards

    # pick a random card
    question = choice(cards(q_dir))

    # let tutor process the card and construct a message from it
    if tutor:
        tutor = qTutor()
        question = tutor.get_msg(question)

    return question


def chunk_msg(msg, max_length=512):
    """Splits a message into chunks of max length

    Args:
        msg (str): message to split
        max_length (int, optional): max length of each chunk. Defaults to 1024.

    Returns:
        iterator: iterator over chunks
    """

    # initialize chunks
    chunks = []
    # split question into multiple pushs if length exceeds max length
    if len(msg) > max_length:
        # tokenize question
        tokens = msg.split("\n")
        print(tokens)
        # initialize chunk
        chunk = ""
        # iterate over tokens
        for token in tokens:
            # if chunk is too long
            if len(chunk) + len(token) > max_length:
                # push chunk
                chunks.append(chunk)
                # reset chunk
                chunk = ""
            # add token to chunk
            chunk += token + "\n"
        # push last chunk
        chunks.append(chunk)
    # if message is short enough
    else:
        chunks.append(msg)
    return reversed(chunks)


def run(args):
    # schedule first push
    next_push = schedule_push(args, berlin_now())

    # mark first run
    first_run = True

    # start loop
    while True:
        try:
            # if next push is due and time is appropriate
            if (
                berlin_now() >= next_push
                and time_is_appropriate(args.BEGIN, args.END, berlin_now())
            ) or first_run:
                # select a question
                question = select_question(
                    args.QUESTIONS_DIR, args.markdown, args.tutor
                )

                # push each chunk
                chunks = chunk_msg(question)
                for chunk in chunks:
                    try:
                        push(chunk, args.APP_TOKEN, args.USER_KEY)
                    except Exception as e:
                        logging.error(f"Push failed: {e}")
                    sleep(1)

                # schedule next push
                next_push = schedule_push(args, berlin_now())

                # calculate time to sleep
                # schedule next push
                next_push = schedule_push(args, berlin_now())

            # calculate time to sleep
            sleep_time = (next_push - berlin_now()).total_seconds()  #

            # mark first run as done
            first_run = False

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
