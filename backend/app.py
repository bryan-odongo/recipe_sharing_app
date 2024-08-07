import os
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from database import db
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, Login,  Profile

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    api = Api(app)

    
    api.add_resource(UserRegister, "/register")
    api.add_resource(Profile, "/profile")
    api.add_resource(Login, "/login")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
