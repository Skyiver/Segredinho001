import os

class Config:
    # Configuração do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    HOST = '0.0.0.0'
    PORT = 5002
    DEBUG = True