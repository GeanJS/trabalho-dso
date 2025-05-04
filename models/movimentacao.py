from abc import ABC, abstractmethod
from datetime import datetime
from models.item import Item
from models.funcionario import Funcionario

class Movimentacao(ABC):
    def __init__(self, data: datetime, quantidade: int, item: Item, funcionario: Funcionario):
        self.data = data
        self.quantidade = quantidade
        self.item = item
        self.__funcionario = funcionario

    @property
    def data(self) -> datetime:
        return self.__data
    
    @data.setter
    def data(self, data: datetime):
        if not isinstance(data, datetime):
            raise ValueError("Insira uma data!")
        self.__data = data

    @property
    def quantidade(self)  -> int:
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    
    @property
    def item(self) -> Item: 
        return self.__item
    
    def retorna_dados(self) -> dict:
        return {
            "data": self.__data,
            "quantidade": self.__quantidade,
            "item": self.__item
        }

    @property
    def funcionario(self) -> Funcionario:
        return self.__funcionario