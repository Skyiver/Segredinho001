from flask import Flask
from app.config import DevelopmentConfig
from app.routes import alunos_bp, professores_bp, turmas_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Registrar Blueprints
    app.register_blueprint(alunos_bp, url_prefix='/api')
    app.register_blueprint(professores_bp, url_prefix='/api')
    app.register_blueprint(turmas_bp, url_prefix='/api')

    # Rota de reset
    @app.route('/api/reseta', methods=['POST'])
    def reset_data():
        try:
            # Lógica para resetar dados
            return '', 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    return app

# Aparentemente isso tudo meio que é uma App Factory. Sinto que preciso estudar melhor isso