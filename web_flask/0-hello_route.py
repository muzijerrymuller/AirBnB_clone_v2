#!/usr/bin/python3

"""
This module starts a Flask web application.
It listens on 0.0.0.0, port 5000, and displays 'Hello HBNB' on the root path.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """
    Route for the root URL.
    Returns a string 'Hello HBNB!'.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    """
    The main entry point of the application.
    Runs the Flask web server, listening on all IP addresses (0.0.0.0) on port 5000.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
