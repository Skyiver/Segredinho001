class User:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return vars(self)

# Dados iniciais (se necessário)
users = {
    "user": User(1, "João Silva", "joao.silva@email.com")
}