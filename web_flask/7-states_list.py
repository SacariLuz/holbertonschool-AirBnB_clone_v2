#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Return an HTML page showing a list with all state objects"""
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def close_session(self):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
