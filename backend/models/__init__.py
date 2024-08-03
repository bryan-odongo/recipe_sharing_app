from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates, relationship
from datetime import datetime
import re

from .user import User
from .recipes import Recipe
from .ingredients import Ingredient
from .replies import Replies
from .cookinghacks import CookingHacks
from .images import Image
from .review import Review

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
