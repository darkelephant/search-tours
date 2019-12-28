# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')                     
def index():
    page = render_template("index.html")
    return page

@app.route('/from/<direction>')
def from_to(direction):
    page = render_template("direction.html")
    return page

@app.route('/tours/<id>')  
def about(id):
    page = render_template("tour.html")
    return page
  
if __name__ == "__main__":
    app.run('localhost', 8000)
