from flask import Flask
from config import Config
from models import db
from routes.alunos import alunos_bp
from routes.professores import professores_bp
from routes.turmas import turmas_bp
from utils.reset_routes import reset_bp  

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')
app.register_blueprint(reset_bp, url_prefix='/api') 

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )