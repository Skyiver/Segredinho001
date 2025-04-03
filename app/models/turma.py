class Turma:
    id_counter = 1

    def __init__(self, id, descricao, idProfessor, ativo):
        self.id = id
        self.descricao = descricao
        self.idProfessor = idProfessor
        self.ativo = ativo

    def to_dict(self):
        return vars(self)