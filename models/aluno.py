from bd import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  
    nome = db.Column(db.String(100), nullable=False)
    primeiro_semestre = db.Column(db.Float, nullable=True)
    segundo_semestre = db.Column(db.Float, nullable=True)
    idade = db.Column(db.Integer, nullable=True)  
    turma_id = db.Column(db.Integer, nullable=True)
    data_nascimento = db.Column(db.String(20), nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    def __init__(self, nome, **kwargs):
        self.nome = nome
        self.primeiro_semestre = kwargs.get('nota_primeiro_semestre')
        self.segundo_semestre = kwargs.get('nota_segundo_semestre')
        self.idade = kwargs.get('idade')
        self.turma_id = kwargs.get('turma_id')
        self.data_nascimento = kwargs.get('data_nascimento')
        self.media_final = kwargs.get('media_final')

    def __repr__(self):
        return f'<Aluno {self.nome}>'