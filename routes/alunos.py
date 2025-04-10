from flask import Blueprint, jsonify, request
from models.aluno import Aluno

alunos_bp = Blueprint('alunos', __name__)
alunos_db = {}

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        return jsonify([aluno.to_dict() for aluno in alunos_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "aluno sem nome"}), 400
            
        if 'id' in data and data['id'] in alunos_db:
            return jsonify({"erro": "id ja utilizada"}), 400
            
        aluno = Aluno(
            nome=data['nome'],
            idade=data.get('idade'),
            turma_id=data.get('turma_id'),
            data_nascimento=data.get('data_nascimento'),
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final'),
            id=data.get('id')
        )
        
        alunos_db[aluno.id] = aluno
        return jsonify(aluno.to_dict()), 200
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        aluno = alunos_db.get(id)
        if not aluno:
            return jsonify({"erro": "aluno nao encontrado"}), 404
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = alunos_db.get(id)
        if not aluno:
            return jsonify({"erro": "aluno nao encontrado"}), 404
            
        data = request.get_json()
        if 'nome' not in data:
            return jsonify({"erro": "aluno sem nome"}), 400
            
        aluno.nome = data['nome']
        return jsonify(aluno.to_dict()), 200
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        if id not in alunos_db:
            return jsonify({"erro": "aluno nao encontrado"}), 404
            
        del alunos_db[id]
        return '', 204
    except Exception as e:
        return jsonify({"erro": str(e)}), 500