from bd import db

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __init__(self, nome, professor_id, ativo=True):
        self.nome = nome
        self.professor_id = professor_id
        self.ativo = ativo

    def __repr__(self):
        return f'<Turma {self.nome}>'
