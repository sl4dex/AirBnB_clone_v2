#!/usr/bin/python3
"""hello hbnb module"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """outputs hello on root dir"""
    return 'Hello, HBNB!'

if __name__ == "__main__":
    app.run()
