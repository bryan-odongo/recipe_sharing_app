from . import db
from .recipes import Recipe

class User(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)

    recipes = db.relationship('Recipe', back_populates='user')