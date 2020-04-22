#!/usr/bin/python3
""" script that starts a Flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Show into the screen Hello HBNB!"""
    return ('Hello HBNB!')

app.run()
