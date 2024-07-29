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


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text):
    """
    prints a message when /python/<text> is called in the url
    Also prints out the default value of text when /python/ is called
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """
    Prints a message when /number/<n> is called in the url
    """
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
