from sqlalchemy.orm import validates
from database import db


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=True)
    instructions = db.Column(db.Text, nullable=True)
    banner_image = db.Column(db.String(256), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel", back_populates="recipes")
    ingredients = db.relationship(
        "Ingredient", back_populates="recipe", cascade="all, delete-orphan"
    )
    comments = db.relationship(
        "Comment", back_populates="recipe", cascade="all, delete-orphan"
    )
    ratings = db.relationship(
        "Rating", back_populates="recipe", cascade="all, delete-orphan"
    )
    other_images = db.relationship(
        "OtherRecipeImages", back_populates="recipe", cascade="all, delete-orphan"
    )

    @validates("title")
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title is required")
        return title

    def __repr__(self):
        return f"<Recipe(title={self.title}, user_id={self.user_id})>"

    __tableargs__ = (
        db.UniqueConstraint("title", "user_id", name="unique_user_recipe_title"),
    )


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(256), nullable=True)
    quantity = db.Column(db.String(256), nullable=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)

    recipe = db.relationship("Recipe", back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient(name={self.name}, recipe_id={self.recipe_id})>"

    __table_args__ = (
        db.UniqueConstraint("name", "recipe_id", name="unique_recipe_ingredient"),
    )


class OtherRecipeImages(db.Model):
    __tablename__ = "other_recipe_images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(256), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)

    recipe = db.relationship("Recipe", back_populates="other_images")

    __table_args__ = (
        db.UniqueConstraint("image", "recipe_id", name="unique_recipe_image"),
    )
