import secrets
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from database import db

from resources.user import (
    RegisterResource,
    LoginResource,
    ResetPasswordResource,
    UserResource,
    UserListResource,
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
swagger = swagger(app)

CORS(app)


# auth
api.add_resource(RegisterResource, "/api/auth/register")
api.add_resource(LoginResource, "/api/auth/login")
api.add_resource(ResetPasswordResource, "/auth/reset-password")
api.add_resource(UserResource, "/api/auth/users/<int:user_id>")
api.add_resource(UserListResource, "/api/auth/users")


# create resources
# Define a sample resource
class HelloWorld(Resource):
    def get(self):
        return jsonify({"message": "Hello, World!"})


# Add the resource to the API
api.add_resource(HelloWorld, "/hello")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
