Classe  Usuario():
    def  __init__ ( self, id, nome, email, senha, sexo, cidade, data_nascimento):
        self .id =  id
        self .nome = nome
        self .email = email
        self .senha = senha
        self .sexo = sexo
        self .cidade = cidade
        self .data_nascimento = data_nascimento

    def  publicar(self):
        passar

    def  curtir(self):
        passar

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()