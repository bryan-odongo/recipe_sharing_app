from flask_restful import Resource, reqparse
from flask import request
from models.recipe import Recipe, Ingredient, OtherRecipeImages
from models.user import UserModel
from database import db


class RecipeResource(Resource):
    def get(self, recipe_id):
        """
        Retrieve a specific recipe by ID.
        ---
        parameters:
          - name: recipe_id
            in: path
            required: true
            type: integer
            description: The ID of the recipe to retrieve
        responses:
          200:
            description: The recipe details
            schema:
              id: Recipe
              properties:
                id:
                  type: integer
                  description: The recipe ID
                title:
                  type: string
                  description: The title of the recipe
                description:
                  type: string
                  description: A short description of the recipe
                instructions:
                  type: string
                  description: The instructions for the recipe
                banner_image:
                  type: string
                  description: The URL of the recipe's banner image
                user_id:
                  type: integer
                  description: The ID of the user who created the recipe
                other_images:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The image ID
                      image:
                        type: string
                        description: The URL of the image
                ingredients:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The ingredient ID
                      name:
                        type: string
                        description: The name of the ingredient
                      image:
                        type: string
                        description: The URL of the ingredient image
                      quantity:
                        type: string
                        description: The quantity of the ingredient
                comments:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The comment ID
                      text:
                        type: string
                        description: The text of the comment
                      user_id:
                        type: integer
                        description: The ID of the user who made the comment
                      recipe_id:
                        type: integer
                        description: The ID of the recipe the comment belongs to
                      responses:
                        type: integer
                        description: The number of responses to the comment
                      timestamp:
                        type: string
                        description: The timestamp of the comment
                ratings:
                  type: number
                  description: The average rating of the recipe
            examples:
              application/json:
                id: 1
                title: "Spaghetti Carbonara"
                description: "A classic Italian pasta dish"
                instructions: "Boil pasta, fry pancetta, mix with eggs and cheese"
                banner_image: "http://example.com/image1.jpg"
                user_id: 1
                other_images:
                  - id: 1
                    image: "http://example.com/image2.jpg"
                ingredients:
                  - id: 1
                    name: "Spaghetti"
                    image: "http://example.com/image3.jpg"
                    quantity: "200g"
                comments:
                  - id: 1
                    text: "Great recipe!"
                    user_id: 1
                    recipe_id: 1
                    responses: 2
                    timestamp: "2024-08-04T12:00:00"
                ratings: 4.5
          404:
            description: Recipe not found
            examples:
              application/json:
                error: "Recipe not found"
        """
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
                "other_images": [
                    {
                        "id": image.id,
                        "image": image.image,
                    }
                    for image in recipe.other_images
                ],
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
                        "responses": len(comment.responses),
                        "timestamp": comment.timestamp.isoformat(),
                    }
                    for comment in recipe.comments
                ],
                "ratings": average_rating,
            }, 200
        return {"error": "Recipe not found"}, 404

    def put(self, recipe_id):
        """
        Update an existing recipe by ID.
        ---
        parameters:
          - name: recipe_id
            in: path
            required: true
            type: integer
            description: The ID of the recipe to update
          - name: body
            in: body
            required: true
            schema:
              id: UpdateRecipe
              properties:
                title:
                  type: string
                  description: The title of the recipe
                description:
                  type: string
                  description: A short description of the recipe
                instructions:
                  type: string
                  description: The instructions for the recipe
                banner_image:
                  type: string
                  description: The URL of the recipe's banner image
                ingredients:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: The name of the ingredient
                      image:
                        type: string
                        description: The URL of the ingredient image
                      quantity:
                        type: string
                        description: The quantity of the ingredient
        responses:
          200:
            description: The updated recipe
            schema:
              id: Recipe
              properties:
                id:
                  type: integer
                  description: The recipe ID
                title:
                  type: string
                  description: The title of the recipe
                description:
                  type: string
                  description: A short description of the recipe
                instructions:
                  type: string
                  description: The instructions for the recipe
                banner_image:
                  type: string
                  description: The URL of the recipe's banner image
                user_id:
                  type: integer
                  description: The ID of the user who created the recipe
                ingredients:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The ingredient ID
                      name:
                        type: string
                        description: The name of the ingredient
                      image:
                        type: string
                        description: The URL of the ingredient image
                      quantity:
                        type: string
                        description: The quantity of the ingredient
            examples:
              application/json:
                id: 1
                title: "Spaghetti Carbonara"
                description: "A classic Italian pasta dish"
                instructions: "Boil pasta, fry pancetta, mix with eggs and cheese"
                banner_image: "http://example.com/image1.jpg"
                user_id: 1
                ingredients:
                  - id: 1
                    name: "Spaghetti"
                    image: "http://example.com/image3.jpg"
                    quantity: "200g"
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: Recipe not found
            examples:
              application/json:
                error: "Recipe not found"
        """
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
        """
        Delete a recipe by ID.
        ---
        parameters:
          - name: recipe_id
            in: path
            required: true
            type: integer
            description: The ID of the recipe to delete
        responses:
          200:
            description: Recipe deleted
            examples:
              application/json:
                message: "Recipe deleted"
          404:
            description: Recipe not found
            examples:
              application/json:
                error: "Recipe not found"
        """
        recipe = Recipe.query.get(recipe_id)
        if recipe:
            db.session.delete(recipe)
            db.session.commit()
            return {"message": "Recipe deleted"}, 200
        return {"error": "Recipe not found"}, 404


