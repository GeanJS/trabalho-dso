from controller.controlador_usuario import ControladorUsuario
from controller.controlador_sistema_administrador import ControladorSistemaAdministrador
from controller.controlador_sistema_funcionario import ControladorSistemaFuncionario
from models.usuario import Usuario

class ControladorSistema:
    def __init__(self):
        self.__usuarios = [
            Usuario('admin', 'admin', 'administrador'),
        ]
        self.__itens = []
        self.__clientes = []
        self.__controlador_usuario = ControladorUsuario(self, self.__usuarios)

    @property
    def lista_usuarios(self):
        return self.__usuarios
    
    @property
    def lista_itens(self):
        return self.__itens
    
    @property
    def lista_clientes(self):
        return self.__clientes
    
    def inicia_sistema(self):
        while True:
            usuario = self.__controlador_usuario.iniciar()

            if usuario is None:
                print("Encerrando o Sistema...")
                exit(0)
                
            if usuario.tipo == 'administrador':
                controlador_admin = ControladorSistemaAdministrador(self, usuario, self.__itens, self.__clientes)
                controlador_admin.inicializa_sistema_administrador()
            elif usuario.tipo == 'funcionario':
                controlador_func = ControladorSistemaFuncionario(self, usuario, self.__itens, self.__clientes)
                controlador_func.inicializa_sistema_funcionario()
