#!/usr/bin/python3
"""hello hbnb module"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """outputs hello on root dir"""
    return 'Hello, HBNB!'


@app.route('/hbnb')
def hbnb():
    """outputs HBNB on /hbnb dir"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """outputs value of <text> var"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):
    """outputs value of <text> var"""
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>')
def num(n):
    """outputs value of <n> if its int"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def num_t(n):
    """outputs template if <n> is int"""
    return render_template('5-number.html')


@app.route('/number_odd_or_even/<int:n>')
def num_oddeven(n):
    """outputs template if <n> is odd or even"""
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html',
                               num=n, oddeven="even")
    return render_template('6-number_odd_or_even.html', num=n, oddeven="odd")


if __name__ == "__main__":
    app.run()
