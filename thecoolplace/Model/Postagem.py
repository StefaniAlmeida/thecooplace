from database.Config import config
import mysql.connector

class Postagem():
    def __init__(self, usuario, texto, id=None):
        self.usuario = usuario
        self.texto = texto
        self.id = id

   
