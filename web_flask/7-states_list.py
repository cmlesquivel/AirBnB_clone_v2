#!/usr/bin/python3
""" script that get all states from db hbnb_dev_db"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """ Show the states list """
    dict_states = storage.all(State)
    return render_template('7-states_list.html', my_list=dict_states)


@app.teardown_appcontext
def shotdown_session(exception=None):
    """ remove the current SQLAlchemy Session: """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
