import os

class Config:
    # Configuração do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configuração do JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'senha-super-secreta')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600)) 
    
    HOST = '0.0.0.0'
    PORT = 5002
    DEBUG = True
    
class TestConfig(Config):
    TESTING = True
    JWT_SECRET_KEY = 'senha'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'