class RecipeListResource(Resource):
    def get(self):
        """
        Retrieve all recipes.
        ---
        responses:
          200:
            description: A list of all recipes
            schema:
              type: array
              items:
                id: Recipe
                properties:
                  id:
                    type: integer
                    description: The recipe ID
                  title:
                    type: string
                    description: The title of the recipe
                  description:
                    type: string
                    description: A short description of the recipe
                  instructions:
                    type: string
                    description: The instructions for the recipe
                  banner_image:
                    type: string
                    description: The URL of the recipe's banner image
                  user_id:
                    type: integer
                    description: The ID of the user who created the recipe
            examples:
              application/json:
                - id: 1
                  title: "Spaghetti Carbonara"
                  description: "A classic Italian pasta dish"
                  instructions: "Boil pasta, fry pancetta, mix with eggs and cheese"
                  banner_image: "http://example.com/image1.jpg"
                  user_id: 1
                - id: 2
                  title: "Chicken Curry"
                  description: "A spicy and savory chicken curry"
                  instructions: "Cook chicken, add spices, simmer with coconut milk"
                  banner_image: "http://example.com/image2.jpg"
                  user_id: 2
        """
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
        """
        Create a new recipe.
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: NewRecipe
              required:
                - title
                - user_id
              properties:
                title:
                  type: string
                  description: The title of the recipe
                description:
                  type: string
                  description: A short description of the recipe
                instructions:
                  type: string
                  description: The instructions for the recipe
                banner_image:
                  type: string
                  description: The URL of the recipe's banner image
                user_id:
                  type: integer
                  description: The ID of the user who created the recipe
                ingredients:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: The name of the ingredient
                      image:
                        type: string
                        description: The URL of the ingredient image
                      quantity:
                        type: string
                        description: The quantity of the ingredient
        responses:
          201:
            description: The created recipe
            schema:
              id: Recipe
              properties:
                id:
                  type: integer
                  description: The recipe ID
                title:
                  type: string
                  description: The title of the recipe
                description:
                  type: string
                  description: A short description of the recipe
                instructions:
                  type: string
                  description: The instructions for the recipe
                banner_image:
                  type: string
                  description: The URL of the recipe's banner image
                user_id:
                  type: integer
                  description: The ID of the user who created the recipe
                ingredients:
                  type: array
                  items:
                    id: Ingredient
                    properties:
                      id:
                        type: integer
                        description: The ingredient ID
                      name:
                        type: string
                        description: The name of the ingredient
                      image:
                        type: string
                        description: The URL of the ingredient image
                      quantity:
                        type: string
                        description: The quantity of the ingredient
            examples:
              application/json:
                id: 1
                title: "Spaghetti Carbonara"
                description: "A classic Italian pasta dish"
                instructions: "Boil pasta, fry pancetta, mix with eggs and cheese"
                banner_image: "http://example.com/image1.jpg"
                user_id: 1
                ingredients:
                  - id: 1
                    name: "Spaghetti"
                    image: "http://example.com/image3.jpg"
                    quantity: "200g"
                  - id: 2
                    name: "Pancetta"
                    image: "http://example.com/image4.jpg"
                    quantity: "100g"
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: User not found
            examples:
              application/json:
                error: "User not found"
          500:
            description: An unexpected error occurred
            examples:
              application/json:
                error: "An unexpected error occurred"
        """
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
        """
        Get an ingredient associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: ingredient_id
            in: path
            type: integer
            required: true
            description: The ID of the ingredient
        responses:
          200:
            description: A successful response
            schema:
              id: Ingredient
              properties:
                id:
                  type: integer
                  description: The ingredient ID
                name:
                  type: string
                  description: The name of the ingredient
                image:
                  type: string
                  description: The URL of the ingredient image
                quantity:
                  type: string
                  description: The quantity of the ingredient
            examples:
              application/json:
                id: 1
                name: "Sugar"
                image: "http://example.com/image1.jpg"
                quantity: "100g"
          404:
            description: Ingredient not found
            examples:
              application/json:
                error: "Ingredient not found"
        """
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
        """
        Update an ingredient associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: ingredient_id
            in: path
            type: integer
            required: true
            description: The ID of the ingredient
          - name: body
            in: body
            required: true
            schema:
              id: UpdateIngredient
              required:
                - name
              properties:
                name:
                  type: string
                  description: The new name of the ingredient
                image:
                  type: string
                  description: The new URL of the ingredient image
                quantity:
                  type: string
                  description: The new quantity of the ingredient
        responses:
          200:
            description: A successful response
            schema:
              id: Ingredient
              properties:
                id:
                  type: integer
                  description: The ingredient ID
                name:
                  type: string
                  description: The name of the ingredient
                image:
                  type: string
                  description: The URL of the ingredient image
                quantity:
                  type: string
                  description: The quantity of the ingredient
            examples:
              application/json:
                id: 1
                name: "Brown Sugar"
                image: "http://example.com/image2.jpg"
                quantity: "200g"
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: Ingredient not found
            examples:
              application/json:
                error: "Ingredient not found"
        """
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
        """
        Delete an ingredient associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: ingredient_id
            in: path
            type: integer
            required: true
            description: The ID of the ingredient
        responses:
          200:
            description: A successful response
            examples:
              application/json:
                message: "Ingredient deleted"
          404:
            description: Ingredient not found
            examples:
              application/json:
                error: "Ingredient not found"
        """
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


