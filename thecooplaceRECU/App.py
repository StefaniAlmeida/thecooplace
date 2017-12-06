from model.Usuario import Usuario

    def criarRedeSocial():
        nome = str(input("Digite um nome da Rede Social: "))

    def inserirUsuario(usuario: Usuario):
    usuario = []
    nome = input("Digite seu nome:  ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha de usuário: ")
    sexo = input("Digite seu sexo: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    usuario = Usuario(nome, email, senha, sexo, data_nascimento)

    '''
    CRIANDO O MENU
    '''
    opecoes = int(input("Menu:\n "
                        "1- Criar rede social\n"
                        "2- Inserir usuário\n"
                        "3- Adicionar amigo\n"
                        "4- Enviar mensagem\n")
    try:

        if (op == 1:)
            criarRedeSocial()
        elif (op == 2:)
            inserirUsuario()
        elif (op == 3:)
            adicionarAmigo()
        elif (op == 4:)
            enviarMensagem()
            break

    except ValueError:
        print("Apenas números são válidos... Tente novamente!")

    if __name__ == '__main__':
        main()