from flask import jsonify, request, make_response
from flask_restful import Resource
from backend.models.recipes import Recipe
from backend.models.ingredients import Ingredient, db

class IngredientsResource(Resource):

    def get(self):
        try:
            ingredients = Ingredient.query.all()
            return jsonify([ingredient.to_dict() for ingredient in ingredients])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500
        
    def post(self):
        try:
            recipe_id = request.form.get('recipe_id')
            name = request.form.get('name')
            image = request.form.get('image')

            if not recipe_id or not image or not name:
                return make_response(jsonify({"error": "Missing required fields: recipe_id, image, and name"}), 400)

            recipe = Recipe.query.get(recipe_id)
            
            if not recipe:
                return make_response(jsonify({"error": "Recipe not found"}), 404)
            new_ingredient = Ingredient(
                recipe_id=recipe_id,
                name=name,
                image=image
            )
            db.session.add(new_ingredient)
            db.session.commit()
            response_dict = new_ingredient.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response
        except KeyError as ke:
            print(f"Missing key: {ke}")
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        except Exception as e:
            print(f"Error creating ingredient: {e}")
            return make_response(jsonify({"error": "Unable to create ingredient", "details": str(e)}), 500)

class IngredientsByID(Resource):

    def get(self, id):
        response_dict = Ingredient.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict, 200)
        return response
    
    def patch(self, id):
        record = Ingredient.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Ingredient not found"}), 404)
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "Invalid data format"}), 400)
        for attr, value in data.items():
            if hasattr(record, attr):
                setattr(record, attr, value)
        try: 
            db.session.add(record)
            db.session.commit()
            response_dict = record.to_dict()
            return make_response(jsonify(response_dict), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to update ingredient", "details": str(e)}), 500)
        
    def delete(self, id):
        record = Ingredient.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Ingredient not found"}), 404)
        try:
            db.session.delete(record)
            db.session.commit()
            response_dict = {"message": "Ingredient successfully deleted"}
            response = make_response(response_dict, 200)
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to delete ingredient", "details": str(e)}), 500)
