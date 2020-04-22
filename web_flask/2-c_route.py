#!/usr/bin/python3
""" script that starts a Flask"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """ Show the Hello HBNB! for the root path"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """ Show HBNB for the path /hbnb"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def print_c_is_fun(text):
    """ Show 'C' plus given text"""
    return ("C {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
