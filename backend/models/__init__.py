from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from .user import User
from .recipes import Recipe
from .ingredients import Ingredient
from .replies import Replies
from .cookinghacks import CookingHacks
from .cookingtips import CookingTips
from .images import Image
from .review import Review
