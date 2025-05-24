from datetime import datetime
from models.movimentacao import Movimentacao
from item import Item
from funcionario import Funcionario
from local_armazenamento import LocalArmazenamento

class Realocacao(Movimentacao):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario, local_origem: LocalArmazenamento, local_destino: LocalArmazenamento):
        super().__init__(data, quantidade, item, funcionario)
        self.__local_origem = local_origem
        self.__local_destino = local_destino

    @property
    def local_origem(self):
        return self.__local_origem

    @property
    def local_destino(self):
        return self.__local_destino
    