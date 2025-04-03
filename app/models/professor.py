class Professor:
    id_counter = 1

    def __init__(self, id, nome, idade, materia, observacao):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacao = observacao

    def to_dict(self):
        return vars(self)