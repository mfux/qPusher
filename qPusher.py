import http.client, urllib
import datetime as dt
import pytz
from time import sleep
from random import randint, choice
import os

#################
# CONFIGURATION #
#################

# pushOVER app access data
APP_TOKEN = 'ahi3s16dbk89fs7hv2tkxaaomvxgaa'
USER_KEY_MAX = 'udzgnk8o6p349vwctj6qvi4c5f7eo6'
USER_KEY_STEFFEN = 'uh4xyaumaoffv26hpb64s3j2vvprp3'

# path to stored questions
qPATH_MAX = '/home/maximilian/data/questions/'
qPATH_STEFFEN = '/home/maximilian/data/steffen_questions/'

# push questions between these times
BEGIN = 9  # 09:00
END = 22   # 22:00

# push a question every ... minutes
PERIOD = 45

##################
#   FUNCTIONS    #
##################

def berlin_now():
    berlin_tz = pytz.timezone("Europe/Berlin")
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    berlin_now = utc_now.astimezone(berlin_tz)
    return berlin_now


# sending a push msg (copied from pushit website)
def push(msg, brother):
    if brother == 'steffen':
        user_key = USER_KEY_STEFFEN
    else:
        user_key = USER_KEY_MAX

    print(berlin_now().strftime('%H:%M:%S'))
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": APP_TOKEN,
        "user": user_key,
        "message": msg,
      }), {"Content-type": "application/x-www-form-urlencoded"})
    return conn.getresponse()

# check whether current time is inside of boundaries
def time_is_appropriate():
    # get the current time
    now = berlin_now()
    # return True/False whether time  is inside of defined boundaries
    return now.hour >= BEGIN and now.hour < END

def schedule_push():
    """
    Calculate a datetime Object that points to
    the time in x minutes with some deviation
    """
    # get the current time
    now = berlin_now()
    # 15% random time deviation
    deviation = randint(int(-PERIOD * 0.15), int(PERIOD * 0.15))
    # return datetime object
    next_push = now + dt.timedelta(minutes=PERIOD+deviation)
    return next_push

def select_question(brother):
    """Picks a Random question from the Question Directory"""
    if brother == 'steffen':
        qpath = qPATH_STEFFEN
    else:
        qpath = qPATH_MAX
    # pick a random file from directory
    question_path = choice([qpath + name for name in os.listdir(qpath)
                            if os.path.isfile(qpath + name)])

    # read question from file and return
    with open(question_path, 'r') as f:
        question = f.read()

    return question

###################
#      MAIN       #
###################

# schedule the next push
next_push = schedule_push()
# push(select_question('max'), 'max')
# push(select_question('steffen'), 'steffen')

# run forever
while True:
    # get current time
    now = berlin_now()

    # if the next push is due
    if now >= next_push:
        if time_is_appropriate():
            # select and send a question
            push(select_question('max'), 'max')
        # schedule the next push
        next_push = schedule_push()

    # sleep 1 second
    sleep(1)
