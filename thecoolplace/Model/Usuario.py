from database.Config import config
import mysql.connector

class Usuario():
    def __init__(self, nome, email, senha, sexo, cidade, data_nascimento, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.sexo = sexo
        self.cidade = cidade
        self.data_nascimento = data_nascimento
        self.id = id

    def insert(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_usuario(nome, email, senha, sexo, cidade, data_nascimento)
            VALUES(%s, %s, %s, %s, %s, %s)
        """, (self.nome, self.email, self.senha, self.sexo, self.cidade, self.data_nascimento))

        self.id = cursor.lastrowid

        conn.commit()
        cursor.close()