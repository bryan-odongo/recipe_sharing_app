from . import db, validates

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes'), nullable=False)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)

    recipe = db.Relationship('Recipe', back_populates='ingredient')

    @validates('name')
    def validate_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Name must be a non-empty string')
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'recipe_id': self.recipe_id
        }
    
    def __repr__(self):
        return f'<Ingredient {self.name}, ID: {self.id}>'