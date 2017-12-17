class Usuario():
    def __init__(self, nome, email, senha, sexo, cidade, data_nascimento, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.sexo = sexo
        self.cidade = cidade
        self.data_nascimento = data_nascimento
        self.id = id