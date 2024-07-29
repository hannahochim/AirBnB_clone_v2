#!/usr/bin/python3
"""
Scripts starts a simple flask application
routing / returns Hello Hbnb
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """function def for routing"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True)
