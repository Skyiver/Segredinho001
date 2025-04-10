class Professor:
    id_counter = 1

    def __init__(self, nome, idade=None, materia=None, observacao=None, id=None):
        self.id = id if id is not None else Professor.id_counter
        if id is None:
            Professor.id_counter += 1
            
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacao = observacao

    def to_dict(self):
        return vars(self)