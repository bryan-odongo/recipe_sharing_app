import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from .models import db, User, Recipe, CookingHacks, CookingTips, Replies, Review, Ingredient, Image

# Initialize Flask app
app = Flask(__name__)

# Load configuration
config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

# Initialize db and migrate
db.init_app(app)
migrate = Migrate(app, db)

# Run the app
if __name__ == '__main__':
    try:
        app.run(port=5555)
    except Exception as e:
        print(f"An error occurred: {e}")
