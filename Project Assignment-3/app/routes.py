from flask import render_template
from app import app
import os

@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html", title="Rekognition demo app")
