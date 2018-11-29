from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/<name>")
# def get_name(name):
#     return "Hello <i>{}</i>".format(name.upper())

import math
@app.route("//<number>")
def sqr_rt(number):
    return "math.sqrt(number)"