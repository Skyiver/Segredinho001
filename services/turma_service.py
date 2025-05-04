from models import db, Turma, Professor

class TurmaService:
    @staticmethod
    def validar_criacao(data):
        if not data.get('nome'):
            raise ValueError("turma sem nome")
        if not Professor.query.get(data.get('professor_id')):
            raise ValueError("professor não encontrado")
        if data.get('id') and Turma.query.get(data['id']):
            raise ValueError("id ja utilizada")

    @staticmethod
    def validar_atualizacao(data):
        if 'nome' in data and not data['nome']:
            raise ValueError("turma sem nome")
        if 'professor_id' in data and not Professor.query.get(data['professor_id']):
            raise ValueError("professor não encontrado")

    @staticmethod
    def criar_turma(data):
        TurmaService.validar_criacao(data)
        turma = Turma(**data)
        db.session.add(turma)
        db.session.commit()
        return turma

    @staticmethod
    def atualizar_turma(id, data):
        turma = Turma.query.get(id)
        if not turma:
            raise ValueError("turma não encontrada")
        TurmaService.validar_atualizacao(data)
        for campo, valor in data.items():
            setattr(turma, campo, valor)
        db.session.commit()
        return turma

    @staticmethod
    def deletar_turma(id):
        turma = Turma.query.get(id)
        if not turma:
            raise ValueError("turma não encontrada")
        db.session.delete(turma)
        db.session.commit()