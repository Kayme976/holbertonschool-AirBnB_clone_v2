#!/usr/bin/python3
"""That starts a Flask web application 7."""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    This route generates an HTML page that lists all states in the database.
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    This function ensures that the database is closed when the request ends.
    """
    storage.close()


if __name__ == "__main__":
    """
    This conditional ensures that the Flask application only runs if the script
    is executed directly and not used as an imported module.
    """
    app.run(host='0.0.0.0', port=5000)
