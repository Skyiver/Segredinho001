import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'