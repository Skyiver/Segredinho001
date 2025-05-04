from flask import Blueprint, jsonify, request
from services.aluno_service import AlunoService
from models import db, Aluno
from flask_jwt_extended import jwt_required

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        alunos = Aluno.query.all()
        return jsonify([a.to_dict() for a in alunos]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos', methods=['POST'])
@jwt_required()
def criar_aluno():
    try:
        data = request.get_json() or {}
        aluno = AlunoService.criar_aluno(data)  
        return jsonify(aluno.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            raise ValueError("aluno nao encontrado")
        return jsonify(aluno.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            raise ValueError("aluno nao encontrado")

        data = request.get_json() or {}
        if 'nome' not in data:
            return jsonify({"erro": "aluno sem nome"}), 400  

        aluno.nome = data['nome']
        db.session.commit()
        return jsonify(aluno.to_dict()), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        AlunoService.deletar_aluno(id)  
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500