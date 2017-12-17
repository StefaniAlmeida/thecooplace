import mysql.connector
from database.Config import config
from database.UsuarioDAO import UsuarioDAO
from Model.Usuario import Usuario

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
                "1) Ver perfil\n" \
                "2) -\n" \
                "0) Sair\n\n" \
                "->"
            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break

def main():
    criarBanco()
    menu()

if __name__ == '__main__':
    main()