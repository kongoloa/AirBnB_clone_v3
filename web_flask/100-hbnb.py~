#!/usr/bin/python3
from flask import Flask, render_template
"""
intializing flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def filters():
    """
    display HBNB HTML page
    """
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    return (render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities))


@app.teardown_appcontext
def teardown_db(exception):
    """
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
