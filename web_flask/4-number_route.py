#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Display C followed by the value of the text.
    """
    text = text.replace("_", " ")
    return "C %s" % (text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """
    Display python  followed by the value of the text.
    """
    text = text.replace("_", " ")
    return "Python %s" % (text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_if_int(n):
    """
    Display n is a number, only if n is an integer.
    """
    return "%d is a number" % (n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
