#!/usr/bin/python3
""" script that starts a Flask"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """ Show into the screen Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """ Show into the screen HBNB!"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
