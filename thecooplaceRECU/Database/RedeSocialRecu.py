import mysql.connector
from model.RedeSocialDinamics import RedeSocialDinamics
from database.configDB import config

class RedeSocialRecu():

    def inserirRedeSocial(redeSocial: RedeSocialDinamics):


        idRedeSocial = 0

        query = "INSERT INTO redesocial(nome, descricao) " \
                "VALUES(%s, %s)"

        values = (redeSocial.nome, redeSocial.descricao)

        try:
            # Conexão com a base de dados.
            conn =  psycopg2.connector.connect()
            cur = conn.cur()
            cur.execute(query, values)

            if cur.lastrowid:
                idRedeSocial = cursor.lastrowid

            conn.commit()

        except psycopg2.connector.Error as error:
            print(error)

       finally:
            cur.close()
            conn.close()

        return idRedeSocial