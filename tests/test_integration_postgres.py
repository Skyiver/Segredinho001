import os
import requests
import time

BASE = os.getenv("BASE_URL", "http://localhost:5002/api")

def test_flush_and_create_and_get():
    # 1. Resetar o sistema
    r = requests.post(f"{BASE}/reseta")
    assert r.status_code == 200

    # 2. Criar um professor de apoio
    prof = {"nome": "IntProfessor", "id": 900}
    r = requests.post(f"{BASE}/professores", json=prof)
    assert r.status_code == 200

    # 3. Criar turma referenciando
    turma = {"nome": "IntTurma", "id": 901, "professor_id": 900}
    r = requests.post(f"{BASE}/turmas", json=turma)
    assert r.status_code == 200

    # 4. Criar aluno referenciando a turma
    aluno = {"nome": "IntAluno", "id": 902, "turma_id": 901}
    r = requests.post(f"{BASE}/alunos", json=aluno)
    assert r.status_code == 200
    data = r.json()
    assert data["nome"] == "IntAluno"
    assert data["turma_id"] == 901

    # 5. Buscar aluno e verificar já está no Postgres
    r = requests.get(f"{BASE}/alunos/902")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 902
    assert data["nome"] == "IntAluno"