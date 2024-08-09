from datetime import datetime
from flask import jsonify, request, make_response
from flask_restful import Resource
from backend.models.cookingtips import CookingTips
from backend.database import db

class CookingTipsResource(Resource):

    def get(self):
        try:
            cookingtips = CookingTips.query.all()
            return jsonify([cookingtip.to_dict() for cookingtip in cookingtips])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal server error"}, 500
        
    def post(self):
        try:
            created_at_str = request.form.get('created_at')
            created_at = datetime.fromisoformat(created_at_str) if created_at_str else datetime.now()


            update_at_str = request.form.get('updated_at')
            updated_at = datetime.fromisoformat(update_at_str) if update_at_str else datetime.now()
            
            new_cooking_tip = CookingTips(
                title=request.form['title'],
                content=request.form['content'],
                created_at=created_at,
                updated_at=updated_at
            )
            db.session.add(new_cooking_tip)
            db.session.commit()
            response_dict = new_cooking_tip.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response
        except KeyError as ke:
            print(f"Missing: {ke}")
            return make_response(jsonify({"error": f"Missing required field: {ke}"}), 400)
        except Exception as e:
            print(f"Error creating cooking hack: {e}")
            return make_response(jsonify({"error": "unable to create cooking tip", "details": str(e)}), 500)
        

class CookingTipsByID(Resource):

    def get(self, id):
        response_dict = CookingTips.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict, 200)
        return response
    
    def patch(self, id):
        record = CookingTips.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Cooking tip not found"}), 404)
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "Invalid data format"}), 400)
        for attr, value in data.items():
            if attr in ["created_at", "updated_at"] and value:
                try:
                    value = datetime.fromisoformat(value)
                except ValueError:
                    return make_response(jsonify({"error": "Invalid date format"}), 400)
            if hasattr(record, attr):
                setattr(record, attr, value)
        try:
            db.session.add(record)
            db.session.commit()
            response_dict = record.to_dict()
            return make_response(jsonify(response_dict), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to update cooking tip", "details": str(e)}), 500)

    def delete(self, id):
        record = CookingTips.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Cooking tip not found"}), 404)
        try:
            db.session.delete(record)
            db.session.commit()

            response_dict = {"message": "cooking tip successfully deleted"}

            response = make_response(
                response_dict,
                200
            )
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to delete cooking tip", "details": str(e)}), 500)