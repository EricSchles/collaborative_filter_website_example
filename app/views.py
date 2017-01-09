from app import app, db, viz
from flask import request, render_template,redirect, url_for
import json
from app.models import Jokes
from datetime import datetime


def increment_value(obj,decision):
    if decision == "dad_joke":
        obj.dad_joke += 1
        listing = json.loads(obj.dad_timestamps)
        listing.append(str(datetime.now()))
        obj.dad_timestamps = json.dumps(listing)
    elif decision == "nerd_joke":
        obj.nerd_joke += 1
        listing = json.loads(obj.nerd_timestamps)
        listing.append(str(datetime.now()))
        obj.nerd_timestamps = json.dumps(listing)
    elif decision == "weird_joke":
        obj.weird_joke += 1
        listing = json.loads(obj.weird_timestamps)
        listing.append(str(datetime.now()))
        obj.weird_timestamps = json.dumps(listing)
    elif decision == "cat_meme":
        obj.cat_meme += 1
        listing = json.loads(obj.cat_timestamps)
        listing.append(str(datetime.now()))
        obj.cat_timestamps = json.dumps(listing)
    elif decision == "dog_meme":
        obj.dog_meme += 1
        listing = json.loads(obj.dog_timestamps)
        listing.append(str(datetime.now()))
        obj.dog_timestamps = json.dumps(listing)
    return obj


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/joke_decision", methods=["GET","POST"])
def joke_decision():
    user_id = request.form.get("user_id") #this will pull in the information from the cookie with an implicit field from the form
    
    if request.form.get("image_one"):
        decision = 
    request.form.get("image_two")
    joke = Jokes.query.filter_by(user_id=user_id)
    joke = increment_value(joke,decision)
    db.session.add(joke)
    db.session.commit()
    return redirect(url_for("index"))
    
# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
