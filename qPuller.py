from flask import Flask, request, send_from_directory
from random import choice
import os, os.path

#################
# CONFIGURATION #
#################

# path to the questions
qPATH = "/home/maximilian/data/questions/"

# port at which the app listens
PORT = 45818

# route at which the app responds
ROUTE_MAX = '/qPull'
ROUTE_STEFFEN = '/qWrite'

# path to stored questions
qPATH_MAX = '/home/maximilian/data/questions/'
qPATH_STEFFEN = '/home/maximilian/data/steffen_questions/'

#################
#  APPLICATION  #
#################
app = Flask(__name__)

def select_question():
    """Picks a Random question from the Question Directory"""
    # pick a random file from directory
    question_path = choice([qPATH + name for name in os.listdir(qPATH)
                            if os.path.isfile(qPATH + name)])

    # read question from file and return
    with open(question_path, 'r') as f:
        question = f.read()

    return question

def write_question(question, brother):
    if brother == 'steffen':
        q_path = qPATH_STEFFEN
    else:
        q_path = qPATH_MAX
    # create sequentially named file
    i = 1
    f_name = 'QUESTION_' + str(i)
    while os.path.isfile(q_path + f_name):
        i += 1
        f_name = 'QUESTION_' + str(i)

    if i == 10:
        push_achievement()

    # write file
    with open(q_path + f_name, 'w') as f:
        f.write(question)

    print(f_name) # debug
    return f_name

@app.route(ROUTE_MAX, methods=['POST'])
def hello_world():

    # extract questions from request and write to disk
    questions = list(request.get_json()['questions'])
    q_tuples = []
    for question in questions:
        q_tuples.append((write_question(question, 'max'), question))

    response = ''
    for t in q_tuples:
        response += t[0] + ": " + t[1] + '\n\n'
    return response

@app.route(ROUTE_STEFFEN, methods=['POST'])
def hello_world2():

    # extract questions from request and write to disk
    questions = list(request.get_json()['questions'])
    q_tuples = []
    for question in questions:
        q_tuples.append((write_question(question, 'steffen'), question))

    response = ''
    for t in q_tuples:
        response += t[0] + ": " + t[1] + '\n\n'
    return response

@app.route('/slides/<path:path>')
def send_slide(path):
    return send_from_directory('/home/maximilian/data/slides', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('/home/maximilian/data/img', path)

@app.route('/get_question')
def get_random_question():
    return select_question()

app.run(host="0.0.0.0", port=PORT)
