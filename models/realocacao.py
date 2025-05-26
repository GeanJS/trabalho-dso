from datetime import datetime
from models.movimentacao import Movimentacao
from models.item import Item
from models.funcionario import Funcionario
from models.local_armazenamento import LocalArmazenamento

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
    
    
    def retorna_dados(self) -> dict:
        dados = super().retorna_dados()
        dados.update({
            "tipo": "Realocacao",
            "origem": self.__local_origem.nome,
            "destino": self.__local_destino.nome
        })
        return dados
    