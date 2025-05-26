from datetime import datetime
from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, registrador: str, data_cadastro: datetime):
        super().__init__(nome, telefone, email, endereco, cpf, registrador, data_cadastro)
        self.__historico_de_compras = []
        
    @property    
    def historico_de_compras(self):
        return self.__historico_de_compras
    
    def retorna_dados(self):
        dados = super().retorna_dados()
        return dados
    