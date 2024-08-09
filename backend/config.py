import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key().decode()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', generate_key())
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'postgresql+psycopg2://Anthony:Gachie@localhost:5432/recipe_sharing')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'postgresql+psycopg2://Anthony:Gachie@localhost:5432/test_db')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://Anthony:Gachie@localhost:5432/recipe_sharing')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
