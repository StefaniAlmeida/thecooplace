import psycopg2.connector
from model.Usuario import Usuario
from database.configDB import config

class UsuarioDAO():

    def inserirUsuario(usuario: Usuario):

        query = "INSERT INTO usuario(id_usuario, nome, nascimento, genero, email, senha) " \
                "VALUES(%i, %s, %s, %c, %s, %S)"
        values = (usuario.id_usuario, usuario.nome, usuario.nascimento, usuario.genero, usuario.email, usuario.senha)

        try:
            #conectando com o BD
            conn = psycopg2.connect("dbusuario=mydb user=myuser")

            #Abrindo o cursor
            cur = conn.cursor()

            cur.execute(query, values)

            conn.commit()

        except psycopg2.connector.Error as error:
            print(error)

        finally:
            cur.close()
            conn.close()
            exit()
