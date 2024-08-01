from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)  # Scale from 1 to 5

    recipe = relationship("Recipe", back_populates="ratings")
    user = relationship("User", back_populates="ratings")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text)
    is_read = Column(Boolean, default=False)
    created_at = Column(String)

    user = relationship("User", back_populates="notifications")
