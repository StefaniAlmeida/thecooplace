from model.Mensagem import Mensagem
class Chat(Mensagem):
    def __init__(self, conversa, id):
        auto.conversa = conversa
        self.id = id