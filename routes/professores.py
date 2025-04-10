from flask import Blueprint, jsonify, request
from models.professor import Professor

professores_bp = Blueprint('professores', __name__)
professores_db = {}

@professores_bp.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify([prof.to_dict() for prof in professores_db.values()]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({"erro": "professor sem nome"}), 400
            
        if 'id' in data and data['id'] in professores_db:
            return jsonify({"erro": "id ja utilizada"}), 400
            
        professor = Professor(
            nome=data['nome'],
            idade=data.get('idade'),
            materia=data.get('materia'),
            observacao=data.get('observacao'),
            id=data.get('id')
        )
        
        professores_db[professor.id] = professor
        return jsonify(professor.to_dict()), 200
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    try:
        professor = professores_db.get(id)
        if not professor:
            return jsonify({"erro": "professor nao encontrado"}), 404
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        professor = professores_db.get(id)
        if not professor:
            return jsonify({"erro": "professor nao encontrado"}), 404
            
        data = request.get_json()
        if 'nome' not in data:
            return jsonify({"erro": "professor sem nome"}), 400
            
        professor.nome = data['nome']
        return jsonify(professor.to_dict()), 200
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        if id not in professores_db:
            return jsonify({"erro": "professor nao encontrado"}), 404
            
        del professores_db[id]
        return '', 204
    except Exception as e:
        return jsonify({"erro": str(e)}), 500