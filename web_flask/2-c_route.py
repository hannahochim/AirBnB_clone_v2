#!/usr/bin/python3
"""
Script starts a simple flask application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Prints a message when / is called in the url
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Prints a message when /hbnb is called in the url
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Prints a message when /c/<text> is called in the url
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True)
