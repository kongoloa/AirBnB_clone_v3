#!/usr/bin/python3
from flask import Flask, render_template
"""
intializing flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    """
    states = storage.all(classes["State"]).values()
    return (render_template('8-cities_by_states.html', states=states))


@app.route('/cities_by_states')
def cities_by_states():
    """
    """
    states = storage.all(classes["State"]).values()
    return (render_template('8-cities_by_states.html', states=states))


@app.teardown_appcontext
def teardown_db(exception):
    """
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
