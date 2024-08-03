from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

from database import db


class RegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "firstname", type=str, required=True, help="First name cannot be blank!"
        )
        parser.add_argument(
            "lastname", type=str, required=True, help="Last name cannot be blank!"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password cannot be blank!"
        )
        parser.add_argument(
            "email", type=str, required=True, help="Email cannot be blank!"
        )
        parser.add_argument(
            "is_admin", type=bool, required=False, default=False, help="Is admin flag"
        )
        data = parser.parse_args()

        if UserModel.get_user_by_email(data["email"]):
            return {"error": "Email already in use"}, 400

        try:
            new_user = UserModel.create_user(
                data["firstname"],
                data["lastname"],
                data["password"],
                data["email"],
                data["is_admin"],
            )
            return new_user.json(), 201
        except ValueError as e:
            return {"error": str(e)}, 400


class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "email", type=str, required=True, help="Email cannot be blank!"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password cannot be blank!"
        )
        data = parser.parse_args()

        user = UserModel.get_user_by_email(data["email"])
        if user and user.check_password(data["password"]):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "success": "Login successful",
            }, 200
        return {"error": "Invalid email or password"}, 401


class ResetPasswordResource(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "email", type=str, required=True, help="Email cannot be blank!"
        )
        parser.add_argument(
            "new_password",
            type=str,
            required=True,
            help="New password cannot be blank!",
        )
        data = parser.parse_args()

        user = UserModel.get_user_by_email(data["email"])
        if not user:
            return {"error": "User not found"}, 404

        user.set_password(data["new_password"])
        db.session.commit()
        return {"success": "Password reset successful"}, 200


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = UserModel.get_user(user_id)
        if user:
            return user.json()
        return {"error": "User not found"}, 404

    @jwt_required()
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str)
        parser.add_argument("lastname", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("is_admin", type=bool)
        data = parser.parse_args()

        try:
            updated_user = UserModel.update_user(
                user_id,
                data["firstname"],
                data["lastname"],
                data["password"],
                data["email"],
                data["is_admin"],
            )
            if updated_user:
                return updated_user.json()
            return {"message": "User not found"}, 404
        except ValueError as e:
            return {"message": str(e)}, 400

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.get_user(user_id)
        if user:
            UserModel.delete_user(user_id)
            return {"message": "User deleted"}
        return {"message": "User not found"}, 404


class UserListResource(Resource):
    @jwt_required()
    def get(self):
        users = UserModel.get_all_users()
        return [user.json() for user in users], 200
