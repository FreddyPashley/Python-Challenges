from utils import *
from presets import *

import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        code = flask.request.form["code"]
        is_correct = check(code, **addTwoNums)
        print(is_correct)
        too_long = False
        if type(is_correct) == tuple:
            too_long = is_correct[1]
            is_correct = str(is_correct[0])
        else:
            is_correct = str(is_correct)
        if is_correct == "True":
            is_correct = "Correct!"
        if too_long:
            is_correct += ". (Your code could be more consice)"
        return flask.render_template("index.html", notif=is_correct, code=code)
    else:
        return flask.render_template("index.html")
    
app.run()