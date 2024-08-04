from flask_restful import Resource, reqparse
from models.recipe import Recipe
from models.engagement import Comment, CommentResponse, Rating
from models.user import UserModel
from database import db


class CommentResource(Resource):
    def get(self, recipe_id, comment_id):
        comment = Comment.query.filter_by(id=comment_id, recipe_id=recipe_id).first()
        if comment:
            return {
                "id": comment.id,
                "text": comment.text,
                "recipe_id": comment.recipe_id,
                "user_id": comment.user_id,
                "responses": [
                    {"id": response.id, "text": response.text}
                    for response in comment.responses
                ],
                "timestamp": comment.timestamp.isoformat(),
            }, 200
        return {"error": "Comment not found"}, 404

    def put(self, recipe_id, comment_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "text", type=str, required=True, help="Text cannot be blank!"
        )
        data = parser.parse_args()

        comment = Comment.query.filter_by(id=comment_id, recipe_id=recipe_id).first()
        if not comment:
            return {"error": "Comment not found"}, 404

        try:
            comment.text = data["text"]
            db.session.commit()
            return {
                "id": comment.id,
                "text": comment.text,
                "recipe_id": comment.recipe_id,
                "user_id": comment.user_id,
                "timestamp": comment.timestamp.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, recipe_id, comment_id):
        comment = Comment.query.filter_by(id=comment_id, recipe_id=recipe_id).first()
        if not comment:
            return {"error": "Comment not found"}, 404

        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted"}, 200


class CommentListResource(Resource):
    def post(self, recipe_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "text", type=str, required=True, help="Text cannot be blank!"
        )
        parser.add_argument(
            "user_id", type=int, required=True, help="User ID cannot be blank!"
        )
        data = parser.parse_args()

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        user = UserModel.query.get(data["user_id"])
        if not user:
            return {"error": "User not found"}, 404

        try:
            comment = Comment(
                text=data["text"], recipe_id=recipe_id, user_id=data["user_id"]
            )
            db.session.add(comment)
            db.session.commit()

            return {
                "id": comment.id,
                "text": comment.text,
                "recipe_id": comment.recipe_id,
                "user_id": comment.user_id,
                "timestamp": comment.timestamp.isoformat(),
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": "An unexpected error occurred"}, 500


class CommentResponseResource(Resource):
    def get(self, recipe_id, comment_id, response_id):
        response = CommentResponse.query.filter_by(
            id=response_id, comment_id=comment_id
        ).first()
        if response:
            return {
                "id": response.id,
                "text": response.text,
                "comment_id": response.comment_id,
                "user_id": response.user_id,
                "timestamp": response.timestamp.isoformat(),
            }, 200
        return {"error": "Response not found"}, 404

    def put(self, recipe_id, comment_id, response_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "text", type=str, required=True, help="Text cannot be blank!"
        )
        data = parser.parse_args()

        response = CommentResponse.query.filter_by(
            id=response_id, comment_id=comment_id
        ).first()
        if not response:
            return {"error": "Response not found"}, 404

        try:
            response.text = data["text"]
            db.session.commit()
            return {
                "id": response.id,
                "text": response.text,
                "comment_id": response.comment_id,
                "user_id": response.user_id,
                "timestamp": response.timestamp.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, recipe_id, comment_id, response_id):
        response = CommentResponse.query.filter_by(
            id=response_id, comment_id=comment_id
        ).first()
        if not response:
            return {"error": "Response not found"}, 404

        db.session.delete(response)
        db.session.commit()
        return {"message": "Response deleted"}, 200


class CommentResponseListResource(Resource):
    def post(self, recipe_id, comment_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "text", type=str, required=True, help="Text cannot be blank!"
        )
        parser.add_argument(
            "user_id", type=int, required=True, help="User ID cannot be blank!"
        )
        data = parser.parse_args()

        comment = Comment.query.get(comment_id)
        if not comment:
            return {"error": "Comment not found"}, 404

        user = UserModel.query.get(data["user_id"])
        if not user:
            return {"error": "User not found"}, 404

        try:
            response = CommentResponse(
                text=data["text"], comment_id=comment_id, user_id=data["user_id"]
            )
            db.session.add(response)
            db.session.commit()

            return {
                "id": response.id,
                "text": response.text,
                "comment_id": response.comment_id,
                "user_id": response.user_id,
                "timestamp": response.timestamp.isoformat(),
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": "An unexpected error occurred"}, 500


class RatingResource(Resource):
    def get(self, recipe_id, rating_id):
        rating = Rating.query.filter_by(id=rating_id, recipe_id=recipe_id).first()
        if not rating:
            return {"message": "Rating not found"}, 404
        return {
            "id": rating.id,
            "value": rating.value,
            "recipe_id": rating.recipe_id,
            "user_id": rating.user_id,
            "timestamp": rating.timestamp.isoformat(),
        }

    def put(self, recipe_id, rating_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "value", type=int, required=True, help="Rating value is required"
        )
        args = parser.parse_args()

        rating = Rating.query.filter_by(id=rating_id, recipe_id=recipe_id).first()
        if not rating:
            return {"message": "Rating not found"}, 404

        rating.value = args["value"]
        db.session.commit()

        return {"message": "Rating updated"}

    def delete(self, recipe_id, rating_id):
        rating = Rating.query.filter_by(id=rating_id, recipe_id=recipe_id).first()
        if not rating:
            return {"message": "Rating not found"}, 404

        db.session.delete(rating)
        db.session.commit()

        return {"message": "Rating deleted"}


class RatingListResource(Resource):
    def post(self, recipe_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "value", type=int, required=True, help="Rating value is required"
        )
        parser.add_argument(
            "user_id", type=int, required=True, help="User ID is required"
        )
        args = parser.parse_args()

        recipe = Recipe.query.get(recipe_id)
        user = UserModel.query.get(args["user_id"])

        if not recipe:
            return {"message": "Recipe not found"}, 404
        if not user:
            return {"message": "User not found"}, 404

        rating = Rating(
            value=args["value"], recipe_id=recipe_id, user_id=args["user_id"]
        )
        db.session.add(rating)
        db.session.commit()

        return {"message": "Rating created", "id": rating.id}, 201
