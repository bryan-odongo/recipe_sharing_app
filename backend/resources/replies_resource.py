from flask import jsonify, request, make_response
from flask_restful import Resource
from backend.models.review import Review
from backend.models.replies import Replies, db

class RepliesResource(Resource):

    def get(self):
        try:
            replies = Replies.query.all()
            return jsonify([reply.to_dict() for reply in replies])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500
        
    def post(self):
        try:
            review_id = request.form.get('review_id')
            reply = request.form.get('reply')

            if not review_id or not reply:
                return make_response(jsonify({"error": "Missing required field: review_id and reply"}), 400)
            
            review = Review.query.get(review_id)

            if not review:
                return make_response(jsonify({"error": "Review not found"}), 404)
            new_reply = Replies(
                review_id=review_id,
                reply=reply
            )
            db.session.add(new_reply)
            db.session.commit()
            response_dict = new_reply.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response
        except KeyError as ke:
            print(f"Missing key: {ke}")
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        except Exception as e:
            print(f"Error creating ingredient: {e}")
            return make_response(jsonify({"error": "Unable to create ingredient", "details": str(e)}), 500)
        
class RepliesByID(Resource):

    def get(self, id):
        response_dict = Replies.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict,200)
        return response
    
    def patch(self, id):
        record = Replies.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Reply not found"}), 404)
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
            return make_response(jsonify({"error": "Unable to update reply", "details": str(e)}), 500)
        
    def delete(self, id):
        record = Replies.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Reply not found"}), 404)
        try:
            db.session.delete(record)
            db.session.commit()
            response_dict = {"message": "Reply successfully deleted"}
            response = make_response(response_dict, 200)
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to delete reply", "details": str(e)}), 500)
