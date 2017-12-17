import mysql.connector
from database.Config import config
from Model.Postagem import Postagem

class PostagemDAO():

    def insert(postagem: Postagem):

        # Id da postagem inserida.
        idPostagem = 0
        # Script de Inserção.
        query = "INSERT INTO tb_postagem(usuario, texto) " \
                "VALUES(%s, %s)"
        # Valores.
        values = (postagem.usuario, postagem.texto)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id da postagem inserida no banco.
            if cursor.lastrowid:
                idPostagem = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
            # Retornar id da postagem.
            postagem.id = idPostagem
            return idPostagem

