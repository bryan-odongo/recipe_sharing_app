from flask_restful import Resource, reqparse
from database import db
from models import User
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

BLANK_ERROR = "'{}' cannot be blank."
USER_ALREADY_EXISTS = "A user with that username or email already exists."
CREATED_SUCCESSFULLY = "User created successfully."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User <id={user_id}> successfully logged out."

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", type=str, required=True, help=BLANK_ERROR.format("username")
)
_user_parser.add_argument(
    "password", type=str, required=True, help=BLANK_ERROR.format("password")
)
_user_parser.add_argument(
    "email", type=str, required=True, help=BLANK_ERROR.format("email")
)
_user_parser.add_argument(
    "first_name", type=str, required=True, help=BLANK_ERROR.format("first name")
)
_user_parser.add_argument(
    "last_name", type=str, required=True, help=BLANK_ERROR.format("last name")
)

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        
        try:
            user = User(
                username=data["username"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"]
            )
            user.password_hash = data["password"]  # The setter will handle hashing

            db.session.add(user)
            db.session.commit()
        except ValueError as e:
            return {"message":{"message": str(e)}}, 400
        except IntegrityError:
            db.session.rollback()
            return {"message":{"message": USER_ALREADY_EXISTS}}, 400
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message":{"message": str(e)}}, 500

        return {"message":{"message": CREATED_SUCCESSFULLY}}, 201

class Profile(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "user deleted"}), 200
