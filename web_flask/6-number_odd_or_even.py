#!/usr/bin/python3
"""
Script starts a simple flask application
"""
from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """
    Prints a message when /number_template/<n> is called in the url
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Prints a message when /number_odd_or_even/<n> is called in the url
    Displays Number: n is odd/even
    """
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
