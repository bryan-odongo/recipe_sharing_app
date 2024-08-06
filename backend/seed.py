import os
import sys
from flask import Flask
from faker import Faker
from .models import db, CookingHacks, Recipe, Replies, Ingredient, Image, CookingTips, Review, User

from .app import app
from .config import config

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

with app.app_context():
    fake = Faker()

    db.drop_all()
    db.create_all()

    user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    review_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def generate_ingredient():
        return {
            'name': fake.word(),
            'quantity': f"{fake.random_int(min=1, max=500)} {fake.random_element(elements=['grams', 'cups', 'tablespoons', 'teaspoons'])}"
        }

    def generate_instructions(num_steps=5):
        return "\n".join(f"{i+1}. {fake.sentence()}" for i in range(num_steps))

    def seed_recipes():
        recipes = []
        for _ in range(10):
            recipe = Recipe(
                user_id=fake.random_element(elements=user_ids),
                title=fake.sentence(),
                description=fake.text(),
                instructions=generate_instructions(),
                country=fake.random_element(elements=['Kenyan', 'Ugandan', 'Tanzanian', 'Rwandan', 'Ethiopian']),
                prep_time=fake.random_int(min=10, max=120),  
                cook_time=fake.random_int(min=10, max=120),  
                servings=fake.random_int(min=1, max=6),
                diet=fake.random_element(elements=['Vegetarian', 'Vegan', 'Gluten-Free', 'Low-Fat']),
                image_url=fake.image_url(),
                skill_level=fake.random_element(elements=['Easy', 'Medium', 'Hard']),
                created_at=fake.date_time_this_year()
            )
            db.session.add(recipe)
            recipes.append(recipe)
        db.session.commit()
        return [recipe.id for recipe in recipes]

    def seed_cooking_hacks():
        for _ in range(10):
            cooking_hacks = CookingHacks(
                content=fake.sentence()  
            )
            db.session.add(cooking_hacks)
        db.session.commit()
        print("Cooking hacks seeded successfully.")

    def seed_cooking_tips():
        for _ in range(10):
            cooking_tips = CookingTips(
                title=fake.sentence(),
                content=fake.text(),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year()
            )
            db.session.add(cooking_tips)
        db.session.commit()
        print("Cooking tips seeded successfully.")

    def seed_images(recipe_ids):
        for _ in range(10):
            image = Image(
                recipe_id=fake.random_element(elements=recipe_ids),
                image_url=fake.image_url()
            )
            db.session.add(image)
        db.session.commit()
        print("Images seeded successfully.")

    def seed_ingredients(recipe_ids):
        for _ in range(10):
            ingredient = Ingredient(
                recipe_id=fake.random_element(elements=recipe_ids),
                name=fake.sentence(),
                image=fake.image_url()
            )
            db.session.add(ingredient)
        db.session.commit()
        print("Ingredients seeded successfully.")

    def seed_replies():
        for _ in range(10):
            reply = Replies(
                review_id=fake.random_element(elements=review_ids),
                reply=fake.text()
            )
            db.session.add(reply)
        db.session.commit()
        print("Replies seeded successfully.")

    recipe_ids = seed_recipes()
    seed_cooking_hacks()
    seed_cooking_tips()
    seed_images(recipe_ids)
    seed_ingredients(recipe_ids)
    seed_replies()
