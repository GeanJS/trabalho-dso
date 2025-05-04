from models.movimentacao import Movimentacao
from models.funcionario import Funcionario
from models.cliente import Cliente
from models.item import Item
from datetime import datetime

class Venda(Movimentacao):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario, cliente: Cliente):
        super().__init__(data, quantidade, item, funcionario)
        self.__cliente = cliente
        

    @property
    def cliente(self) -> Cliente:
        return self.__cliente


    def retorna_dados(self) -> dict:
        dados = super().retorna_dados()
        dados.update({
            "funcionario": self.__funcionario.nome,
            "cliente": self.__cliente.nome,
            "tipo": "Venda",
            "valor_venda": self.valor_venda()
        })
        return dados

    def valor_venda(self) -> float:
        return self.__quantidade * self.__item.valor_esperado_venda() 