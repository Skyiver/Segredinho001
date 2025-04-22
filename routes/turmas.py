from flask import Blueprint, request, jsonify
from models.turma import Turma
from bd import db

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    try:
        turmas = Turma.query.all()
        return jsonify([turma.to_dict() for turma in turmas]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "turma sem nome"}), 400
            
        turma = Turma(
            nome=data['nome'],
            horario=data.get('horario'),
            ativo=data.get('ativo', True),
            professor_id=data.get('professor_id')
        )
        
        db.session.add(turma)
        db.session.commit()
        return jsonify(turma.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = Turma.query.get_or_404(id)
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        turma = Turma.query.get_or_404(id)
        data = request.get_json()
        
        if 'nome' in data:
            turma.nome = data['nome']
        if 'horario' in data:
            turma.horario = data['horario']
        if 'ativo' in data:
            turma.ativo = data['ativo']
        if 'professor_id' in data:
            turma.professor_id = data['professor_id']
            
        db.session.commit()
        return jsonify(turma.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        turma = Turma.query.get_or_404(id)
        db.session.delete(turma)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500