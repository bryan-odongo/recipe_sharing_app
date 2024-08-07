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

from backend.resources.recipes_resource import RecipeResource, RecipeByID
api.add_resource(RecipeResource, '/recipes', endpoint='recipes')
api.add_resource(RecipeByID, '/recipes/<int:id>', endpoint='recipes_by_id')

from backend.resources.cookinghacks_resource import CookingHacksResource, CookinghacksByID
api.add_resource(CookingHacksResource, '/cookinghacks', endpoint='cookinghacks')
api.add_resource(CookinghacksByID, '/cookinghacks/<int:id>', endpoint='cooking_hacks_by_id')

if __name__ == '__main__':
    try:
        app.run(port=5555, debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
