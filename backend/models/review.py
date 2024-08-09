from backend.database import db

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)

    replies = db.relationship('Replies', back_populates='review')

    def to_dict(self):
        return{
            'id': self.id,
            'replies': [self.to_dict() for reply in self.replies]
        }