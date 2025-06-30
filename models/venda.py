from datetime import datetime
from models.funcionario import Funcionario
from models.cliente import Cliente
from models.item import Item
from models.movimentacao import Movimentacao

class Venda(Movimentacao):
    def __init__(self, data: datetime, itens: list[tuple[Item, int]], funcionario: Funcionario, cliente: Cliente):
        super().__init__(data, funcionario)
        self.__itens = itens
        self.__cliente = cliente
       
    @property
    def itens(self):
        return self.__itens 
        
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
    
    
    def valor_total(self):
        return sum(item.valor_esperado_da_venda() * quantidade for item, quantidade in self.__itens )
    
    
    def retorna_dados(self):
        return {
            "data": self.data.strftime("%Y-%m-%d %H:%M"),
            "funcionario": self.funcionario.nome,
            "cliente": self.cliente.nome,
            "itens": [
                {
                    "codigo": item.codigo,
                    "descricao": item.descricao,
                    "quantidade": qtd,
                    "valor_unitario": item.valor_esperado_da_venda()
                } for item, qtd in self.__itens
            ],
            "valor_total": self.valor_total()
        }