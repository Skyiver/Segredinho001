from flask import Blueprint, jsonify, request
from models.turma import Turma

turmas_bp = Blueprint('turmas', __name__)
turmas_db = {}

@turmas_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    try:
        return jsonify([turma.to_dict() for turma in turmas_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json()
        if not data.get('nome'):
            return jsonify({"erro": "turma sem nome"}), 400

        if 'id' in data and data['id'] in turmas_db:
            return jsonify({"erro": "id ja utilizada"}), 400

        turma = Turma(
            nome=data['nome'],
            professor_id=data.get('professor_id'),
            ativo=data.get('ativo', True),
            id=data.get('id')
        )

        turmas_db[turma.id] = turma
        return jsonify(turma.to_dict()), 200

    except KeyError as e:
        return jsonify({"erro": f"Campo obrigatório faltando: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = turmas_db.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        turma = turmas_db.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404

        data = request.get_json()
        if 'nome' not in data:
            return jsonify({"erro": "turma sem nome"}), 400
        turma.nome = data['nome']

        return jsonify(turma.to_dict()), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        if id not in turmas_db:
            return jsonify({"erro": "turma nao encontrada"}), 404

        del turmas_db[id]
        return '', 204
    except Exception as e:
        return jsonify({"erro": str(e)}), 500