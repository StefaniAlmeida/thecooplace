from database.Config import config
import mysql.connector
from Model.Usuario import Usuario
from Model.Postagem import Postagem

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
    except mysql.connector.ProgrammingError:
        return

def menu():
    while True:
        try:
            opcao = int(input(
                "1) Inserir usuário\n" \
                "2) Inserir postagem\n" \
                "0) Sair\n\n" \
                "->"
            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break
        elif(opcao == 1):
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            sexo = input("Sexo: ")
            cidade = input("Cidade: ")
            data_nascimento = input("Data de nascimento: ")

            usuario = Usuario(nome, email, senha, sexo, cidade, data_nascimento)
            usuario.insert()
            print("Usuário cadastrado.")
        elif(opcao == 2):
            try:
                id = int(input("ID do dono da postagem: "))
            except:
                print("Valor inválido.")
                continue
            texto = input("Texto: ")
            postagem = Postagem(id, texto)
            postagem.insert()
            print("Postagem inserida.")

def main():
    criarBanco()
    menu()

if __name__ == '__main__':
    main()