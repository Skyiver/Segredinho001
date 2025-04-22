from datetime import datetime  
from bd import db

class Turma(db.Model):
    __tablename__ = 'turmas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))

    professor = db.relationship('Professor', back_populates='turmas')
    alunos = db.relationship('Aluno', secondary='aluno_turma', back_populates='turmas')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'horario': self.horario,
            'ativo': self.ativo,
            'professor_id': self.professor_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }