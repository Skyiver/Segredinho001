class  Aluno: 
    id_counter = 1

    def __init__(self, id, nome, idade, turma_id, data_nascimento, 
                 nota_primeiro_semestre, nota_segundo_semestre, 
                 media_final):

        self.id = Aluno.id_counter
        Aluno.id_counter += 1
        self.nome = nome 
        self.turma_id = turma_id
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return vars (self)

class Professor:
    id_counter = 1

    def __init__(self, id, nome, idade, materia, observacao):

        self.id = Professor.id_counter
        Professor.id_counter += 1
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacao = observacao

    def to_dict(self):
        return vars (self)

class Turma:
    id_counter = 1

    def __init__(self, id, descricao, idProfessor, ativo):
 
        self.id = Turma.id_counter
        Turma.id_counter += 1
        self.descricao = descricao
        self.idProfessor = idProfessor
        self.ativo = ativo

    def to_dict(self):
      return vars (self)
        