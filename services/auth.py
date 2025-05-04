from flask_jwt_extended import JWTManager, create_access_token
from models import Professor  

jwt = JWTManager()

def configure_jwt(app):
    jwt.init_app(app)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Professor.query.get(identity)

def login_professor(email, senha):
    professor = Professor.query.filter_by(email=email).first()
    if professor and professor.verificar_senha(senha): 
        return create_access_token(identity=professor)
    return None