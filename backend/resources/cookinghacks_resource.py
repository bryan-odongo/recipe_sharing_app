from flask import jsonify, request, make_response
from flask_restful import Resource
from backend.models.cookinghacks import CookingHacks, db

class CookingHacksResource(Resource):

    def get(self):
        try:
            cookinghacks = CookingHacks.query.all()
            return jsonify([cookinghack.to_dict() for cookinghack in cookinghacks])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal server Error"}, 500

    def post(self):
        try: 
            new_cooking_hack = CookingHacks(
                content=request.form['content']
            )
            db.session.add(new_cooking_hack)
            db.session.commit()
            response_dict = new_cooking_hack.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response
        except KeyError as ke:
            print(f"Missing: {ke}")
            return make_response(jsonify({"error": f"Missing required field: {ke}"}), 400)
        except Exception as e:
            print(f"Error creating cooking hack: {e}")
            return make_response(jsonify({"error": "Unable to create cooking hack", "details": str(e)}), 500)


class CookinghacksByID(Resource):

    def get(self, id):
        response_dict = CookingHacks.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict, 200)
        return response

    def patch(self, id):
        record = CookingHacks.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Cooking hack not found"}), 404)
        
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
            return make_response(jsonify({"error": "Unable to update cooking hack", "details": str(e)}), 500)

    def delete(self, id):
        record = CookingHacks.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Cooking hack not found"}), 404)
        try:
            db.session.delete(record)
            db.session.commit()
            response_dict = {"message": "Cooking hack successfully delete"}
            response = make_response(response_dict, 200)
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "unable to delete cooking hack", "details": str(e)}), 500)