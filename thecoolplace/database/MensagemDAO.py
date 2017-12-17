import mysql.connector
from database.Config import config
from Model.Mensagem import Mensagem

class MensagemDAO():
    def insert(mensagem: Mensagem):

        # Id da mensagem inserida.
        idMensagem = 0
        # Script de Inserção.
        query = "INSERT INTO tb_mensagem(remetente, destinatario, texto, data_envio) " \
                "VALUES(%s, %s, %s, %s)"
        # Valores.
        values = (mensagem.remetente, mensagem.destinatario, mensagem.texto, mensagem.data_envio)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id da mensagem inserida no banco.
            if cursor.lastrowid:
                idMensagem = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
            # Retornar id da mensagem.
            mensagem.id = idMensagem
            return idMensagem

