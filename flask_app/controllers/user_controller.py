from flask import render_template, redirect, request, session

from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")