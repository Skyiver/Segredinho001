from flask import Blueprint, jsonify, request
from app.models.turma import Turma

turmas_bp = Blueprint('turmas', __name__)
turmas_db = {}

@turmas_bp.route('/turmas', methods=['GET'])
def get_turmas():
    try:
        return jsonify([turma.to_dict() for turma in turmas_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500