#!/usr/bin/python3
from flask import Flask, render_template
"""
intializing flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def display_site():
    """
    display HBNB HTML page
    """
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    places = storage.all(classes["Place"]).values()
    return (render_template('100-hbnb.html', states=states,
                            amenities=amenities, places=places))


@app.teardown_appcontext
def teardown_db(exception):
    """
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
