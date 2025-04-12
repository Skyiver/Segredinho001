class Turma:
    id_counter = 1

    def __init__(self, nome, professor_id, ativo=True, id=None):
        self.id = id if id is not None else Turma.id_counter
        if id is None:
            Turma.id_counter += 1

        self.nome = nome
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return vars(self)