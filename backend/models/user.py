from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    role_name = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("user_roles.id"))

    role = relationship("UserRole")

    @validates("firstname")
    def validate_firstname(self, key, firstname):
        if not firstname:
            raise ValueError("First name is required.")
        return firstname

    @validates("lastname")
    def validate_lastname(self, key, lastname):
        if not lastname:
            raise ValueError("Last name is required.")
        return lastname

    @validates("email")
    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email is required.")
        if User.query.filter_by(email=email).first():
            raise ValueError("The email is already in use.")
        return email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_user(cls, firstname, lastname, password, email, role_id):
        new_user = cls(
            firstname=firstname, lastname=lastname, email=email, role_id=role_id
        )
        new_user.set_password(password)
        return new_user

    def json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "is_active": self.is_active,
        }


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bio = Column(String(256))
    profile_picture_id = Column(Integer, ForeignKey("images.id"))

    user = relationship("User", back_populates="profiles")


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    user = relationship("User", back_populates="favorites")
