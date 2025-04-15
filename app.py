from flask import Flask, jsonify
from config import Config
from models import db
from routes.alunos import alunos_bp
from routes.professores import professores_bp
from routes.turmas import turmas_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')

@app.route('/api/reseta', methods=['POST'])
def reset_sistema():
    try:
        db.drop_all()
        db.create_all()
        return jsonify({"status": "sistema resetado"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )