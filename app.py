from flask import Flask, jsonify
from config import Config
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma
from routes.alunos import alunos_bp, alunos_db
from routes.professores import professores_bp, professores_db
from routes.turmas import turmas_bp, turmas_db

app = Flask(__name__)
app.config.from_object(Config)

# Registrar blueprints
app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')

@app.route('/api/reseta', methods=['POST'])
def reset_sistema():
    try:
        alunos_db.clear()
        professores_db.clear()
        turmas_db.clear()
        
        Aluno.id_counter = 1
        Professor.id_counter = 1
        Turma.id_counter = 1
        
        return jsonify({"status": "sistema resetado"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )