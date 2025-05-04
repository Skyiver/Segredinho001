import os
import requests
import unittest
from flask_jwt_extended import create_access_token

# Configuração do banco de dados para testes
os.environ["DATABASE_URL"] = "postgresql://usuario:senha@localhost:5432/escola"
BASE_URL = "http://localhost:5002/api"

class TestSchoolAPI(unittest.TestCase):
    def get_auth_headers(self):
        access_token = create_access_token(identity="usuario_teste")
        return {'Authorization': f'Bearer {access_token}'}

    def reset_server(self):
        r = requests.post(f"{BASE_URL}/reseta")
        self.assertEqual(r.status_code, 200)

    # =====================
    # Testes para alunos
    # =====================
    def test_alunos_get_lista(self):
        self.reset_server()
        r = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    def test_alunos_post_cria_aluno(self):
        self.reset_server()
        aluno = {"nome": "Alice", "id": 101}
        r = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Alice")
        self.assertEqual(data["id"], 101)

    def test_alunos_get_por_id(self):
        self.reset_server()
        aluno = {"nome": "Bruno", "id": 102}
        r1 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.get(f"{BASE_URL}/alunos/102")
        self.assertEqual(r2.status_code, 200)
        data = r2.json()
        self.assertEqual(data["nome"], "Bruno")
        self.assertEqual(data["id"], 102)

    def test_alunos_put_atualiza_aluno(self):
        self.reset_server()
        aluno = {"nome": "Carlos", "id": 103}
        r1 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        novo_nome = {"nome": "Carlos Eduardo"}
        r2 = requests.put(
            f"{BASE_URL}/alunos/103", 
            json=novo_nome,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r2.status_code, 200)
        data = r2.json()
        self.assertEqual(data["nome"], "Carlos Eduardo")
        self.assertEqual(data["id"], 103)

    def test_alunos_delete_remove_aluno(self):
        self.reset_server()
        aluno = {"nome": "Teste Delete", "id": 104}
        r1 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.delete(
            f"{BASE_URL}/alunos/104",
            headers=self.get_auth_headers()
        )
        self.assertIn(r2.status_code, [200, 204])
        r3 = requests.get(f"{BASE_URL}/alunos/104")
        self.assertIn(r3.status_code, [400, 404])
        data = r3.json()
        self.assertEqual(data.get("erro"), "aluno nao encontrado")

    def test_alunos_post_id_duplicado(self):
        self.reset_server()
        aluno = {"nome": "Evelyn", "id": 105}
        r1 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r2.status_code, 400)
        data = r2.json()
        self.assertEqual(data.get("erro"), "id ja utilizada")

    def test_alunos_put_sem_nome(self):
        self.reset_server()
        aluno = {"nome": "Felipe", "id": 106}
        r1 = requests.post(
            f"{BASE_URL}/alunos", 
            json=aluno,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.put(
            f"{BASE_URL}/alunos/106", 
            json={"id": 106},
            headers=self.get_auth_headers()
        )
        self.assertEqual(r2.status_code, 400)
        data = r2.json()
        self.assertEqual(data.get("erro"), "aluno sem nome")

    # ============================
    # Testes para professores
    # ============================
    def test_professores_get_lista(self):
        self.reset_server()
        r = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    def test_professores_post_cria_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Gomes", "id": 201}
        r = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Prof. Gomes")
        self.assertEqual(data["id"], 201)

    def test_professores_get_por_id(self):
        self.reset_server()
        professor = {"nome": "Prof. Silva", "id": 202}
        r1 = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.get(f"{BASE_URL}/professores/202")
        self.assertEqual(r2.status_code, 200)
        data = r2.json()
        self.assertEqual(data["nome"], "Prof. Silva")
        self.assertEqual(data["id"], 202)

    def test_professores_put_atualiza_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Oliveira", "id": 203}
        r1 = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        novo = {"nome": "Prof. Oliveira Neto"}
        r2 = requests.put(
            f"{BASE_URL}/professores/203", 
            json=novo,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r2.status_code, 200)
        data = r2.json()
        self.assertEqual(data["nome"], "Prof. Oliveira Neto")
        self.assertEqual(data["id"], 203)

    def test_professores_delete_remove_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Rodrigues", "id": 204}
        r1 = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.delete(
            f"{BASE_URL}/professores/204",
            headers=self.get_auth_headers()
        )
        self.assertIn(r2.status_code, [200, 204])
        r3 = requests.get(f"{BASE_URL}/professores/204")
        self.assertIn(r3.status_code, [400, 404])
        data = r3.json()
        self.assertEqual(data.get("erro"), "professor nao encontrado")

    def test_professores_post_id_duplicado(self):
        self.reset_server()
        professor = {"nome": "Prof. Mendes", "id": 205}
        r1 = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r1.status_code, 200)
        r2 = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r2.status_code, 400)
        data = r2.json()
        self.assertEqual(data.get("erro"), "id ja utilizada")

    def test_professores_post_sem_nome(self):
        self.reset_server()
        r = requests.post(
            f"{BASE_URL}/professores", 
            json={"id": 206},
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 400)
        data = r.json()
        self.assertEqual(data.get("erro"), "professor sem nome")

    # ============================
    # Testes para turmas
    # ============================
    def test_turmas_get_lista(self):
        self.reset_server()
        r = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    def test_turmas_post_cria_turma(self):
        self.reset_server()
        professor = {"nome": "Prof. Teste", "id": 201}
        rp = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rp.status_code, 200)
        turma = {"nome": "Turma A", "id": 301, "professor_id": 201}
        r = requests.post(
            f"{BASE_URL}/turmas", 
            json=turma,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma A")
        self.assertEqual(data["id"], 301)
        self.assertEqual(data["professor_id"], 201)

    def test_turmas_get_por_id(self):
        self.reset_server()
        professor = {"nome": "Prof. Silva", "id": 202}
        rp = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rp.status_code, 200)
        turma = {"nome": "Turma B", "id": 302, "professor_id": 202}
        rt = requests.post(
            f"{BASE_URL}/turmas", 
            json=turma,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rt.status_code, 200)
        r = requests.get(f"{BASE_URL}/turmas/302")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma B")
        self.assertEqual(data["id"], 302)
        self.assertEqual(data["professor_id"], 202)

    def test_turmas_put_atualiza_turma(self):
        self.reset_server()
        professor = {"nome": "Prof. Oliveira", "id": 203}
        rp = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rp.status_code, 200)
        turma = {"nome": "Turma C", "id": 303, "professor_id": 203}
        rt = requests.post(
            f"{BASE_URL}/turmas", 
            json=turma,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rt.status_code, 200)
        novo = {"nome": "Turma C - Atualizada"}
        r = requests.put(
            f"{BASE_URL}/turmas/303", 
            json=novo,
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma C - Atualizada")
        self.assertEqual(data["id"], 303)

    def test_turmas_delete_remove_turma(self):
        self.reset_server()
        professor = {"nome": "Prof. Rodrigues", "id": 204}
        rp = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rp.status_code, 200)
        turma = {"nome": "Turma D", "id": 304, "professor_id": 204}
        rt = requests.post(
            f"{BASE_URL}/turmas", 
            json=turma,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rt.status_code, 200)
        rd = requests.delete(
            f"{BASE_URL}/turmas/304",
            headers=self.get_auth_headers()
        )
        self.assertIn(rd.status_code, [200, 204])
        rg = requests.get(f"{BASE_URL}/turmas/304")
        self.assertIn(rg.status_code, [400, 404])
        data = rg.json()
        self.assertEqual(data.get("erro"), "turma nao encontrada")

    def test_turmas_post_sem_nome(self):
        self.reset_server()
        professor = {"nome": "Prof. Mendes", "id": 205}
        rp = requests.post(
            f"{BASE_URL}/professores", 
            json=professor,
            headers=self.get_auth_headers()
        )
        self.assertEqual(rp.status_code, 200)
        r = requests.post(
            f"{BASE_URL}/turmas", 
            json={"id": 305, "professor_id": 205},
            headers=self.get_auth_headers()
        )
        self.assertEqual(r.status_code, 400)
        data = r.json()
        self.assertEqual(data.get("erro"), "turma sem nome")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSchoolAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()