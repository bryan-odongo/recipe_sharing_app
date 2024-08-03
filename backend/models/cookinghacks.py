from . import db, validates

class CookingHacks(db.Model):
    __tablename__ = 'cookinghacks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    @validates('content')
    def validate_content(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Content must be a non-empty string")
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'content': self.content
        }
    
    def __repr__(self):
        return f'<CookingHacks {self.content}, ID: {self.id}>'