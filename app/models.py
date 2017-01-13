"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db


class Jokes(db.Model):
    """
    This model gives us a record of all the jokes they have preferred over time.
    
    parameters:
    @dad_joke - frequency of times they liked dad jokes
    @nerd_joke - frequency of times they liked nerd jokes
    @weird_joke - frequency of times they liked weird jokes
    @cat_meme - frequency of times they liked cat memes
    @dog_meme - frequency of times they liked dog memes
    @dad_timestamps - list of all timestamps when a dad joke was liked
    @nerd_timestamps - list of all timestamps when a nerd joke was liked
    @weird_timestamps - list of all timestamps when a weird joke was liked
    @cat_timestamps - list of all timestamps when a cat joke was liked
    @dog_timestamps - list of all timestamps when dog joke was liked
    @user_id - user's id which we get from the cookie stored on their computer
    """
    __tablename__ = 'jokes'
    id = db.Column(db.Integer, primary_key=True)
    dad_over_nerd = db.Column(db.Integer)
    nerd_over_dad = db.Column(db.Integer)
    dad_over_weird = db.Column(db.Integer)
    weird_over_dad = db.Column(db.Integer)
    dad_over_cat = db.Column(db.Integer)
    cat_over_dad = db.Column(db.Integer)
    dad_over_dog = db.Column(db.Integer)
    dog_over_dad = db.Column(db.Integer) 
    nerd_over_weird = db.Column(db.Integer)
    weird_over_nerd = db.Column(db.Integer)
    nerd_over_cat = db.Column(db.Integer)
    cat_over_nerd = db.Column(db.Integer)
    nerd_over_dog = db.Column(db.Integer)
    dog_over_nerd = db.Column(db.Integer)
    weird_over_cat = db.Column(db.Integer)
    cat_over_weird = db.Column(db.Integer)
    weird_over_dog = db.Column(db.Integer)
    dog_over_weird = db.Column(db.Integer)
    dog_over_cat = db.Column(db.Integer)
    cat_over_dog = db.Column(db.Integer)
    dad_joke = db.Column(db.Integer)
    nerd_joke = db.Column(db.Integer)
    weird_joke = db.Column(db.Integer)
    cat_meme = db.Column(db.Integer)
    dog_meme = db.Column(db.Integer)
    dad_timestamps = db.Column(db.String)
    nerd_timestamps = db.Column(db.String)
    weird_timestamps = db.Column(db.String)
    cat_timestamps = db.Column(db.String)
    dog_timestamps = db.Column(db.String)
    user_id = db.Column(db.String)

    def __init__(
            self,
            dad_over_nerd,
            nerd_over_dad,
            dad_over_weird,
            weird_over_dad,
            dad_over_cat,
            cat_over_dad,
            dad_over_dog,
            dog_over_dad, 
            nerd_over_weird,
            weird_over_nerd,
            nerd_over_cat,
            cat_over_nerd,
            nerd_over_dog,
            dog_over_nerd,
            weird_over_cat,
            cat_over_weird,
            weird_over_dog,
            dog_over_weird,
            dog_over_cat,
            cat_over_dog,
            dad_joke,
            nerd_joke,
            weird_joke,
            cat_meme,
            dog_meme,
            dad_timestamps,
            nerd_timestamps,
            weird_timestamps,
            cat_timestamps,
            dog_timestamps,
            user_id):
        self.dad_joke = dad_joke
        self.nerd_joke = nerd_joke
        self.weird_joke = weird_joke
        self.cat_meme = cat_meme
        self.dog_meme = dog_meme
        self.dad_timestamps = dad_timestamps
        self.nerd_timestamps = nerd_timestamps
        self.weird_timestamps = weird_timestamps
        self.cat_timestamps = cat_timestamps
        self.dog_timestamps = dog_timestamps
        self.user_id = user_id
        self.dad_over_nerd = dad_over_nerd
        self.nerd_over_dad = nerd_over_dad
        self.dad_over_weird = dad_over_weird
        self.weird_over_dad = weird_over_dad
        self.dad_over_cat = dad_over_cat
        self.cat_over_dad = cat_over_dad
        self.dad_over_dog = dad_over_dog
        self.dog_over_dad = dog_over_dad
        self.nerd_over_weird = nerd_over_weird
        self.weird_over_nerd = weird_over_nerd
        self.nerd_over_cat = nerd_over_cat
        self.cat_over_nerd = cat_over_nerd
        self.nerd_over_dog = nerd_over_dog
        self.dog_over_nerd = dog_over_nerd
        self.weird_over_cat = weird_over_cat
        self.cat_over_weird = cat_over_weird
        self.weird_over_dog = weird_over_dog
        self.dog_over_weird = dog_over_weird
        self.dog_over_cat = dog_over_cat
        self.cat_over_dog = cat_over_dog
        
    def __str__(self):
        return self.user_id
        
class Users(db.Model):
    """
    This model gives us a set of specific information for each user in this application
    
    parameters:
    @username - username of the user
    @password - password of the user, hashed for secrutiy reasons

    functions:
    __str__ - Returns the user name and password as an formatted string <Id: id, Username: username>
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String) #add hashing to this field

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __str__(self):
        return "<ID: {}, Username:{}>".format(self.id,self.username)
