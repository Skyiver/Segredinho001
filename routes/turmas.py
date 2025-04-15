from flask import Blueprint, jsonify, request
from models.turma import Turma
from bd import db

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    try:
        turmas = Turma.query.all()
        return jsonify([{
            "id": t.id,
            "nome": t.nome,
            "professor_id": t.professor_id,
            "ativo": t.ativo
        } for t in turmas]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json()

        if not data.get('nome') or not data.get('professor_id'):
            return jsonify({"erro": "nome e professor_id são obrigatórios"}), 400

        turma = Turma(
            nome=data['nome'],
            professor_id=data['professor_id'],
            ativo=data.get('ativo', True)
        )

        db.session.add(turma)
        db.session.commit()

        return jsonify({
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "ativo": turma.ativo
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404

        return jsonify({
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "ativo": turma.ativo
        }), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"erro": "turma nao encontrada"}), 404

        data = request.get_json()

        if 'nome' in data:
            turma.nome = data['nome']
        if 'professor_id' in data:
            turma.professor_id = data['professor_id']
        if 'ativo' in data:
            turma.ativo = data['ativo']

        db.session.commit()

        return jsonify({
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "ativo": turma.ativo
        }), 200

    except Exception as e:
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
        return jsonify({"erro": str(e)}), 500
