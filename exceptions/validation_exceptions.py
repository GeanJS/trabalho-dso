class ValidationException(Exception):
    def __init__(self, campo, mensagem):
        self.campo = campo
        self.mensagem = mensagem
        super().__init__(f"Erro em '{campo}': {mensagem}")