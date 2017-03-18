from app import app, db, viz
from flask import request, render_template,redirect, url_for, Response
import json
from app.models import Jokes, Users
from datetime import datetime
from glob import glob
import os
import random
from functools import wraps


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    result = Users.query.filter_by(username=username).all()
    if len(result) == 0:
        return False
    elif result[0].password != password:
        return False
    else:
        return True

    
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

#ToDo update this method, like a ton
def increment_value(obj,decision):

    if decision == "dad_jokes":
        obj.dad_joke += 1
        listing = json.loads(obj.dad_timestamps)
        listing.append(str(datetime.now()))
        obj.dad_timestamps = json.dumps(listing)
    elif decision == "nerd_jokes":
        obj.nerd_joke += 1
        listing = json.loads(obj.nerd_timestamps)
        listing.append(str(datetime.now()))
        obj.nerd_timestamps = json.dumps(listing)
    elif decision == "weird_jokes":
        obj.weird_joke += 1
        listing = json.loads(obj.weird_timestamps)
        listing.append(str(datetime.now()))
        obj.weird_timestamps = json.dumps(listing)
    elif decision == "cat_memes":
        obj.cat_meme += 1
        listing = json.loads(obj.cat_timestamps)
        listing.append(str(datetime.now()))
        obj.cat_timestamps = json.dumps(listing)
    elif decision == "dog_memes":
        obj.dog_meme += 1
        listing = json.loads(obj.dog_timestamps)
        listing.append(str(datetime.now()))
        obj.dog_timestamps = json.dumps(listing)
    return obj


@app.route("/index",methods=["GET","POST"])
@requires_auth
def index():
    starting_directory = os.getcwd()
    if not starting_directory.endswith("img"):
        os.chdir("app/static/img")
    img_dirs = glob("*")
    #####
    # Add code here (clean up explanation of this
    #####
    
    first_dir = random.choice(img_dirs) #pick first joke type to show to end user
    img_dirs.remove(first_dir)
    second_dir = random.choice(img_dirs) #pick second joke type to show to end user
    first_picture = random.choice(glob(first_dir+"/*"))
    second_picture = random.choice(glob(second_dir+"/*"))
    first_file = "img/"+first_picture
    second_file = "img/"+second_picture
    os.chdir(starting_directory)
    first_img_url = url_for('static', filename=first_file)
    second_img_url = url_for('static', filename=second_file) 
    return render_template("index.html", first_img_url=first_img_url, second_img_url=second_img_url, first_dir=first_dir, second_dir=second_dir)


@app.route("/joke_decision", methods=["GET","POST"])
def joke_decision():
    auth = request.authorization
    
    user_id = auth.username #this will pull in the information from the cookie with an implicit field from the form
    if request.form.get("image_one"):
        decision = request.form.get("image_one")
        # import code
        # code.interact(local=locals())
    else:
        decision = request.form.get("image_two")
    joke = Jokes.query.filter_by(user_id=user_id).first()
    joke = increment_value(joke,decision)
    db.session.add(joke)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
    """
    Takes in username and password and creates new user in the database

    # Inputs:
    #     - @param username: string field
    #     - @param password: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None
    """
    if request.method=="POST":
        
        print(type(request.form))
        username = request.form.get("username")
        password = request.form.get("password_field")
        if len(Users.query.filter_by(username=username).all()) == 0:
            user = Users(username=username,password=password)
            db.session.add(user)
            db.session.commit()
            joke = Jokes(0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0,
                         json.dumps([]), json.dumps([]), json.dumps([]), json.dumps([]), json.dumps([]),
                         username)
            db.session.add(joke)
            db.session.commit()
            return redirect(url_for("sign_in"))
        else:
            return render_template("sign_up.html",error="username already exists, please choose another")
    return render_template("sign_up.html")

@app.route("/",methods=["GET","POST"])
def sign_in():
    """
    Takes in username and password and checks to see in the database

    # Inputs:
    #     - @param username: string field
    #     - @param password: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None
    """
    if request.method=="POST":
        
        username = request.form.get("username")
        password = request.form.get("password_field")
        result = Users.query.filter_by(username=username).all()
        if len(result) == 0:
            return render_template("sign_in.html",error="does not exist")
        elif result[0].password != password:
            return render_template("sign_in.html",error="wrong password")
        else:
            return redirect(url_for("index"))
    return render_template("sign_in.html")



# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
