import mysql.connector
from database.Config import config
from Model.Usuario import Usuario

class UsuarioDAO():

    def insert(self, usuario: Usuario):

        # Id do usuario inserido.
        idUsuario = 0
        # Script de Inserção.
        query = "INSERT INTO tb_usuario(nome, email, senha, sexo, cidade, data_nascimento) " \
                "VALUES(%s, %s, %s, %s, %s, %s)"
        # Valores.
        values = (usuario.nome, usuario.email, usuario.senha, usuario.sexo, usuario.cidade, usuario.data_nascimento)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id do usuario inserido no banco.
            if cursor.lastrowid:
                idUsuario = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
            # Retornar id do usuario.
            usuario.id = idUsuario
            return idUsuario

    def listar(self):
        query = "SELECT * FROM tb_usuario"

        try:
            conn = mysql.connector.connect(**config)

            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)

            usuarios = []

            for row in cursor.fetchall():
                id = row['id']
                nome = row['nome']
                email = row['email']
                senha = row['senha']
                sexo = row['sexo']
                cidade = row['cidade']
                data_nascimento = row['data_nascimento']

                usuario = Usuario(nome, email, senha, sexo, cidade, data_nascimento, id)
                usuarios.append(usuario)

        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

            return usuarios

    def addAmigo(self, id1, id2):
        query = "INSERT INTO tb_amigo(usuario1_id, usuario2_id) " \
                "VALUES(%s, %s)"
        values = (id1, id2)

        try:
            conn = mysql.connector.connect(**config)

            cursor = conn.cursor()
            cursor.execute(query, values)

            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def desfazerAmizade(self, id1, id2):
        query = "DELETE FROM tb_amigo " \
                "WHERE (usuario1id = %s and usuario2id = %s) or (usuario2id = %s and usuario1id = %s)"
        values = (id1, id2, id2, id1)

        try:
            conn = mysql.connector.connect(**config)

            cursor = conn.cursor()
            cursor.execute(query, values)

            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def verificarLogin(self, email, senha):
        query = "SELECT * FROM tb_usuario " \
                "WHERE email = %s and senha = %s"
        values = (email, senha)

        usuario = None

        try:
            conn = mysql.connector.connect(**config)

            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, values)

            row = cursor.fetchone()

            if(not row is None):
                id = row['id']
                nome = row['nome']
                email = row['email']
                senha = row['senha']
                sexo = row['sexo']
                cidade = row['cidade']
                data_nascimento = row['data_nascimento']

                usuario = Usuario(nome, email, senha, sexo, cidade, data_nascimento, id)

        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

            return usuario