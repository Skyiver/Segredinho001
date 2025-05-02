# services/aluno_service.py
from models import db, Aluno, Turma
from sqlalchemy.exc import IntegrityError

class AlunoService:
    @staticmethod
    def validar_criacao(data):
        if not data.get('nome'):
            raise ValueError("aluno sem nome")
        if data.get('id') and Aluno.query.get(data['id']):
            raise ValueError("id ja utilizada")
        if data.get('turma_id') and not Turma.query.get(data['turma_id']):
            raise ValueError("turma não encontrada")

    @staticmethod
    def validar_atualizacao(aluno, data):
        if 'nome' in data and not data['nome']:
            raise ValueError("aluno sem nome")
        if 'turma_id' in data and not Turma.query.get(data['turma_id']):
            raise ValueError("turma não encontrada")

    @staticmethod
    def criar_aluno(data):
        AlunoService.validar_criacao(data)
        aluno = Aluno(**data)
        db.session.add(aluno)
        db.session.commit()
        return aluno

    @staticmethod
    def atualizar_aluno(id, data):
        aluno = Aluno.query.get(id)
        if not aluno:
            raise ValueError("aluno não encontrado")
        AlunoService.validar_atualizacao(aluno, data)
        for campo, valor in data.items():
            setattr(aluno, campo, valor)
        db.session.commit()
        return aluno

    @staticmethod
    def deletar_aluno(id):
        aluno = Aluno.query.get(id)
        if not aluno:
            raise ValueError("aluno não encontrado")
        db.session.delete(aluno)
        db.session.commit()