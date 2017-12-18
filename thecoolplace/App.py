import mysql.connector
from database.Config import config
from database.UsuarioDAO import UsuarioDAO
from database.MensagemDAO import MensagemDAO
from Model.Usuario import Usuario
from Model.Mensagem import Mensagem
from datetime import date

def criarBanco():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE tb_usuario(
                id int primary key auto_increment,
                nome varchar(100) not null,
                email varchar(30) not null,
                senha varchar(20) not null,
                sexo varchar(20),
                cidade varchar(30),
                data_nascimento varchar(10)
            );
        """)

        cursor.execute("""
            CREATE TABLE tb_mensagem(
                id int primary key auto_increment,
                remetente_id int not null,
                destinatario_id int not null,
                texto text,
                data_envio varchar(10),
                foreign key(remetente_id) references tb_usuario(id),
                foreign key(destinatario_id) references tb_usuario(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE tb_postagem(
                id int primary key auto_increment,
                usuario_id int not null,
                texto text,
                foreign key(usuario_id) references tb_usuario(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE tb_amigo(
                usuario1_id int not null,
                usuario2_id int not null,
                foreign key(usuario1_id) references tb_usuario(id),
                foreign key(usuario2_id) references tb_usuario(id)
            );
        """)
    except mysql.connector.ProgrammingError:
        return

def menu():
    while True:
        try:
            opcao = int(input(
                "1) Login\n" \
                "2) Registro\n" \
                "0) Sair\n\n" \
                "->"
            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break
        elif(opcao == 1):
            email = input("E-mail: ")
            senha = input("Senha: ")

            usuario = UsuarioDAO().verificarLogin(email, senha)

            if(usuario is None):
                print("Credenciais incorretos.\n")
                continue
            else:
                menuDeUsuario(usuario)
        elif(opcao == 2):
            try:
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                sexo = input("Sexo: ")
                cidade = input("Cidade: ")
                data_nascimento = input("Data de nascimento (dd/mm/YYYY): ")

                usuario = Usuario(nome, email, senha, sexo, cidade, data_nascimento)
                UsuarioDAO().insert(usuario)

                menuDeUsuario(usuario)
            except:
                print("Erro!")
                continue

def menuDeUsuario(usuario: Usuario):
    while True:
        try:
            opcao = int(input(
                "\n1) Ver perfil\n" \
                "2) Add Amigo\n" \
                "3) Mandar mensagem\n" \
                "4) Ver amigos\n" \
                "5) Ver mensagens\n" \
                "0) Sair\n\n" \
                "->"
            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break
        elif(opcao == 1):
            print("\nNome: %s" \
                  "\nE-mail: %s" \
                  "\nSexo: %s" \
                  "\nCidade: %s" \
                  "\nData de nascimento: %s" % (usuario.nome, usuario.email, usuario.sexo, usuario.cidade, usuario.data_nascimento))
        elif(opcao == 2):
            nome = input("Nome: ")

            usuarios = UsuarioDAO().procurarPeloNome(nome)

            if(len(usuarios) == 0):
                print("Nenhum usuário com este nome encontrado.")
                continue
            elif(len(usuarios) == 1):
                try:
                    UsuarioDAO().addAmigo(usuario.id, usuarios[0].id)
                    print("Amigo adicionado.")
                except Exception as err:
                    print(err)
            else:
                print()
                i = 1
                for u in usuarios:
                    print("%s) %s - %s" % (i, u.nome, u.email))
                    i += 1

                n = input("Digite o número do usuário: ")

                u = UsuarioDAO().procurarPeloId(usuarios[u - 1].id)

                if(u is None):
                    print("Usuário inválido.")
                else:
                    UsuarioDAO().addAmigo(usuario.id, u.id)
                    print("%s foi adicionado aos seus amigos." % (u.nome))
        elif(opcao == 3):
            nome = input("Nome: ")

            usuarios = UsuarioDAO().procurarPeloNome(nome)

            if (len(usuarios) == 0):
                print("Nenhum usuário com este nome encontrado.")
                continue
            elif (len(usuarios) == 1):
                try:
                    texto = input("Mensagem: ")
                    mensagem = Mensagem(usuario, usuarios[0], texto, str(date.today()))

                    MensagemDAO().insert(mensagem)
                    print("Mensagem enviada.")
                except Exception as err:
                    print(err)
            else:
                print()
                i = 1
                for u in usuarios:
                    print("%s) %s - %s" % (i, u.nome, u.email))
                    i += 1

                n = input("Digite o número do usuário: ")

                u = UsuarioDAO().procurarPeloId(usuarios[u - 1].id)

                if (u is None):
                    print("Usuário inválido.")
                else:
                    try:
                        texto = input("Mensagem: ")
                        mensagem = Mensagem(usuario, usuarios[0], texto, str(date.today()))

                        MensagemDAO().insert(mensagem)
                        print("Mensagem enviada.")
                    except Exception as err:
                        print(err)

        elif(opcao == 4):
            amigos = UsuarioDAO().listarAmigos(usuario.id)

            i = 1
            for amigo in amigos:
                print("%s) %s" % (i, amigo.nome))
        elif(opcao == 5):
            mensagens = MensagemDAO().listarDeUsuario(usuario.id)

            for mensagem in mensagens:
                print("(%s) %s -> %s: %s" % (mensagem.data_envio, mensagem.remetente.nome, mensagem.destinatario.nome, mensagem.texto))

def main():
    criarBanco()
    menu()

if __name__ == '__main__':
    main()