class Aluno:
    id_counter = 1

    def __init__(self, nome, idade=None, turma_id=None, data_nascimento=None,
                 nota_primeiro_semestre=None, nota_segundo_semestre=None,
                 media_final=None, id=None):
        self.id = id if id is not None else Aluno.id_counter
        if id is None:
            Aluno.id_counter += 1
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return vars(self)