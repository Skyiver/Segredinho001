class Aluno:
    id_counter = 1

    def __init__(self, id, nome, idade, turma_id, data_nascimento, 
                 nota_primeiro_semestre, nota_segundo_semestre, 
                 media_final):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return vars(self)