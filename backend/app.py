import secrets
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from database import db

# import resources


from config import sqliteConfig

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sqliteConfig
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = (
    f"a1d3c56531737{secrets.token_hex(2)}cf62bc36a7e30cd871d7{secrets.token_hex(2)}7b5b51e8208b8cef{secrets.token_hex(2)}c2689e8c0cb412b"
)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

CORS(app)

# create resources

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
