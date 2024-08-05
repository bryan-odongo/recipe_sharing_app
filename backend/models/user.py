from backend.models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    recipe = db.relationship('Recipe', back_populates='user')