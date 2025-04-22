from flask import Blueprint, request, jsonify
from models.aluno import Aluno
from bd import db

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        alunos = Aluno.query.all()
        return jsonify([aluno.to_dict() for aluno in alunos]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "aluno sem nome"}), 400
            
        aluno = Aluno(
            nome=data['nome'],
            idade=data.get('idade'),
            data_nascimento=data.get('data_nascimento'),
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final'),
            turma_id=data.get('turma_id')
        )
        
        db.session.add(aluno)
        db.session.commit()
        return jsonify(aluno.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        aluno = Aluno.query.get_or_404(id)
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = Aluno.query.get_or_404(id)
        data = request.get_json()
        
        if 'nome' in data:
            aluno.nome = data['nome']
        if 'idade' in data:
            aluno.idade = data['idade']
        if 'data_nascimento' in data:
            aluno.data_nascimento = data['data_nascimento']
        if 'turma_id' in data:
            aluno.turma_id = data['turma_id']
            
        db.session.commit()
        return jsonify(aluno.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500