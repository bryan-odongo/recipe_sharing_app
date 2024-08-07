import os
from flask import Flask
from backend.config import config
from backend.models import db, migrate  

app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

db.init_app(app)
migrate.init_app(app, db)

from backend.models.user import User
from backend.models.recipes import Recipe
from backend.models.ingredients import Ingredient
from backend.models.replies import Replies
from backend.models.cookinghacks import CookingHacks
from backend.models.cookingtips import CookingTips
from backend.models.images import Image
from backend.models.review import Review

from flask_restful import Api
api = Api(app)

from backend.resources.recipes_resource import RecipeResource
api.add_resource(RecipeResource, '/recipes', endpoint='recipes')

if __name__ == '__main__':
    try:
        app.run(port=5555, debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
