import mysql.connector
from database.Config import config
from database.UsuarioDAO import UsuarioDAO
from Model.Mensagem import Mensagem

class MensagemDAO():

    def insert(self, mensagem: Mensagem):

        # Id da mensagem inserida.
        idMensagem = 0
        # Script de Inserção.
        query = "INSERT INTO tb_mensagem(remetente_id, destinatario_id, texto, data_envio) " \
                "VALUES(%s, %s, %s, %s)"
        # Valores.
        values = (mensagem.remetente.id, mensagem.destinatario.id, mensagem.texto, mensagem.data_envio)

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

    def listarDeUsuario(self, id):
        query = "SELECT * FROM tb_mensagem " \
                "WHERE destinatario_id = %s or remetente_id = %s"
        values = (id, id)

        mensagens = []

        try:
            conn = mysql.connector.connect(**config)

            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, values)

            for row in cursor.fetchall():
                usuarioDAO = UsuarioDAO()

                id = row['id']
                remetente = usuarioDAO.procurarPeloId(row['remetente_id'])
                destinatario = usuarioDAO.procurarPeloId(row['destinatario_id'])
                texto = row['texto']
                data_envio = row['data_envio']

                mensagem = Mensagem(remetente, destinatario, texto, data_envio, id)
                mensagens.append(mensagem)

        except mysql.connector.Error as error:
            print(error)
        except Exception as err:
            print(err)
        finally:
            cursor.close()
            conn.close()

            return mensagens