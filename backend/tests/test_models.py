from sqlalchemy.exec import IntegrityError
import pytest
from app import create_app
from models import db, CookingHacks, CookingTips, Image, Ingredient, Recipe, Replies, Review, User
from faker import Faker

fake = Faker()

class TestRecipe:
    """Class Recipe in models/recipes.py"""

    def test_recipe(self, new_user):
        recipe=Recipe(
            user_id=new_user.id,
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
        assert recipe.user_id == new_user.id
    
    def test_invalid_recipe(self, app, new_user):
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            invalid_recipe=Recipe(
                user_id=new_user.id,
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
            with pytest.raises(IntegrityError):
                db.session.add(invalid_recipe)
                db.session.commit()
    
class TestImage:
    """Class Image in models/images.py"""

    def test_image(self, app, new_recipe):
        with app.app_context():
            db.session.add(new_recipe)
            db.session.commit()

            image=Image(
                recipe_id=new_recipe.id,
                image_url=fake.image_url()
            )
            db.session.add(image)
            db.session.commit()
            fetched_image = Image.query.filter_by(recipe_id=new_recipe.id).first()

            assert fetched_image is not None
            assert fetched_image.image_url == image.image_url

class TestReply:
    """Class Reply in models/replies.py"""

    def test_replies(self, app, new_user, new_recipe):
        with app.app_context():
            db.session.add(new_user)
            db.session.add(new_recipe)
            db.session.commit()

            reply=Replies(
                review_id=1,
                reply=fake.text()
            )
            db.session.add(reply)
            db.session.commit()

            fetched_reply= Replies.query.filter_by(reply=reply.reply).first()
            assert fetched_reply is not None
            assert fetched_reply.reply == reply.reply

class TestCookingHacks:
    """Class CookingHacks in models/cookinghacks.py"""

    def test_cooking_hacks(self, app):
        with app.app_context():

            cooking_hack= CookingHacks(
                content=fake.text()
            )
            db.session.add(cooking_hack)
            db.session.commit()

            fetched_cooking_hack = CookingHacks.query.filter_by(content=cooking_hack.content).first()
            assert fetched_cooking_hack is not None

class TestCookingTips:
    """Class CookingTips in models/cookingtips.py"""

    def test_coooking_tips(self, app):
        with app.app_context():
            cooking_tip = CookingTips(
                title = fake.sentence(),
                content=fake.text(),
                created_at=fake.date_time_this_year_now(),
                updated_at=fake.date_time_this_year_now()
            )
            db.session.add(cooking_tip)
            db.session.commit()

            fetched_cooking_tip = CookingTips.query.filter_by(title=cooking_tip.content).first()
            assert fetched_cooking_tip is not None



class TestIngredients:
    """class Ingredient in models/ingredients.py"""

    def test_ingredients(self, app):
        with app.app_context():
            ingredient = Ingredient(
                recipe_id=1,
                name=fake.word(),
                image=fake.image_url()
            )
            db.session.add(ingredient)
            db.session.commit

            fetched_ingredient = Ingredient.query.filter_by(id=ingredient.id).first()
            assert fetched_ingredient is not None

