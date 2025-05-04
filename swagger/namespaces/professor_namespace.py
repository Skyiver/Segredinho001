from flask_restx import Namespace, Resource, fields
from services.professor_service import ProfessorService

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "id": fields.Integer(readonly=True, description="ID do professor"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=False, description="Matéria lecionada"),
    "idade": fields.Integer(required=False, description="Idade"),
    "observacao": fields.String(required=False, description="Observação"),
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_model)
    def get(self):
        from models import Professor
        return [p.to_dict() for p in Professor.query.all()]

    @professores_ns.expect(professor_model, validate=True)
    @professores_ns.marshal_with(professor_model)
    def post(self):
        prof = ProfessorService.criar_professor(professores_ns.payload)
        return prof.to_dict(), 200

@professores_ns.route("/<int:id>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_model)
    def get(self, id):
        from models import Professor
        p = Professor.query.get(id)
        if not p:
            professores_ns.abort(404, "professor nao encontrado")
        return p.to_dict()

    @professores_ns.expect(professor_model, validate=True)
    @professores_ns.marshal_with(professor_model)
    def put(self, id):
        prof = ProfessorService.atualizar_professor(id, professores_ns.payload)
        return prof.to_dict(), 200

    def delete(self, id):
        ProfessorService.deletar_professor(id)
        return {"message": "professor excluído com sucesso"}, 204