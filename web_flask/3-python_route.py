#!/usr/bin/python3
"""hello hbnb module"""
from flask import Flask


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


if __name__ == "__main__":
    app.run()
