from controller.controlador_sistema_funcionario import ControladorSistemaFuncionario
from controller.controlador_funcionario import ControladorFuncionario
from controller.controlador_usuario import ControladorUsuario
import os

class ControladorSistemaAdministrador(ControladorSistemaFuncionario):
    def __init__(self, controlador_sistema, usuario_logado, itens, clientes):
        super().__init__(controlador_sistema, usuario_logado, itens, clientes)
        self.__controlador_usuario = ControladorUsuario(self, controlador_sistema.lista_usuarios)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__usuario_logado = usuario_logado
        self.__controlador_sistema = controlador_sistema
    
    @property
    def usuario_logado(self):
        return self.__usuario_logado
    
    def inicializa_sistema_administrador(self):
        try:
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
                        self.__controlador_usuario.abre_menu()
                    case 5:
                        self.__controlador_sistema.inicia_sistema()
                    case 0:
                        self.encerra_sistema()
                    case _:
                        print("Opcao invalida. Digite um valor entre 1 e 5!")
        except KeyboardInterrupt:
            return None
        
    def encerra_sistema(self):
        print("Encerrando o Sistema...")
        exit(0)
        