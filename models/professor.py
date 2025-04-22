from datetime import datetime 
from bd import db

class Professor(db.Model):
    __tablename__ = 'professores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacao = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 

    turmas = db.relationship('Turma', back_populates='professor')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacao': self.observacao,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }