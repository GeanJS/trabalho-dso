from abc import ABC, abstractmethod
from datetime import datetime
from models.item import Item
from models.funcionario import Funcionario

class Movimentacao(ABC):
    def __init__(self, data: datetime, funcionario: Funcionario):
        self.__data = data
        self.__funcionario = funcionario
        
    @property
    def data(self) -> datetime:
        return self.__data
    
    @property
    def funcionario(self) -> Funcionario:
        return self.__funcionario
    