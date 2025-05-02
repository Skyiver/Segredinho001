from flask import Blueprint, jsonify, request
from models import Professor
from services.professor_service import ProfessorService

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def listar_professores():
    try:
        professores = Professor.query.all()
        return jsonify([p.to_dict() for p in professores]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json() or {}
        professor = ProfessorService.criar_professor(data)
        return jsonify(professor.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    try:
        professor = Professor.query.get(id)
        if not professor:
            raise ValueError("professor nao encontrado")
        return jsonify(professor.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        data = request.get_json() or {}
        professor = ProfessorService.atualizar_professor(id, data)
        return jsonify(professor.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        ProfessorService.deletar_professor(id)
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500