class IngredientListResource(Resource):
    def post(self, recipe_id):
        """
        Add a new ingredient to a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: body
            in: body
            required: true
            schema:
              id: NewIngredient
              required:
                - name
              properties:
                name:
                  type: string
                  description: The name of the ingredient
                image:
                  type: string
                  description: The URL of the ingredient image
                quantity:
                  type: string
                  description: The quantity of the ingredient
        responses:
          201:
            description: A successful response
            schema:
              id: Ingredient
              properties:
                id:
                  type: integer
                  description: The ingredient ID
                name:
                  type: string
                  description: The name of the ingredient
                image:
                  type: string
                  description: The URL of the ingredient image
                quantity:
                  type: string
                  description: The quantity of the ingredient
            examples:
              application/json:
                id: 1
                name: "Sugar"
                image: "http://example.com/image1.jpg"
                quantity: "100g"
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: Recipe not found
            examples:
              application/json:
                error: "Recipe not found"
        """
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

        try:
            new_ingredient = Ingredient(
                name=data["name"],
                image=data.get("image"),
                quantity=data.get("quantity"),
                recipe_id=recipe_id,
            )
            db.session.add(new_ingredient)
            db.session.commit()

            return {
                "id": new_ingredient.id,
                "name": new_ingredient.name,
                "image": new_ingredient.image,
                "quantity": new_ingredient.quantity,
                "recipe_id": new_ingredient.recipe_id,
            }, 201
        except Exception as e:
            return {"error": str(e)}, 400


