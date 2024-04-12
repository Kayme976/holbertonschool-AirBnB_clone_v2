#!/usr/bin/python3
"""Starts a Flask web application 9.
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__, template_folder='templates')


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    for state in storage.all(State).values():
        if state.id == id:
            state.cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def close_session(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
