from flask_restful import Resource, reqparse
from flask import request
from models.recipe import Recipe, Ingredient
from models.engagement import Comment
from models.user import UserModel
from database import db


class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = Recipe.query.get(recipe_id)
        if recipe:
            ratings = [rating.value for rating in recipe.ratings]
            average_rating = sum(ratings) / len(ratings) if ratings else 0
            return {
                "id": recipe.id,
                "title": recipe.title,
                "description": recipe.description,
                "instructions": recipe.instructions,
                "banner_image": recipe.banner_image,
                "user_id": recipe.user_id,
                "ingredients": [
                    {
                        "id": ingredient.id,
                        "name": ingredient.name,
                        "image": ingredient.image,
                        "quantity": ingredient.quantity,
                    }
                    for ingredient in recipe.ingredients
                ],
                "comments": [
                    {
                        "id": comment.id,
                        "text": comment.text,
                        "user_id": comment.user_id,
                        "recipe_id": comment.recipe_id,
                        "timestamp": comment.timestamp.isoformat(),
                    }
                    for comment in recipe.comments
                ],
                "ratings": average_rating,
            }, 200
        return {"error": "Recipe not found"}, 404

    def put(self, recipe_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="Title cannot be blank!"
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument("instructions", type=str, required=False)
        parser.add_argument("banner_image", type=str, required=False)
        parser.add_argument("ingredients", type=dict, action="append", required=False)
        data = parser.parse_args()

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        try:
            recipe.title = data["title"]
            recipe.description = data.get("description", recipe.description)
            recipe.instructions = data.get("instructions", recipe.instructions)
            recipe.banner_image = data.get("banner_image", recipe.banner_image)

            if data.get("ingredients") is not None:
                current_ingredients = {
                    ingredient.name: ingredient for ingredient in recipe.ingredients
                }

                for ingredient_data in data["ingredients"]:
                    name = ingredient_data.get("name")
                    if not name:
                        return {"error": "Ingredient name is required"}, 400

                    if name in current_ingredients:
                        ingredient = current_ingredients[name]
                        ingredient.image = ingredient_data.get(
                            "image", ingredient.image
                        )
                        ingredient.quantity = ingredient_data.get(
                            "quantity", ingredient.quantity
                        )
                    else:
                        ingredient = Ingredient(
                            name=name,
                            image=ingredient_data.get("image"),
                            quantity=ingredient_data.get("quantity"),
                            recipe=recipe,
                        )
                        db.session.add(ingredient)

                new_ingredient_names = {
                    ingredient["name"] for ingredient in data["ingredients"]
                }
                for ingredient_name in list(current_ingredients.keys()):
                    if ingredient_name not in new_ingredient_names:
                        db.session.delete(current_ingredients[ingredient_name])

            db.session.commit()
            return {
                "id": recipe.id,
                "title": recipe.title,
                "description": recipe.description,
                "instructions": recipe.instructions,
                "banner_image": recipe.banner_image,
                "user_id": recipe.user_id,
                "ingredients": [
                    {
                        "id": ingredient.id,
                        "name": ingredient.name,
                        "image": ingredient.image,
                        "quantity": ingredient.quantity,
                    }
                    for ingredient in recipe.ingredients
                ],
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, recipe_id):
        recipe = Recipe.query.get(recipe_id)
        if recipe:
            db.session.delete(recipe)
            db.session.commit()
            return {"message": "Recipe deleted"}, 200
        return {"error": "Recipe not found"}, 404

    def post(self):
        data = request.get_json()

        title = data.get("title")
        description = data.get("description")
        instructions = data.get("instructions")
        banner_image = data.get("banner_image")
        user_id = data.get("user_id")
        ingredients_data = data.get("ingredients", [])

        recipe = Recipe(
            title=title,
            description=description,
            instructions=instructions,
            banner_image=banner_image,
            user_id=user_id,
        )
        db.session.add(recipe)

        for ingredient_data in ingredients_data:
            ingredient = Ingredient(
                name=ingredient_data.get("name"),
                image=ingredient_data.get("image"),
                quantity=ingredient_data.get("quantity"),
                recipe=recipe,
            )
            db.session.add(ingredient)

        db.session.commit()

        return {
            "id": recipe.id,
            "title": recipe.title,
            "description": recipe.description,
            "instructions": recipe.instructions,
            "banner_image": recipe.banner_image,
            "user_id": recipe.user_id,
            "ingredients": [
                {
                    "id": ingredient.id,
                    "name": ingredient.name,
                    "image": ingredient.image,
                    "quantity": ingredient.quantity,
                }
                for ingredient in recipe.ingredients
            ],
        }, 201


class RecipeListResource(Resource):
    def get(self):
        recipes = Recipe.query.all()
        return [
            {
                "id": recipe.id,
                "title": recipe.title,
                "description": recipe.description,
                "instructions": recipe.instructions,
                "banner_image": recipe.banner_image,
                "user_id": recipe.user_id,
            }
            for recipe in recipes
        ], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="Title cannot be blank!"
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument("instructions", type=str, required=False)
        parser.add_argument("banner_image", type=str, required=False)
        parser.add_argument(
            "user_id", type=int, required=True, help="User ID is required"
        )
        parser.add_argument("ingredients", type=dict, action="append", required=False)
        data = parser.parse_args()

        user = UserModel.query.get(data["user_id"])
        if not user:
            return {"error": "User not found"}, 404

        try:
            new_recipe = Recipe(
                title=data["title"],
                description=data.get("description"),
                instructions=data.get("instructions"),
                banner_image=data.get("banner_image"),
                user_id=data["user_id"],
            )
            db.session.add(new_recipe)

            if data.get("ingredients"):
                for ingredient_data in data["ingredients"]:
                    if not ingredient_data.get("name"):
                        return {"error": "Ingredient name is required"}, 400
                    ingredient = Ingredient(
                        name=ingredient_data.get("name"),
                        image=ingredient_data.get("image"),
                        quantity=ingredient_data.get("quantity"),
                        recipe=new_recipe,
                    )
                    db.session.add(ingredient)

            db.session.commit()
            return {
                "id": new_recipe.id,
                "title": new_recipe.title,
                "description": new_recipe.description,
                "instructions": new_recipe.instructions,
                "banner_image": new_recipe.banner_image,
                "user_id": new_recipe.user_id,
                "ingredients": [
                    {
                        "id": ingredient.id,
                        "name": ingredient.name,
                        "image": ingredient.image,
                        "quantity": ingredient.quantity,
                    }
                    for ingredient in new_recipe.ingredients
                ],
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": "An unexpected error occurred"}, 500


class IngredientResource(Resource):
    def get(self, recipe_id, ingredient_id):
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        ingredient = Ingredient.query.filter_by(
            id=ingredient_id, recipe_id=recipe_id
        ).first()
        if ingredient:
            return {
                "id": ingredient.id,
                "name": ingredient.name,
                "image": ingredient.image,
                "quantity": ingredient.quantity,
            }, 200
        return {"error": "Ingredient not found"}, 404

    def put(self, recipe_id, ingredient_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="Name cannot be blank!"
        )
        parser.add_argument("image", type=str, required=False)
        parser.add_argument("quantity", type=str, required=False)
        data = parser.parse_args()

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        ingredient = Ingredient.query.filter_by(
            id=ingredient_id, recipe_id=recipe_id
        ).first()
        if not ingredient:
            return {"error": "Ingredient not found"}, 404

        try:
            ingredient.name = data["name"]
            ingredient.image = data.get("image", ingredient.image)
            ingredient.quantity = data.get("quantity", ingredient.quantity)

            db.session.commit()
            return {
                "id": ingredient.id,
                "name": ingredient.name,
                "image": ingredient.image,
                "quantity": ingredient.quantity,
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, recipe_id, ingredient_id):
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        ingredient = Ingredient.query.filter_by(
            id=ingredient_id, recipe_id=recipe_id
        ).first()
        if ingredient:
            db.session.delete(ingredient)
            db.session.commit()
            return {"message": "Ingredient deleted"}, 200
        return {"error": "Ingredient not found"}, 404
