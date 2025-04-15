from bd import db

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacao = db.Column(db.Text)

    def __init__(self, nome, **kwargs):
        self.nome = nome
        self.id = kwargs.get('id')  
        self.idade = kwargs.get('idade')
        self.materia = kwargs.get('materia')
        self.observacao = kwargs.get('observacao')

    def __repr__(self):
        return f'<Professor {self.nome}>'