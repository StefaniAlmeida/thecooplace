class Mensagem():
    def __init__(self, remetente, destinatario, texto, data_envio, id=None):
        self.destinatario = destinatario
        self.remetente = remetente
        self.texto = texto
        self.data_envio = data_envio
        self.id = id