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

    def __init__(self, dad_joke, nerd_joke, weird_joke, cat_meme, dog_meme,
                 dad_timestamps, nerd_timestamps, weird_timestamps, cat_timestamps,
                 dog_timestamps, user_id):
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

    def __str__(self):
        return self.user_id
        
