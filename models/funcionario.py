from models.pessoa import Pessoa
from models.cargo import Cargo
from datetime import datetime

class Funcionario(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, registrador:str,  cargo: Cargo, data_cadastro: datetime):
        super().__init__(nome, telefone, email, endereco, cpf, registrador, data_cadastro)
        self.__cargo = cargo
        self.__historico_de_vendas = []

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novo_cargo: Cargo):
        self.__cargo = novo_cargo
        
    @property
    def historico_de_vendas(self):
        return self.__historico_de_vendas
        
    def retorna_dados(self):
        dados = super().retorna_dados()
        dados.update({
            "funcao": self.__cargo.funcao,
            "salario": self.__cargo.salario
        })
        return dados