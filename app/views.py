from app import app, db, viz
from flask import request, render_template,redirect, url_for
import json
from app.models import *

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        username = request.form.get("username")
    return render_template("index.html")

@app.route("/languages",methods=["GET","POST"])
def languages():
    viz.languages()
    return render_template("language_frequency.html")

# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
