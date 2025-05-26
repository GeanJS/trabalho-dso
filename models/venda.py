from datetime import datetime
from models.movimentacao import Movimentacao
from models.funcionario import Funcionario
from models.item import Item
from models.cliente import Cliente

class Venda(Movimentacao):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario, cliente: Cliente):
        super().__init__(data, quantidade, item, funcionario)
        self.__cliente = cliente
        self.__valor_total = self.calcula_valor_total()

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def valor_total(self):
        return self.__valor_total
    
    def calcula_valor_total(self):
        return self.quantidade * self.item.valor_esperado_venda()