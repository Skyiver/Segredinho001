from flask import Blueprint, jsonify, request
from models import db, Turma, Professor

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
        if not data.get('nome'):
            return jsonify({"erro": "turma sem nome"}), 400
        if data.get('id') is not None and Turma.query.get(data['id']):
            return jsonify({"erro": "id ja utilizada"}), 400
        if not Professor.query.get(data.get('professor_id')):
            return jsonify({"erro": "professor nao encontrado"}), 404

        turma = Turma(
            id=data.get('id'),
            nome=data['nome'],
            professor_id=data['professor_id'],
            ativo=data.get('ativo', True)
        )
        db.session.add(turma)
        db.session.commit()
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404

        data = request.get_json() or {}
        if 'nome' not in data:
            return jsonify({"erro": "turma sem nome"}), 400

        turma.nome = data['nome']
        db.session.commit()
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404

        db.session.delete(turma)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500