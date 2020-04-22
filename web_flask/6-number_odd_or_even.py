#!/usr/bin/python3
""" script that starts a Flask"""

from flask import Flask
from flask import render_template

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
    my_text = text.replace('_', ' ')
    return ("C {}".format(my_text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_is_cool(text='is cool'):
    """ Show 'Pyhon' plus given text or 'is cool' by defect"""
    my_text = text.replace('_', ' ')
    return ("Python {}".format(my_text))


@app.route("/number/<int:num>", strict_slashes=False)
def print_if_is_number(num):
    """ Show num if num is only number """
    return ("{} is a number".format(num))


@app.route("/number_template/<int:num>", strict_slashes=False)
def show_template_is_number(num):
    """ Show the template if num is only number """
    return render_template('5-number.html', number=num)


@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def is_odd_or_even(num):
    """ Show the template if num is only number """
    return render_template('6-number_odd_or_even.html', number=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
