from flask import Blueprint, jsonify, request
from models.aluno import Aluno
from bd import db

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        alunos = Aluno.query.all()
        return jsonify([{
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma_id": aluno.turma_id,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
        } for aluno in alunos]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "aluno sem nome"}), 400
        
        if Aluno.query.filter_by(nome=data['nome']).first():
            return jsonify({"erro": "aluno com nome já existente"}), 400
        
        aluno = Aluno(
            nome=data['nome'],
            id=data.get('id'),  # Aceita ID manual
            idade=data.get('idade'),
            turma_id=data.get('turma_id'),
            data_nascimento=data.get('data_nascimento'),
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final')
        )
        
        db.session.add(aluno)
        db.session.commit()
        return jsonify({"id": aluno.id, "nome": aluno.nome}), 200  
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
