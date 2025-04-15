class Config:
    HOST = '0.0.0.0'
    PORT = 5002
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////code/db/app.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False