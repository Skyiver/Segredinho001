from flask import Blueprint, jsonify, request
from models.professor import Professor
from bd import db

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def listar_professores():
    try:
        professores = Professor.query.all()
        return jsonify([{
            "id": p.id,
            "nome": p.nome,
            "idade": p.idade,
            "materia": p.materia,
            "observacao": p.observacao
        } for p in professores]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json()

        if not data.get('nome'):
            return jsonify({"erro": "professor sem nome"}), 400

        # Verifica se ID já existe (exigido pelos testes)
        if 'id' in data and Professor.query.get(data['id']):
            return jsonify({"erro": "id ja utilizada"}), 400

        # Verifica se nome já existe
        if Professor.query.filter_by(nome=data['nome']).first():
            return jsonify({"erro": "professor com nome já existente"}), 400

        professor = Professor(
            nome=data['nome'],
            id=data.get('id'),  # ID manual
            idade=data.get('idade'),
            materia=data.get('materia'),
            observacao=data.get('observacao')
        )

        db.session.add(professor)
        db.session.commit()
        return jsonify({
            "id": professor.id,
            "nome": professor.nome
        }), 200  
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    try:
        professor = Professor.query.get(id)
        if not professor:
            return jsonify({"erro": "professor nao encontrado"}), 404
        return jsonify({
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "materia": professor.materia,
            "observacao": professor.observacao
        }), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
