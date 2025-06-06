from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str, registrador: str, data_cadastro: datetime):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__cpf = cpf
        self.__registrador = registrador
        self.__data_cadastro = data_cadastro
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email
        
    @property
    def endereco(self) -> str:
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco
        
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def registrador(self) -> str:
        return self.__registrador
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro
        
    def retorna_dados(self) -> dict:
        return {
            "nome": self.__nome,
            "telefone": self.__telefone,
            "email": self.__email,
            "endereco": self.__endereco,
            "cpf": self.__cpf,
            "registrador": self.registrador,
            "data_cadastro": self.__data_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        }