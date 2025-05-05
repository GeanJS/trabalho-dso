from controller.controlador_cliente import ControladorCliente
from view.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente()
        self.__tela_sistema = TelaSistema()
        
    @property
    def controlador_cliente(self):
        return self.__controlador_amigos
    
    def encerra_sistema(self):
        exit(0)
        
    def abre_tela(self):
        pass