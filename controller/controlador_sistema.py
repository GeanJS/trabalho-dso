from controller.controlador_usuario import ControladorUsuario
from controller.controlador_sistema_administrador import ControladorSistemaAdministrador
from controller.controlador_sistema_funcionario import ControladorSistemaFuncionario

class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario()

    def inicia_sistema(self):
        while True:
            usuario = self.__controlador_usuario.iniciar()

            if usuario.tipo == 'administrador':
                controlador_admin = ControladorSistemaAdministrador()
                controlador_admin.inicializa_sistema_administrador()
            elif usuario.tipo == 'funcionario':
                controlador_func = ControladorSistemaFuncionario()
                controlador_func.inicializa_sistema_funcionario()
