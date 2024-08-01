from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(Text)
    instructions = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    banner_image = Column(String(256))
    category_id = Column(Integer, ForeignKey("categories.id"))

    user = relationship("User", back_populates="recipes")
    ingredients = relationship("Ingredient", back_populates="recipe")
    recipe_steps = relationship("RecipeStep", back_populates="recipe")
    recipe_tags = relationship("RecipeTag", back_populates="recipe")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    quantity = Column(String(80))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    recipe = relationship("Recipe", back_populates="ingredients")


class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    step_number = Column(Integer)
    instruction = Column(Text)

    recipe = relationship("Recipe", back_populates="recipe_steps")


class RecipeTag(Base):
    __tablename__ = "recipe_tags"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    recipe = relationship("Recipe", back_populates="recipe_tags")
