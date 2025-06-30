from datetime import datetime
from models.funcionario import Funcionario
from models.item import Item
from models.movimentacao import Movimentacao
from models.local_armazenamento import LocalArmazenamento

class Realocacao(Movimentacao):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario, local_origem: LocalArmazenamento, local_destino: LocalArmazenamento):
        super().__init__(data, funcionario)
        self.__quantidade = quantidade
        self.__item = item
        self.__local_origem = local_origem
        self.__local_destino = local_destino
    
    
    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    @property
    def item(self) -> Item:
        return self.__item
        
    @property
    def local_origem(self) -> LocalArmazenamento:
        return self.__local_origem
    
    @property
    def local_destino(self) -> LocalArmazenamento:
        return self.__local_destino
    
    
    def retorna_dados(self):
        return{
            "data": self.data.strftime("%Y-%m-%d %H:%M"),
            "item_codigo": self.__item.codigo,
            "quantidade": self.__quantidade,
            "funcionario_nome": self.funcionario.nome,
            "local_origem": self.__local_origem.nome,
            "local_destino": self.__local_destino.nome
        }