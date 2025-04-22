from flask import Flask, jsonify
import time
from sqlalchemy.exc import OperationalError
from config import Config
from bd import db
from routes.alunos import alunos_bp
from routes.professores import professores_bp
from routes.turmas import turmas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            with app.app_context():
                db.create_all()
                break
        except OperationalError as e:
            retry_count += 1
            print(f"Tentativa {retry_count}/{max_retries} - Banco de dados não está pronto...")
            time.sleep(2)
            if retry_count == max_retries:
                raise RuntimeError("Não foi possível conectar ao banco de dados após várias tentativas") from e

    # Blueprints
    app.register_blueprint(alunos_bp, url_prefix='/api')
    app.register_blueprint(professores_bp, url_prefix='/api')
    app.register_blueprint(turmas_bp, url_prefix='/api')

    # Rota de reset
    @app.route('/api/reseta', methods=['POST'])
    def reset_sistema():
        try:
            with app.app_context():
                db.drop_all()
                db.create_all()
                return jsonify({"status": "sistema resetado"}), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )