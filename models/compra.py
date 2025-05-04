from models.movimentacao import Movimentacao
from models.funcionario import Funcionario
from models.item import Item
from datetime import datetime

class Compra(Movimentacao):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario, ):
        super().__init__(data, quantidade, item, funcionario)

    def retorna_dados(self):
        dados = super().retorna_dados()
        dados.update({
            "funcionario": self.__funcionario.nome,
            "tipo": "Compra",
            "valor_compra": self.valor_compra()
        })
        return dados
    
    def valor_compra(self) -> float:
        return self.__quantidade * self.__item.valor_entrada