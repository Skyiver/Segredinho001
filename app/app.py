from flask import Flask, jsonify, request
from models import Aluno, Professor, Turma

app = Flask(__name__)

# Memória
alunos_db = {}
professores_db = {}
turmas_db = {}

#Os dados abaixo são pra rodar no teste
pre_professor = Professor(201, "Professor Testudo", 40, "Matemática", "É um teste")
professores_db[pre_professor.id] = pre_professor

pre_aluno = Aluno(104, "Aluno Testudo", 20, None, "01/01/2000", 8.0, 7.5, 7.75)
alunos_db[pre_aluno.id] = pre_aluno

pre_turma = Turma(301, "Turma Testuda", 201, True)
turmas_db[pre_turma.id] = pre_turma

# =======================
# Rota Inicial (Home)
# =======================
@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API Flask funcionando!"}), 200

# =======================
# Rota Alunos
# =======================
@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos_db.values()]), 200

@app.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.get_json()
    #Nome obrigatório
    if "nome" not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    #ID duplicado?
    if data["id"] in alunos_db:
        return jsonify({"erro": "id ja utilizada"}), 400

    aluno = Aluno(
        data["id"],
        data["nome"],
        data.get("idade"),
        data.get("turma_id"),
        data.get("data_nascimento"),
        data.get("nota_primeiro_semestre"),
        data.get("nota_segundo_semestre"),
        data.get("media_final")
    )
    alunos_db[aluno.id] = aluno
    return jsonify(aluno.to_dict()), 200

@app.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id):
    aluno = alunos_db.get(id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    return jsonify({"erro": "aluno nao encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["PUT"])
def update_aluno(id):
    aluno = alunos_db.get(id)
    if not aluno:
        return jsonify({"erro": "aluno nao encontrado"}), 404
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
    return jsonify({"erro": "aluno nao encontrado"}), 404

# =======================
# Rota Professor
# =======================
@app.route("/professores", methods=["GET"])
def get_professores():
    return jsonify([professor.to_dict() for professor in professores_db.values()]), 200

@app.route("/professores", methods=["POST"])
def create_professor():
    data = request.get_json()
    #Nome obrigatório
    if "nome" not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    #ID duplicado?
    if data["id"] in professores_db:
        return jsonify({"erro": "id ja utilizada"}), 400

    professor = Professor(
        data["id"],
        data["nome"],
        data.get("idade"),
        data.get("materia"),
        data.get("observação")
    )
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
        return jsonify({"erro": "professor nao encontrado"}), 404
    data = request.get_json()
    professor.nome = data.get("nome", professor.nome)
    return jsonify(professor.to_dict()), 200

@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    professor = professores_db.pop(id, None)
    if professor:
        return '', 204
    return jsonify({"erro": "professor nao encontrado"}), 404

# =======================
# Rota Turma
# =======================
@app.route("/turmas", methods=["GET"])
def get_turmas():
    return jsonify([turma.to_dict() for turma in turmas_db.values()]), 200

@app.route("/turmas", methods=["POST"])
def create_turma():
    data = request.get_json()
    #Nome obrigatório
    if "nome" not in data:
        return jsonify({"erro": "turma sem nome"}), 400
    #ID duplicada?
    if data["id"] in turmas_db:
        return jsonify({"erro": "id ja utilizada"}), 400

    professor_id = data.get("professor_id")
    if professor_id not in professores_db:
        return jsonify({"erro": "professor nao encontrado"}), 404

    turma = Turma(
        data["id"],
        data["nome"],
        professor_id,
        data.get("ativo")
    )
    turmas_db[turma.id] = turma
    return jsonify(turma.to_dict()), 200

@app.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id):
    turma = turmas_db.get(id)
    if turma:
        return jsonify(turma.to_dict()), 200
    return jsonify({"erro": "turma nao encontrada"}), 404

@app.route("/turmas/<int:id>", methods=["PUT"])
def update_turma(id):
    turma = turmas_db.get(id)
    if not turma:
        return jsonify({"erro": "turma nao encontrada"}), 404
    data = request.get_json()
    turma.nome = data.get("nome", turma.nome)
    return jsonify(turma.to_dict()), 200

@app.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id):
    turma = turmas_db.pop(id, None)
    if turma:
        return '', 204
    return jsonify({"erro": "turma nao encontrada"}), 404

# =======================
# Desfazer dados
# =======================
@app.route("/reseta", methods=["POST"])
def reset_data():
    alunos_db.clear()
    professores_db.clear()
    turmas_db.clear()

    #Aqui é pra voltar o dados de começo lá e ainda rodar nos testes porque né
    pre_professor = Professor(201, "Professor Testudo", 40, "Matemática", "É um teste")
    professores_db[pre_professor.id] = pre_professor

    pre_aluno = Aluno(104, "Aluno Testudo", 20, None, "01/01/2000", 8.0, 7.5, 7.75)
    alunos_db[pre_aluno.id] = pre_aluno

    pre_turma = Turma(301, "Turma Testuda", 201, True)
    turmas_db[pre_turma.id] = pre_turma
    return '', 200

if __name__ == "__main__":
    app.run(debug=True, port=5002)