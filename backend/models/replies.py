from . import db

class Replies(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    reply = db.Column(db.String)

    review = db.relationship('Review', back_populates='replies')

    def to_dict(self, include_review=False):
        data = {
            'id': self.id,
            'review_id': self.review_id,
            'reply': self.reply,
        }
        if include_review:
            data['review'] = self.review.to_dict() if self.review else None
        return data

    def __repr__(self):
        return f'<Replies {self.reply}, ID: {self.id}>'
