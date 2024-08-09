from flask import jsonify, request, make_response
from flask_restful import Resource
from backend.models.images import Image
from backend.database import db

class ImagesResource(Resource):

    def get(self):
        try:
            images = Image.query.all()
            return jsonify([image.to_dict() for image in images])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500
        
    def post(self):
        try:
            recipe_id = request.form.get('recipe_id')
            image_url = request.form.get('image_url')
            
            if recipe_id is None or image_url is None:
                return make_response(jsonify({"error": "Missing required fields: recipe_id and image_url"}), 400)
            
            new_image = Image(
                recipe_id=recipe_id,
                image_url=image_url
            )
            
            db.session.add(new_image)
            db.session.commit()
            
            response_dict = new_image.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response
        except KeyError as ke:
            print(f"Missing key: {ke}")
            return make_response(jsonify({"error": "Missing required field"}), 400)
        except Exception as e:
            print(f"Error creating image: {e}")
            return make_response(jsonify({"error": "Unable to create image", "details": str(e)}), 500)
        
class ImagesByID(Resource):

    def get(self, id):
        response_dict = Image.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict, 200)
        return response
    
    def patch(self, id):
        record = Image.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Image not found"}), 404)
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
            return make_response(jsonify({"error": "Unable to update image", "details": str(e)}), 500)
        
    def delete(self, id):
        record = Image.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Image not found"}), 404)
        try:
            db.session.delete(record)
            db.session.commit()
            response_dict = {"message": "Image successfully deleted"}
            response = make_response(response_dict, 200)
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to delete image", "details": str(e)}), 500)