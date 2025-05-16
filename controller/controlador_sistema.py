from view.tela_sistema import TelaSistema
from controller.controlador_cliente import ControladorCliente

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente(self)
    
    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            match opcao:
                case 1:
                    self.__controlador_cliente.abre_menu()
                case 0:
                    self.encerra_sistema()
                case _:
                    print("Opcao invalida")
    
    def encerra_sistema(self):
        print("Encerrando o Sistema...")
        exit(0)
        