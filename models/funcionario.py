from models.pessoa import Pessoa#não entendi o motivo de estar dando erro em from pessoa import Pessoa
from models import cargo
from datetime import datetime

class Funcionario(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, funcao:str, salario: float, data_contratacao: datetime):
        Pessoa.__init__(self, nome, telefone, email, endereco, cpf)
        cargo.__init__(self, funcao, salario)
        self.__data_contratacao = data_contratacao
        self.__historico_de_vendas = []

    @property
    def data_contratacao(self) -> datetime:
        return self.__data_contratacao
        
    @data_contratacao.setter
    def data_contratacao(self, data_contratacao: datetime):
        self.__data_contratacao = data_contratacao

    @property
    def historico_de_vendas(self):
        return self.__historico_de_vendas
        
    def retorna_dados(self):
        dados = super().retorna_dados()
        dados.update({

        })
        return dados