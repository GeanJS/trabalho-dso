from view.tela_sistema import TelaSistema
from controller.controlador_cliente import ControladorCliente
from controller.controlador_item import ControladorItem
from controller.controlador_local_armazenamento import ControladorLocalArmazenamento
from controller.controlador_usuario import ControladorUsuario

class ControladorSistemaFuncionario:
    def __init__(self, controlador_sistema, usuario_logado):
        self.__controlador_sistema = controlador_sistema
        self.__usuario_logado = usuario_logado
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_item = ControladorItem(self)
        self.__controlador_local_armazenamento = ControladorLocalArmazenamento(self)
    
    @property
    def usuario_logado(self):
        return self.__usuario_logado
    
    @property
    def tela_sistema(self):
        return self.__tela_sistema
        
    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
        
    @property
    def controlador_item(self):
        return self.__controlador_item
        
    @property
    def controlador_local_armazenamento(self):
        return self.__controlador_local_armazenamento
    
    
    
    def inicializa_sistema_funcionario(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes_funcionario()
            match opcao:
                case 1:
                    self.__controlador_cliente.abre_menu()
                case 2:
                    self.__controlador_item.abre_menu()
                case 3:
                    self.__controlador_local_armazenamento.abre_menu()
                case 4:
                    self.__controlador_sistema.inicia_sistema()
                case 0:
                    self.encerra_sistema()
                case _:
                    print("Opcao invalida. Digite um valor entre _ e _!")
    
    def encerra_sistema(self):
        print("Encerrando o Sistema...")
        exit(0)
        