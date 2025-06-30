from controllers.controlador_sistema_funcionario import ControladorSistemaFuncionario
from controllers.controlador_funcionario import ControladorFuncionario

class ControladorSistemaAdministrador(ControladorSistemaFuncionario):
    def __init__(self,controlador_usuario):
        super().__init__(controlador_usuario)
        self.__controlador_funcionario = ControladorFuncionario(controlador_usuario)
        
    def inicializa_sistema_administrador(self):
        while True:
            opcao = self.tela_sistema.menu_administrador()
            match opcao:
                case 1:
                    self.controlador_cliente.abre_menu()
                case 2:
                    self.__controlador_funcionario.abre_menu()
                case 3:
                    self.controlador_local_armazenamento.abre_menu()
                case 4:
                    self.controlador_item.abre_menu()
                case 5:
                    self.controlador_realocacao.abre_menu()
                case 6:
                    self.controlador_venda.abre_menu()
                case 7:
                    self.controlador_usuario.abre_menu()
                case 0:
                    return
                case _:
                    self.tela_sistema.mostra_mensagem("Erro")