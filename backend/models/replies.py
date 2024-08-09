from backend.database import db

class Replies(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    reply = db.Column(db.String(1000))

    review = db.relationship('Review', back_populates='replies')

    def to_dict(self, include_review=False):
        data = {
            'id': self.id,
            'reply': self.reply,
            'review': self.review.to_dict() if self.review else None
        }
        if include_review:
            data['review'] = self.review.to_dict() if self.review else None
        return data

    def __repr__(self):
        return f'<Replies {self.reply}, ID: {self.id}>'
