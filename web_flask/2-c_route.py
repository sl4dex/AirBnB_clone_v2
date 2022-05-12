#!/usr/bin/python3
"""Web Framework"""
from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
	return 'HBNB'

@app.route('/c/<text>')
def c(text):
	return 'C %s' % text.replace("_", " ")
 
if __name__ == '__main__':
	app.run()