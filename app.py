from flask import Flask, jsonify
from config import Config
from bd import db
from routes.alunos import alunos_bp
from routes.professores import professores_bp
from routes.turmas import turmas_bp
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

def create_app():
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
            db.session.query(Aluno).delete()
            db.session.query(Professor).delete()
            db.session.query(Turma).delete()
            db.session.execute("DELETE FROM sqlite_sequence WHERE name='alunos'")
            db.session.execute("DELETE FROM sqlite_sequence WHERE name='professores'")
            db.session.execute("DELETE FROM sqlite_sequence WHERE name='turmas'")
            db.session.commit()
            return jsonify({"status": "sistema resetado"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"erro": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT)