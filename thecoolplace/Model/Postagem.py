from database.Config import config
import mysql.connector

class Postagem():
    def __init__(self, usuario, texto, id=None):
        self.usuario = usuario
        self.texto = texto
        self.id = id

    def insert(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_postagem(usuario_id, texto)
            VALUES(%s, %s)
        """, (self.usuario, self.texto))

        self.id = cursor.lastrowid

        conn.commit()
        cursor.close()