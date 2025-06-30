from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str, email:str, endereco: str, cpf: str, registrador: str, data_cadastro: datetime):
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
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        
        
    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone: str):
        if isinstance(novo_telefone, str):
            self.__telefone = novo_telefone
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, novo_email: str):
        if isinstance(novo_email, str):
            self.__email = novo_email
        
    @property
    def endereco(self) -> str:
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco: str):
        if isinstance(novo_endereco, str):
            self.__endereco = novo_endereco
            
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf: str):
        if isinstance(novo_cpf, str):
            self.__cpf = novo_cpf
        
    @property
    def registrador(self) -> str:
        return self.__registrador
    
    @registrador.setter
    def registrador(self, novo_registrador: str):
        if isinstance(novo_registrador, str):
            self.__registrador = novo_registrador
        
    @property
    def data_cadastro(self) -> datetime:
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self, nova_data: datetime):
        if isinstance(nova_data, datetime):
            self.__data_cadastro = nova_data
            
    def retorna_dados(self):
        return {
            "nome": self.__nome,
            "telefone": self.__telefone,
            "email": self.__email,
            "endereco": self.__endereco,
            "cpf": self.__cpf,
            "registrador": self.__registrador,
            "data_cadastro": self.__data_cadastro
        }