class OtherRecipeImageResource(Resource):
    def get(self, recipe_id, image_id):
        """
        Get an image associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: image_id
            in: path
            type: integer
            required: true
            description: The ID of the image
        responses:
          200:
            description: A successful response
            schema:
              id: OtherRecipeImage
              properties:
                id:
                  type: integer
                  description: The image ID
                image:
                  type: string
                  description: The URL of the image
                recipe_id:
                  type: integer
                  description: The ID of the recipe
            examples:
              application/json:
                id: 1
                image: "http://example.com/image1.jpg"
                recipe_id: 12
          404:
            description: Image not found
            examples:
              application/json:
                error: "Image not found"
        """
        image = OtherRecipeImages.query.filter_by(
            id=image_id, recipe_id=recipe_id
        ).first()
        if image:
            return {
                "id": image.id,
                "image": image.image,
                "recipe_id": image.recipe_id,
            }, 200
        return {"error": "Image not found"}, 404

    def put(self, recipe_id, image_id):
        """
        Update an image associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: image_id
            in: path
            type: integer
            required: true
            description: The ID of the image
          - name: body
            in: body
            required: true
            schema:
              id: UpdateOtherRecipeImage
              required:
                - image
              properties:
                image:
                  type: string
                  description: The new URL of the image
        responses:
          200:
            description: A successful response
            schema:
              id: OtherRecipeImage
              properties:
                id:
                  type: integer
                  description: The image ID
                image:
                  type: string
                  description: The URL of the image
                recipe_id:
                  type: integer
                  description: The ID of the recipe
            examples:
              application/json:
                id: 1
                image: "http://example.com/image2.jpg"
                recipe_id: 12
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: Image not found
            examples:
              application/json:
                error: "Image not found"
        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "image", type=str, required=True, help="Image URL cannot be blank!"
        )
        data = parser.parse_args()

        image = OtherRecipeImages.query.filter_by(
            id=image_id, recipe_id=recipe_id
        ).first()
        if not image:
            return {"error": "Image not found"}, 404

        try:
            image.image = data["image"]
            db.session.commit()
            return {
                "id": image.id,
                "image": image.image,
                "recipe_id": image.recipe_id,
            }, 200
        except Exception as e:
            return {"error": str(e)}, 400

    def delete(self, recipe_id, image_id):
        """
        Delete an image associated with a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: image_id
            in: path
            type: integer
            required: true
            description: The ID of the image
        responses:
          200:
            description: A successful response
            examples:
              application/json:
                message: "Image deleted"
          404:
            description: Image not found
            examples:
              application/json:
                error: "Image not found"
        """
        image = OtherRecipeImages.query.filter_by(
            id=image_id, recipe_id=recipe_id
        ).first()
        if not image:
            return {"error": "Image not found"}, 404

        db.session.delete(image)
        db.session.commit()
        return {"message": "Image deleted"}, 200


class OtherRecipeImageListResource(Resource):
    def post(self, recipe_id):
        """
        Add a new image to a specific recipe.
        ---
        parameters:
          - name: recipe_id
            in: path
            type: integer
            required: true
            description: The ID of the recipe
          - name: body
            in: body
            required: true
            schema:
              id: NewOtherRecipeImage
              required:
                - image
              properties:
                image:
                  type: string
                  description: The URL of the image
        responses:
          201:
            description: A successful response
            schema:
              id: OtherRecipeImage
              properties:
                id:
                  type: integer
                  description: The image ID
                image:
                  type: string
                  description: The URL of the image
                recipe_id:
                  type: integer
                  description: The ID of the recipe
            examples:
              application/json:
                id: 1
                image: "http://example.com/image1.jpg"
                recipe_id: 12
          400:
            description: Invalid input
            examples:
              application/json:
                error: "Invalid input"
          404:
            description: Recipe not found
            examples:
              application/json:
                error: "Recipe not found"
        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "image", type=str, required=True, help="Image URL cannot be blank!"
        )
        data = parser.parse_args()

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"error": "Recipe not found"}, 404

        try:
            new_image = OtherRecipeImages(image=data["image"], recipe_id=recipe_id)
            db.session.add(new_image)
            db.session.commit()

            return {
                "id": new_image.id,
                "image": new_image.image,
                "recipe_id": new_image.recipe_id,
            }, 201
        except Exception as e:
            return {"error": str(e)}, 400
