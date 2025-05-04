from flask_restx import Namespace, Resource, fields
from services.aluno_service import AlunoService

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

aluno_model = alunos_ns.model("Aluno", {
    "id": fields.Integer(readonly=True, description="ID do aluno"),
    "nome": fields.String(required=True, description="Nome do aluno"),
    "turma_id": fields.Integer(required=False, description="ID da turma"),
    "idade": fields.Integer(readonly=True, description="Idade calculada"),
    "data_nascimento": fields.String(required=False, description="Data de nascimento"),
    "nota_primeiro_semestre": fields.Float(required=False, description="Nota 1º sem."),
    "nota_segundo_semestre": fields.Float(required=False, description="Nota 2º sem."),
    "media_final": fields.Float(readonly=True, description="Média final"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_model)
    def get(self):
        """Lista todos os alunos"""
        from models import Aluno
        return [a.to_dict() for a in Aluno.query.all()]

    @alunos_ns.expect(aluno_model, validate=True)
    @alunos_ns.marshal_with(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        aluno = AlunoService.criar_aluno(data)
        return aluno.to_dict(), 200

@alunos_ns.route("/<int:id>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_model)
    def get(self, id):
        """Obtém um aluno pelo ID"""
        from models import Aluno
        a = Aluno.query.get(id)
        if not a:
            alunos_ns.abort(404, "aluno nao encontrado")
        return a.to_dict()

    @alunos_ns.expect(aluno_model, validate=True)
    @alunos_ns.marshal_with(aluno_model)
    def put(self, id):
        """Atualiza um aluno pelo ID"""
        aluno = AlunoService.atualizar_aluno(id, alunos_ns.payload)
        return aluno.to_dict(), 200

    def delete(self, id):
        """Exclui um aluno pelo ID"""
        AlunoService.deletar_aluno(id)
        return {"message": "aluno excluído com sucesso"}, 204