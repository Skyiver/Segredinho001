from flask import Flask, jsonify, request
from models import Aluno, Professor, Turma

app = Flask(__name__)

# Memória
alunos_db = {}
professores_db = {}
turmas_db = {}

# =======================
# Rota Alunos
# =======================
@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos_db.values()]), 200

@app.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.get_json()
    aluno = Aluno(data["nome"], data["idade"], data["turma_id"],
                  data["data_nascimento"], data["nota_primeiro_semestre"],
                  data["nota_segundo_semestre"], data["media_final"])
    alunos_db[aluno.id] = aluno
    return jsonify(aluno.to_dict()), 200

@app.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id):
    aluno = alunos_db.get(id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    return jsonify({"erro": "aluno não encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["PUT"])
def update_aluno(id):
    aluno = alunos_db.get(id)
    if not aluno:
        return jsonify({"erro": "aluno não encontrado"}), 404
    data = request.get_json()
    if "nome" not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    aluno.nome = data["nome"]
    return jsonify(aluno.to_dict()), 200

@app.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    aluno = alunos_db.pop(id, None)
    if aluno:
        return '', 204
    return jsonify({"erro": "aluno não encontrado"}), 404

# =======================
# Rota Professor
# =======================
@app.route("/professor", methods=["GET"])
def get_professores():
    return jsonify([professor.to_dict() for professor in professores_db.values()]), 200

@app.route("/professores", methods=["POST"])
def create_professor():
    data = request.get_json()
    professor = Professor(data["nome"], data["idade"], data["materia"], data["observação"])
    professores_db[professor.id] = professor
    return jsonify(professor.to_dict()), 200

@app.route("/professores/<int:id>", methods=["GET"])
def get_professor(id):
    professor = professores_db.get(id)
    if professor:
        return jsonify(professor.to_dict()), 200
    return jsonify({"erro": "professor nao encontrado"}), 404

@app.route("/professores/<int:id>", methods=["PUT"])
def update_professor(id):
    professor = professores_db.get(id)
    if not professor:
        return jsonify({"erro": "professor não encontrado"}), 404
    data = request.get_json()
    professor.nome = data.get("nome", professor.nome)
    return jsonify(professor.to_dict()), 200

@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    professor = professores_db.pop(id, None)
    if professor:
        return '', 204
    return jsonify({"erro": "professor não encontrado"}), 404

# =======================
# Rota Turma
# =======================
@app.route("/turmas", methods=["GET"])
def get_turmas():
    return jsonify([turma.to_dict() for turma in turmas_db.values()]), 200

@app.route("/turmas", methods=["POST"])
def create_turma():
    data = request.get_json()
    turma = Turma(data["descricao"], data["professor_id"], data["ativo"])
    turmas_db[turma.id] = turma
    return jsonify(turma.to_dict()), 200

@app.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id):
    turma = turmas_db.get(id)
    if turma:
        return jsonify(turma.to_dict()), 200
    return jsonify({"erro": "turma não encontrada"}), 404

@app.route("/turmas/<int:id>", methods=["PUT"])
def update_turma(id):
    turma = turmas_db.get(id)
    if not turma:
        return jsonify({"erro": "turma não encontrada"}), 404
    data = request.get_json()
    turma.descricao = data.get("descricao", turma.descricao)
    return jsonify(turma.to_dict()), 200

@app.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id):
    turma = turmas_db.pop(id, None)
    if turma:
        return '', 204
    return jsonify({"erro": "turma nâo encontrada"}), 404

# =======================
# Desfazer dados
# =======================
@app.route("/reseta", methods=["POST"])
def reset_data():
    alunos_db.clear()
    professores_db.clear()
    turmas_db.clear()
    return '', 200

if __name__ == "__main__":
    app.run(debug=True)