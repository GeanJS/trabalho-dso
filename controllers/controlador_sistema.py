from controllers.controlador_usuario import ControladorUsuario
from controllers.controlador_sistema_funcionario import ControladorSistemaFuncionario
from controllers.controlador_sistema_administrador import ControladorSistemaAdministrador


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario()

    def inicia_sistema(self):
        while True:
            usuario = self.__controlador_usuario.login()
            
            if usuario is None:
                continue
                
            if usuario.tipo == 'administrador':
                controlador_administrador = ControladorSistemaAdministrador(self.__controlador_usuario)
                controlador_administrador.inicializa_sistema_administrador()
                
            elif usuario.tipo == 'funcionario':
                controlador_funcionario = ControladorSistemaFuncionario(self.__controlador_usuario)
                controlador_funcionario.inicializa_sistema_funcionario()