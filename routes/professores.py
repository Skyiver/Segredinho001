from flask import Blueprint, jsonify, request
from models import db, Professor

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def listar_professores():
    profs = Professor.query.all()
    return jsonify([p.to_dict() for p in profs]), 200

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    data = request.get_json()
    if not data.get('nome'):
        return jsonify({"erro": "professor sem nome"}), 400
    if Professor.query.get(data.get('id')):
        return jsonify({"erro": "id ja utilizada"}), 400

    prof = Professor(
        id=data['id'],
        nome=data['nome'],
        idade=data.get('idade'),
        materia=data.get('materia'),
        observacao=data.get('observacao')
    )
    db.session.add(prof)
    db.session.commit()
    return jsonify(prof.to_dict()), 200

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "professor nao encontrado"}), 404
    return jsonify(prof.to_dict()), 200

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "professor nao encontrado"}), 404
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    prof.nome = data['nome']
    db.session.commit()
    return jsonify(prof.to_dict()), 200

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "professor nao encontrado"}), 404
    db.session.delete(prof)
    db.session.commit()
    return '', 204