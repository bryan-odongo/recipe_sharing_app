from flask import jsonify, request
from flask_restful import Resource
from backend.models.recipes import Recipe, db  

class RecipeResource(Resource):
    def get(self):
        try:
            recipes = Recipe.query.all() 
            return jsonify([recipe.to_dict() for recipe in recipes])  
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500

    def post(self):
        try:
            data = request.get_json()
            new_recipe = Recipe(
                user_id=data.get('user_id'),
                title=data.get('title'),
                description=data.get('description'),
                instructions=data.get('instructions'),
                country=data.get('country'),
                prep_time=data.get('prep_time'),
                cook_time=data.get('cook_time'),
                servings=data.get('servings'),
                diet=data.get('diet'),
                image_url=data.get('image_url'),
                skill_level=data.get('skill_level'),
                created_at=data.get('created_at')
            )
            db.session.add(new_recipe)
            db.session.commit()
            return jsonify(new_recipe.to_dict()), 201 
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500
