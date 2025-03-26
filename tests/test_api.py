import requests
import unittest

# URL base da API
BASE_URL = "http://localhost:5002"

class TestSchoolAPI(unittest.TestCase):

    # Método para resetar os dados da API
    def reset_server(self):
        r = requests.post(BASE_URL + "/reseta")
        self.assertEqual(r.status_code, 200)

    # =====================
    # Testes para alunos primeiro
    # =====================

    # 1. Verifica se GET /alunos retorna uma lista
    def test_alunos_get_lista(self):
        self.reset_server()  # Isso é pra ver se tá rodando certo
        r = requests.get(BASE_URL + "/alunos")
        self.assertEqual(r.status_code, 200)
        try:
            data = r.json()
        except:
            self.fail("A resposta não está em formato JSON.")
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    # 2. Testa se POST /alunos cria um aluno certo
    def test_alunos_post_cria_aluno(self):
        self.reset_server()
        aluno = {"nome": "Alice", "id": 101}
        r = requests.post(BASE_URL + "/alunos", json=aluno)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Alice")
        self.assertEqual(data["id"], 101)

    # 3. Verifica se GET /alunos/<id> retorna o aluno correto
    def test_alunos_get_por_id(self):
        self.reset_server()
        aluno = {"nome": "Bruno", "id": 102}
        requests.post(BASE_URL + "/alunos", json=aluno)
        r = requests.get(BASE_URL + f"/alunos/{102}")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Bruno")
        self.assertEqual(data["id"], 102)

    # 4. Testa se PUT /alunos/<id> atualiza o nome do aluno
    def test_alunos_put_atualiza_aluno(self):
        self.reset_server()
        aluno = {"nome": "Carlos", "id": 103}
        requests.post(BASE_URL + "/alunos", json=aluno)
        # Atualiza o nome do aluno aqui
        novo_nome = {"nome": "Carlos Eduardo"}
        r = requests.put(BASE_URL + f"/alunos/{103}", json=novo_nome)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Carlos Eduardo")
        self.assertEqual(data["id"], 103)

    # 5. Verifica se DELETE /alunos/<id> remove o aluno
    def test_alunos_delete_remove_aluno(self):
      self.reset_server()
    
      #Em teoria tá criado já no reset
      aluno_id = 104

      # Deletando o aluno já criado
      r = requests.delete(BASE_URL + f"/alunos/{aluno_id}")
      self.assertIn(r.status_code, [200, 204])
    
      # Confirma que o aluno foi removido
      r_get = requests.get(BASE_URL + f"/alunos/{aluno_id}")
      self.assertIn(r_get.status_code, [400, 404])  # Não deve encontrar aqui
      data = r_get.json()
      self.assertEqual(data.get("erro"), "aluno nao encontrado")

    # 6. Testa se tentar criar aluno com ID duplicada retorna erro
    def test_alunos_post_id_duplicado(self):
        self.reset_server()
        aluno = {"nome": "Evelyn", "id": 105}
        r1 = requests.post(BASE_URL + "/alunos", json=aluno)
        self.assertEqual(r1.status_code, 200)
        # Tenta criar outro aluno com o mesmo ID
        r2 = requests.post(BASE_URL + "/alunos", json=aluno)
        self.assertEqual(r2.status_code, 400)
        data = r2.json()
        self.assertEqual(data.get("erro"), "id ja utilizada")

    # 7. Testa se PUT /alunos sem o campo "nome" retorna erro
    def test_alunos_put_sem_nome(self):
        self.reset_server()
        aluno = {"nome": "Felipe", "id": 106}
        requests.post(BASE_URL + "/alunos", json=aluno)
        # Tenta atualizar sem enviar o campo "nome"
        r = requests.put(BASE_URL + f"/alunos/{106}", json={"id": 106})
        self.assertEqual(r.status_code, 400)
        data = r.json()
        self.assertEqual(data.get("erro"), "aluno sem nome")

    # ============================
    # Testes para professores agora
    # ============================

    # 8. Verifica se GET /professores retorna uma lista
    def test_professores_get_lista(self):
        self.reset_server()
        r = requests.get(BASE_URL + "/professores")
        self.assertEqual(r.status_code, 200)
        try:
            data = r.json()
        except:
            self.fail("A resposta não está em formato JSON.")
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    # 9. Testa se POST /professores cria um professor corretamente
    def test_professores_post_cria_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Gomes", "id": 201}
        r = requests.post(BASE_URL + "/professores", json=professor)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Prof. Gomes")
        self.assertEqual(data["id"], 201)

    # 10. Verifica se GET /professores/<id> retorna o professor correto
    def test_professores_get_por_id(self):
        self.reset_server()
        professor = {"nome": "Prof. Silva", "id": 202}
        requests.post(BASE_URL + "/professores", json=professor)
        r = requests.get(BASE_URL + f"/professores/{202}")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Prof. Silva")
        self.assertEqual(data["id"], 202)

    # 11. Testa se PUT /professores/<id> atualiza o nome do professor
    def test_professores_put_atualiza_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Oliveira", "id": 203}
        requests.post(BASE_URL + "/professores", json=professor)
        novo_dado = {"nome": "Prof. Oliveira Neto"}
        r = requests.put(BASE_URL + f"/professores/{203}", json=novo_dado)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Prof. Oliveira Neto")
        self.assertEqual(data["id"], 203)

    # 12. Verifica se DELETE /professores/<id> remove o professor
    def test_professores_delete_remove_professor(self):
        self.reset_server()
        professor = {"nome": "Prof. Rodrigues", "id": 204}
        requests.post(BASE_URL + "/professores", json=professor)
        r = requests.delete(BASE_URL + f"/professores/{204}")
        self.assertIn(r.status_code, [200, 204])
        # Confirma que o professor foi removido
        r_get = requests.get(BASE_URL + f"/professores/{204}")
        self.assertIn(r_get.status_code, [400, 404])
        data = r_get.json()
        self.assertEqual(data.get("erro"), "professor nao encontrado")

    # 13. Testa se tentar criar professor com ID duplicada retorna erro
    def test_professores_post_id_duplicado(self):
        self.reset_server()
        professor = {"nome": "Prof. Mendes", "id": 205}
        r1 = requests.post(BASE_URL + "/professores", json=professor)
        self.assertEqual(r1.status_code, 200)
        # Tenta criar outro professor com o mesmo ID
        r2 = requests.post(BASE_URL + "/professores", json=professor)
        self.assertEqual(r2.status_code, 400)
        data = r2.json()
        self.assertEqual(data.get("erro"), "id ja utilizada")

    # 14. Testa se POST /professores sem o campo "nome" retorna erro
    def test_professores_post_sem_nome(self):
        self.reset_server()
        professor = {"id": 206}
        r = requests.post(BASE_URL + "/professores", json=professor)
        self.assertEqual(r.status_code, 400)
        data = r.json()
        self.assertEqual(data.get("erro"), "professor sem nome")

    # ============================
    # Testes para turmas por "último"
    # ============================

    # 15. Verifica se GET /turmas retorna uma lista
    def test_turmas_get_lista(self):
        self.reset_server()
        r = requests.get(BASE_URL + "/turmas")
        self.assertEqual(r.status_code, 200)
        try:
            data = r.json()
        except:
            self.fail("A resposta não está em formato JSON.")
        self.assertIsInstance(data, list, "A resposta deve ser uma lista.")

    # 16. Testa se POST /turmas cria uma turma corretamente
    def test_turmas_post_cria_turma(self):
        self.reset_server()
        # Supondo que a criação de uma turma requeira um nome, ID e o ID do professor, mas provavelmente sim
        turma = {"nome": "Turma A", "id": 301, "professor_id": 201}
        r = requests.post(BASE_URL + "/turmas", json=turma)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma A")
        self.assertEqual(data["id"], 301)
        self.assertEqual(data["professor_id"], 201)

    # 17. Verifica se GET /turmas/<id> retorna a turma correta
    def test_turmas_get_por_id(self):
        self.reset_server()
        turma = {"nome": "Turma B", "id": 302, "professor_id": 202}
        requests.post(BASE_URL + "/turmas", json=turma)
        r = requests.get(BASE_URL + f"/turmas/{302}")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma B")
        self.assertEqual(data["id"], 302)
        self.assertEqual(data["professor_id"], 202)

    # 18. Testa se PUT /turmas/<id> atualiza o nome da turma
    def test_turmas_put_atualiza_turma(self):
        self.reset_server()
        turma = {"nome": "Turma C", "id": 303, "professor_id": 203}
        requests.post(BASE_URL + "/turmas", json=turma)
        novo_dado = {"nome": "Turma C - Atualizada"}
        r = requests.put(BASE_URL + f"/turmas/{303}", json=novo_dado)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(data["nome"], "Turma C - Atualizada")
        self.assertEqual(data["id"], 303)

    # 19. Verifica se DELETE /turmas/<id> remove a turma
    def test_turmas_delete_remove_turma(self):
        self.reset_server()
        turma = {"nome": "Turma D", "id": 304, "professor_id": 204}
        requests.post(BASE_URL + "/turmas", json=turma)
        r = requests.delete(BASE_URL + f"/turmas/{304}")
        self.assertIn(r.status_code, [200, 204])
        # Confirma que a turma foi removida
        r_get = requests.get(BASE_URL + f"/turmas/{304}")
        self.assertIn(r_get.status_code, [400, 404])
        data = r_get.json()
        self.assertEqual(data.get("erro"), "turma nao encontrada")

    # 20. Testa se POST /turmas sem o campo "nome" retorna erro
    def test_turmas_post_sem_nome(self):
        self.reset_server()
        turma = {"id": 305, "professor_id": 205}
        r = requests.post(BASE_URL + "/turmas", json=turma)
        self.assertEqual(r.status_code, 400)
        data = r.json()
        self.assertEqual(data.get("erro"), "turma sem nome")


# Função rodar essa bagaça
def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSchoolAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
