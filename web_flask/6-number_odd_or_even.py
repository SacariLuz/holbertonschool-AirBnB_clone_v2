#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    Display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>")
def display_c(text):
    """
    Display C followed by the value of the text.
    """
    text = text.replace("_", " ")
    return "C %s" % (text)


@app.route("/python")
@app.route("/python/<text>")
def display_python(text="is cool"):
    """
    Display python  followed by the value of the text.
    """
    text = text.replace("_", " ")
    return "Python %s" % (text)


@app.route("/number/<int:n>")
def display_if_int(n):
    """
    Display n is a number, only if n is an integer.
    """
    n = str(n)
    return "%d is a number" % (n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    Display a HTML page only if n is int.
    """
    n = str(n)
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    Render template if number is an integer
    identify if number is odd or even.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
