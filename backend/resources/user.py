from datetime import timedelta
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
        """
        Register a new user.
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: NewUser
              required:
                - firstname
                - lastname
                - password
                - email
              properties:
                firstname:
                  type: string
                  description: The first name of the user
                lastname:
                  type: string
                  description: The last name of the user
                password:
                  type: string
                  description: The password for the user account
                email:
                  type: string
                  description: The email address of the user
                is_admin:
                  type: boolean
                  description: Whether the user is an admin or not
        responses:
          201:
            description: The newly created user
            schema:
              id: User
              properties:
                id:
                  type: integer
                  description: The user ID
                firstname:
                  type: string
                  description: The first name of the user
                lastname:
                  type: string
                  description: The last name of the user
                email:
                  type: string
                  description: The email address of the user
                is_admin:
                  type: boolean
                  description: Whether the user is an admin or not
            examples:
              application/json:
                id: 1
                firstname: "John"
                lastname: "Doe"
                email: "john.doe@example.com"
                is_admin: false
          400:
            description: Invalid input or email already in use
            examples:
              application/json:
                error: "Email already in use"
                error: "Invalid input"
        """
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
        """
        Log in a user and generate access and refresh tokens.
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: Login
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  description: The email address of the user
                password:
                  type: string
                  description: The password for the user account
        responses:
          200:
            description: Successful login with tokens
            schema:
              id: LoginSuccess
              properties:
                access_token:
                  type: string
                  description: JWT access token
                refresh_token:
                  type: string
                  description: JWT refresh token
                success:
                  type: string
                  description: Success message
            examples:
              application/json:
                access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNjMzNTY1MzI5LCJleHBpcmF0aW9uIjoxNjMzNTY4OTI5fQ.9Omb7S9KhA8xV8zVr6xZqL2PbR3ptlQERAI8eQkJ55g"
                refresh_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNjMzNTY1MzI5LCJleHBpcmF0aW9uIjoxNjMzNTY4OTI5fQ.9Omb7S9KhA8xV8zVr6xZqL2PbR3ptlQERAI8eQkJ55g"
                success: "Login successful"
          401:
            description: Invalid email or password
            examples:
              application/json:
                error: "Invalid email or password"
        """
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
            access_token = create_access_token(
                identity=user.id, expires_delta=timedelta(hours=1)
            )
            refresh_token = create_refresh_token(
                identity=user.id, expires_delta=timedelta(hours=1)
            )
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "success": "Login successful",
            }, 200
        return {"error": "Invalid email or password"}, 401


class ResetPasswordResource(Resource):
    def post(self):
        """
        Reset a user's password.
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: ResetPassword
              required:
                - email
                - new_password
              properties:
                email:
                  type: string
                  description: The email address of the user whose password is being reset
                new_password:
                  type: string
                  description: The new password for the user account
        responses:
          200:
            description: Password reset successful
            schema:
              id: ResetPasswordSuccess
              properties:
                success:
                  type: string
                  description: Success message
            examples:
              application/json:
                success: "Password reset successful"
          404:
            description: User not found
            examples:
              application/json:
                error: "User not found"
        """
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
    def get(self, identifier):
        """
        Get user details by user ID, username, or email.
        ---
        parameters:
          - name: identifier
            in: path
            type: string
            required: true
            description: The ID, username, or email of the user to retrieve
        responses:
          200:
            description: User details successfully retrieved
            schema:
              id: User
              properties:
                id:
                  type: integer
                  description: The ID of the user
                firstname:
                  type: string
                  description: The first name of the user
                lastname:
                  type: string
                  description: The last name of the user
                email:
                  type: string
                  description: The email of the user
                is_admin:
                  type: boolean
                  description: Whether the user is an admin
            examples:
              application/json:
                id: 1
                firstname: "John"
                lastname: "Doe"
                email: "john.doe@example.com"
                is_admin: false
          404:
            description: User not found
            examples:
              application/json:
                error: "User not found"
        """
        # Try to get the user by ID, username, or email
        if identifier.isdigit():
            user = UserModel.query.filter_by(id=int(identifier)).first()
        else:
            user = (
                # UserModel.query.filter_by(username=identifier).first() or
                UserModel.query.filter_by(email=identifier).first()
            )

        if user:
            return user.json()

        return {"error": "User not found"}, 404

        def put(self, user_id):
            """
            Update user details by user ID.
            ---
            parameters:
              - name: user_id
                in: path
                type: integer
                required: true
                description: The ID of the user to update
              - name: body
                in: body
                required: false
                schema:
                  id: UpdateUser
                  properties:
                    firstname:
                      type: string
                      description: The first name of the user
                    lastname:
                      type: string
                      description: The last name of the user
                    password:
                      type: string
                      description: The new password for the user
                    email:
                      type: string
                      description: The new email for the user
                    is_admin:
                      type: boolean
                      description: Whether the user should be an admin
            responses:
              200:
                description: User details successfully updated
                schema:
                  id: User
                  properties:
                    id:
                      type: integer
                      description: The ID of the user
                    firstname:
                      type: string
                      description: The first name of the user
                    lastname:
                      type: string
                      description: The last name of the user
                    email:
                      type: string
                      description: The email of the user
                    is_admin:
                      type: boolean
                      description: Whether the user is an admin
                examples:
                  application/json:
                    id: 1
                    firstname: "John"
                    lastname: "Doe"
                    email: "john.doe@example.com"
                    is_admin: false
              400:
                description: Bad request, validation error
                examples:
                  application/json:
                    message: "Validation error message"
              404:
                description: User not found
                examples:
                  application/json:
                    message: "User not found"
            """
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
                    firstname=data["firstname"],
                    lastname=data["lastname"],
                    password=data["password"],
                    email=data["email"],
                    is_admin=data["is_admin"],
                )
                if updated_user:
                    return updated_user.json()
                return {"message": "User not found"}, 404
            except ValueError as e:
                return {"message": str(e)}, 400

        def delete(self, user_id):
            """
            Delete a user by user ID.
            ---
            parameters:
              - name: user_id
                in: path
                type: integer
                required: true
                description: The ID of the user to delete
            responses:
              200:
                description: User successfully deleted
                schema:
                  id: SuccessMessage
                  properties:
                    message:
                      type: string
                      description: Success message
                examples:
                  application/json:
                    message: "User deleted"
              404:
                description: User not found
                examples:
                  application/json:
                    message: "User not found"
            """
            user = UserModel.get_user(user_id)
            if user:
                UserModel.delete_user(user_id)
                return {"message": "User deleted"}
            return {"message": "User not found"}, 404


class UserListResource(Resource):
    def get(self):
        """
        Get a list of all users.
        ---
        responses:
          200:
            description: A list of all users
            schema:
              type: array
              items:
                id: User
                properties:
                  id:
                    type: integer
                    description: The ID of the user
                  firstname:
                    type: string
                    description: The first name of the user
                  lastname:
                    type: string
                    description: The last name of the user
                  email:
                    type: string
                    description: The email of the user
                  is_admin:
                    type: boolean
                    description: Whether the user is an admin
            examples:
              application/json:
                - id: 1
                  firstname: "John"
                  lastname: "Doe"
                  email: "john.doe@example.com"
                  is_admin: false
                - id: 2
                  firstname: "Jane"
                  lastname: "Smith"
                  email: "jane.smith@example.com"
                  is_admin: true
        """
        users = UserModel.get_all_users()
        return [user.json() for user in users], 200
