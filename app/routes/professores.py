from flask import Blueprint, jsonify, request
from app.models.professor import Professor

professores_bp = Blueprint('professores', __name__)
professores_db = {}

@professores_bp.route('/professores', methods=['GET'])
def get_professores():
    try:
        return jsonify([prof.to_dict() for prof in professores_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500