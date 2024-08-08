import secrets
from flask import Flask, jsonify
from flasgger import Swagger
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from database import db

from resources.user import (
    RegisterResource,
    LoginResource,
    ResetPasswordResource,
    UserResource,
    UserListResource,
)
from resources.recipe import (
    IngredientResource,
    RecipeResource,
    RecipeListResource,
    OtherRecipeImageListResource,
    OtherRecipeImageResource,
)
from resources.engagement import (
    CommentResource,
    CommentListResource,
    CommentResponseListResource,
    CommentResponseResource,
    RatingResource,
    RatingListResource,
)


from config import sqliteConfig

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sqliteConfig
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = (
    f"a1d3c56531737{secrets.token_hex(4)}cf62bc36a7e30cd871d7{secrets.token_hex(4)}7b5b51e8208b8cef{secrets.token_hex(4)}c2689e8c0cb412b"
)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
swagger = Swagger(app)

CORS(app)


# auth
api.add_resource(RegisterResource, "/api/register")
api.add_resource(LoginResource, "/api/login")
api.add_resource(ResetPasswordResource, "/reset-password")
api.add_resource(UserResource, "/api/users/<string:identifier>")
api.add_resource(UserListResource, "/api/users")
# recipes
api.add_resource(RecipeListResource, "/api/recipes")
api.add_resource(RecipeResource, "/api/recipes/<int:recipe_id>")
# ingredients
api.add_resource(
    IngredientResource, "/api/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>"
)
# comments
# api.add_resource(CommentListResource, "/api/recipes/<int:recipe_id>/comments")
# api.add_resource(
#     CommentResource, "/api/recipes/<int:recipe_id>/comments/<int:comment_id>"
# )
# responses
# api.add_resource(
#     CommentResponseListResource,
#     "/api/recipes/<int:recipe_id>/comments/<int:comment_id>/responses",
# )
# api.add_resource(
#     CommentResponseResource,
#     "/api/recipes/<int:recipe_id>/comments/<int:comment_id>/responses/<int:response_id>",
# )
# ratings
# api.add_resource(RatingListResource, "/api/recipes/<int:recipe_id>/ratings")
# api.add_resource(RatingResource, "/api/recipes/<int:recipe_id>/ratings/<int:rating_id>")
# other images
# api.add_resource(OtherRecipeImageListResource, "/api/recipes/<int:recipe_id>/images")
# api.add_resource(
#     OtherRecipeImageResource, "/api/recipes/<int:recipe_id>/images/<int:image_id>"
# )


# Test route
class HelloWorld(Resource):
    def get(self):
        """
        This is an example endpoint that returns 'Hello, World!'
        ---
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "Hello, World!"
        """
        return jsonify({"message": "Hello, World!"})


api.add_resource(HelloWorld, "/hello")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
