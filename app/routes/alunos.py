from flask import Blueprint, jsonify, request
from app.models.aluno import Aluno

alunos_bp = Blueprint('alunos', __name__)
alunos_db = {}

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    try:
        return jsonify([aluno.to_dict() for aluno in alunos_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Falta implementar outros métodos (POST, PUT, DELETE) seguindo o padrão com try/catch