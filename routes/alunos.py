from flask import Blueprint, jsonify, request
from models import db, Aluno

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        alunos = Aluno.query.all()
        return jsonify([a.to_dict() for a in alunos]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json() or {}
        if not data.get('nome'):
            return jsonify({"erro": "aluno sem nome"}), 400
        if data.get('id') is not None and Aluno.query.get(data['id']):
            return jsonify({"erro": "id ja utilizada"}), 400

        aluno = Aluno(
            id=data.get('id'),
            nome=data['nome'],
            idade=data.get('idade'),
            turma_id=data.get('turma_id'),
            data_nascimento=data.get('data_nascimento'),
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final')
        )
        db.session.add(aluno)
        db.session.commit()
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({"erro": "aluno nao encontrado"}), 404
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({"erro": "aluno nao encontrado"}), 404

        data = request.get_json() or {}
        if 'nome' not in data:
            return jsonify({"erro": "aluno sem nome"}), 400

        aluno.nome = data['nome']
        db.session.commit()
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({"erro": "aluno nao encontrado"}), 404

        db.session.delete(aluno)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500