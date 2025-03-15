class  Aluno: 

    def __init__(self, nome, id):

        self.nome = nome 
        self.id = id

    def to_dict(self):
        return {"nome": self.nome, "id": self.id}

class Professor:

    def __init__(self, nome, id):

        self.nome = nome 
        self.id = id

    def to_dict(self):
        return {"nome": self.nome, "id": self.id}

class Turma:

    def __init__(self, nome, id, idProfessor):

        self.nome = nome 
        self.id = id
        self.idProfessor = idProfessor

    def to_dict(self):
      return {"nome": self.nome, "id": self.id, "idProfessor": self.idProfessor}
        