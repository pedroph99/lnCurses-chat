class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.mensagens = []

    def enviar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)

    def __str__(self):
        return f'Usuario: {self.nome}, Mensagens: {self.mensagens}'

