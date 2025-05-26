from controller.controlador_sistema_funcionario import ControladorSistemaFuncionario
from controller.controlador_funcionario import ControladorFuncionario
from controller.controlador_usuario import ControladorUsuario
import os

class ControladorSistemaAdministrador(ControladorSistemaFuncionario):
    def __init__(self, controlador_sistema, usuario_logado):
        super().__init__(controlador_sistema, usuario_logado)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__usuario_logado = usuario_logado
        self.__controlador_sistema = controlador_sistema
    
    @property
    def usuario_logado(self):
        return self.__usuario_logado
    
    def inicializa_sistema_administrador(self):
        while True:
            os.system('cls')
            opcao = self.tela_sistema.tela_opcoes_administrador()
            match opcao:
                case 1:
                    self.controlador_cliente.abre_menu()
                case 2:
                    self.__controlador_funcionario.abre_menu()
                case 3:
                    self.controlador_item.abre_menu()
                case 4:
                    self.controlador_local_armazenamento.abre_menu()
                case 5:
                    self.__controlador_usuario.abre_menu()
                case 6:
                    return
                case 0:
                    self.encerra_sistema()
                case _:
                    print("Opcao invalida. Digite um valor entre _ e _!")
    
    def encerra_sistema(self):
        print("Encerrando o Sistema...")
        exit(0)
        