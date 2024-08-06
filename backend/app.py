import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from .models import db, User, Recipe, CookingHacks, CookingTips, Replies, Review, Ingredient, Image

app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    try:
        app.run(port=5555)
    except Exception as e:
        print(f"An error occurred: {e}")
