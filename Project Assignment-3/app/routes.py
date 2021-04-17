from flask import render_template
from app import app
import os

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello World!</h1>"
