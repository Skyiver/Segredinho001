from flask import Blueprint, jsonify, request
from models import db, Aluno

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos]), 200

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.get_json()
    if not data.get('nome'):
        return jsonify({"erro": "aluno sem nome"}), 400
    if Aluno.query.get(data.get('id')):
        return jsonify({"erro": "id ja utilizada"}), 400

    aluno = Aluno(
        id=data['id'],
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

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"erro": "aluno nao encontrado"}), 404
    return jsonify(aluno.to_dict()), 200

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"erro": "aluno nao encontrado"}), 404
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    aluno.nome = data['nome']
    db.session.commit()
    return jsonify(aluno.to_dict()), 200

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"erro": "aluno nao encontrado"}), 404
    db.session.delete(aluno)
    db.session.commit()
    return '', 204