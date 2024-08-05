#!/usr/bin/env python3

import sys
import os
import pytest
from faker import Faker

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import db, User, Recipe
from app import create_app

fake = Faker()

@pytest.fixture(scope='module')
def app():
    app = create_app('testing')  # Ensure you have a 'testing' config for your app
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def new_user():
    user = User(name='Test User', email='testuser@example.com')
    return user

@pytest.fixture(scope='module')
def new_recipe(new_user):
    recipe = Recipe(
        user_id=new_user.id,
        title='Test Recipe',
        description='This is a test recipe',
        instructions='Mix ingredients and cook.',
        country='Testland',
        prep_time=10,
        cook_time=20,
        servings=2,
        diet='vegan',
        image='http://example.com/image.jpg',
        skill_level='easy',
        created_at=fake.date_time_this_year()
    )
    return recipe

@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()
