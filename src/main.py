from utils import *
from function import Function
from call import Call
from parameter import Parameter
from variable import Variable
import flask

prerequisites = {
    "expected_output" : "5",
    "functions": [
        Function(
            name="func1",
            params=[Parameter("x", int), Parameter("y", int)],
            short_description="add_two_args",
            expected_return="x+y",
            global_order=0
        )
    ],
    "calls": [
        Call(
            name="func1",
            content="2, 3",
            assignment="r",
            global_order=1
        ),
        Call(
            name="print",
            content="r",
            global_order=2
        )
    ]
}

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        code = flask.request.form["code"]
        is_correct = check(code, **prerequisites)
        return str(is_correct)
    else:
        return flask.render_template("index.html")
    
app.run()