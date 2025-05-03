from flask_restx import Namespace, Resource, fields
from services.turma_service import TurmaService

turmas_ns = Namespace("turmas", description="Operações relacionadas às turmas")

turma_model = turmas_ns.model("Turma", {
    "id": fields.Integer(readonly=True, description="ID da turma"),
    "nome": fields.String(required=True, description="Nome da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor"),
    "ativo": fields.Boolean(required=False, description="Status ativo/inativo"),
})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_model)
    def get(self):
        from models import Turma
        return [t.to_dict() for t in Turma.query.all()]

    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model)
    def post(self):
        turma = TurmaService.criar_turma(turmas_ns.payload)
        return turma.to_dict(), 200

@turmas_ns.route("/<int:id>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_model)
    def get(self, id):
        from models import Turma
        t = Turma.query.get(id)
        if not t:
            turmas_ns.abort(404, "turma nao encontrada")
        return t.to_dict()

    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model)
    def put(self, id):
        turma = TurmaService.atualizar_turma(id, turmas_ns.payload)
        return turma.to_dict(), 200

    def delete(self, id):
        TurmaService.deletar_turma(id)
        return {"message": "turma excluída com sucesso"}, 204