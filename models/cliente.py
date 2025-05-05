from datetime import datetime
from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, data_cadastro: datetime):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__data_cadastro = data_cadastro
        self.__historico_de_compras = []
        
    @property
    def data_cadastro(self) -> str:
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self, data_cadastro: datetime):
        self.__data_cadastro = data_cadastro
        
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao
        
    @property    
    def historico_de_compras(self):
        return self.__historico_de_compras
    
    def retorna_dados(self):
        dados = super().retorna_dados()
        dados.update({
            "data_cadastro": self.__data_cadastro,
            "descricao": self.__descricao
        })
        return dados
    