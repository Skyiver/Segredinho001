from models import db, Professor

class ProfessorService:
    @staticmethod
    def validar_criacao(data):
        if not data.get('nome'):
            raise ValueError("professor sem nome")
        if data.get('id') and Professor.query.get(data['id']):
            raise ValueError("id ja utilizada")

    @staticmethod
    def validar_atualizacao(data):
        if 'nome' in data and not data['nome']:
            raise ValueError("professor sem nome")

    @staticmethod
    def criar_professor(data):
        ProfessorService.validar_criacao(data)
        professor = Professor(**data)
        db.session.add(professor)
        db.session.commit()
        return professor

    @staticmethod
    def atualizar_professor(id, data):
        professor = Professor.query.get(id)
        if not professor:
            raise ValueError("professor não encontrado")
        ProfessorService.validar_atualizacao(data)
        for campo, valor in data.items():
            setattr(professor, campo, valor)
        db.session.commit()
        return professor

    @staticmethod
    def deletar_professor(id):
        professor = Professor.query.get(id)
        if not professor:
            raise ValueError("professor não encontrado")
        db.session.delete(professor)
        db.session.commit()