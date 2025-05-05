from view.tela_cliente import TelaCliente
from models.cliente import Cliente

class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__cliente = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        
    def busca_por_cpf(self, cpf: str):
        for cliente in self.__cliente:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def cadastra_cliente(self):
        pass
    
    def altera_cliente(self):
        pass
    
    def exclui_cliente(self):
        pass
    
    def lista_cliente(self):
        pass
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    