from flask import Blueprint, request, jsonify
from models.professor import Professor
from bd import db

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def listar_professores():
    try:
        professores = Professor.query.all()
        return jsonify([prof.to_dict() for prof in professores]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "professor sem nome"}), 400
            
        professor = Professor(
            nome=data['nome'],
            idade=data.get('idade'),
            materia=data.get('materia'),
            observacao=data.get('observacao')
        )
        
        db.session.add(professor)
        db.session.commit()
        return jsonify(professor.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    try:
        professor = Professor.query.get_or_404(id)
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        professor = Professor.query.get_or_404(id)
        data = request.get_json()
        
        if 'nome' in data:
            professor.nome = data['nome']
        if 'idade' in data:
            professor.idade = data['idade']
        if 'materia' in data:
            professor.materia = data['materia']
        if 'observacao' in data:
            professor.observacao = data['observacao']
            
        db.session.commit()
        return jsonify(professor.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        professor = Professor.query.get_or_404(id)
        db.session.delete(professor)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500