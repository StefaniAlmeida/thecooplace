from model.Mensagem import Mensagem
class Feed(Mensagem):
    def __init__(self, id, destinatario, remetente, data_envio):
        self.id = id
        self.destinatario = destinatario
        auto.remetente = Remetente
        self.data_envio = data_envio