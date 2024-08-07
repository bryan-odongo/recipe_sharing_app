# from database import db



# class Bookmark(db.Model):

#     __tablename__ = "bookmarks"

#     id= db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     recipe_id= db.Column(db.Integer, db.ForeignKey("recipes.id"))
#     created_at = db.Column(db.DateTime, server_default=db.func.now())

#     user = db.relationship("User", backref="bookmarks")
#     recipe = db.relationship("Recipe", backref="bookmarks")

