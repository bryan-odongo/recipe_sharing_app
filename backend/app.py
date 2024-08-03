from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from .models import db
from .config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    return app

if __name__ == '__main__)':
    import os
    config_name = os.getenv('FLASK_CONFIG', 'default')
    app = create_app(config_name)
    app.run(port=555)