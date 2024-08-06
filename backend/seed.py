from flask import Flask
from faker import Faker
from .models import db, CookingHacks, Recipe, Replies, Ingredient, Image, CookingTips, Review
from .app import create_app

app = create_app('development')

with app.app_context():
    fake = Faker()

    db.drop_all()
    db.create_all()

    user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    review_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def seed_recipes():
        recipes = []
        for _ in range(10):
            recipe = Recipe(
                user_id=fake.random_element(elements=user_ids),
                title=fake.sentence(),
                description=fake.text(),
                instructions=fake.text(),
                country=fake.country(),
                prep_time=fake.random_int(min=1, max=120),
                cook_time=fake.random_int(min=1, max=120),
                servings=fake.random_int(min=1, max=10),
                diet=fake.word(),
                image_url=fake.image_url(),
                skill_level=fake.word(),
                created_at=fake.date_time_this_year()
            )
            db.session.add(recipe)
            recipes.append(recipe)
        db.session.commit()
        return [recipe.id for recipe in recipes]

    def seed_cooking_hacks():
        for _ in range(10):
            cooking_hacks = CookingHacks(
                content=fake.text()
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
