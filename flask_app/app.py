from flask import Flask
from flask import render_template
from flask import request

from predict import get_preds

app = Flask(__name__)

def init():
    print('Starting...')

@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', user=name)

@app.route('/')
def index():
    username = request.args.get('username', None)

    # our predictor returns a list of usernames given a username
    lines = get_preds(username)

    return render_template('index.html',
        username=username,
        prediction=lines)