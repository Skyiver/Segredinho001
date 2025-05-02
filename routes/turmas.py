from flask import Blueprint, jsonify, request
from models import Turma
from services.turma_service import TurmaService

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    try:
        turmas = Turma.query.all()
        return jsonify([t.to_dict() for t in turmas]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json() or {}
        turma = TurmaService.criar_turma(data)
        return jsonify(turma.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            raise ValueError("turma nao encontrada")
        return jsonify(turma.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        data = request.get_json() or {}
        turma = TurmaService.atualizar_turma(id, data)
        return jsonify(turma.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        TurmaService.deletar_turma(id)
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500