from views.tela_sistema import TelaSistema
from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_local_armazenamento import ControladorLocalArmazenamento
from controllers.controlador_item import ControladorItem
from controllers.controlador_realocacao import ControladorRealocacao
from controllers.controlador_venda import ControladorVenda
from controllers.controlador_funcionario import ControladorFuncionario

class ControladorSistemaFuncionario:
    def __init__(self, controlador_usuario):
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuario = controlador_usuario
        self.__controlador_cliente = ControladorCliente(controlador_usuario)
        self.__controlador_funcionario = ControladorFuncionario(controlador_usuario)
        self.__controlador_local_armazenamento = ControladorLocalArmazenamento()
        self.__controlador_item = ControladorItem(self.__controlador_local_armazenamento)
        self.__controlador_realocacao = ControladorRealocacao(self.__controlador_item, self.__controlador_local_armazenamento, controlador_usuario)
        self.__controlador_venda = ControladorVenda(self.__controlador_cliente, self.controlador_item, self.__controlador_funcionario, self.__controlador_local_armazenamento)
        
    @property
    def tela_sistema(self):
        return self.__tela_sistema
    
    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
    
    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
        
    @property
    def controlador_local_armazenamento(self):
        return self.__controlador_local_armazenamento
    
    @property
    def controlador_item(self):
        return self.__controlador_item
    
    @property
    def controlador_realocacao(self):
        return self.__controlador_realocacao
    
    @property
    def controlador_venda(self):
        return self.__controlador_venda
    
    def inicializa_sistema_funcionario(self):
        while True:
            opcao = self.__tela_sistema.menu_funcionario()
            match opcao:
                case 1:
                    self.__controlador_cliente.abre_menu()
                case 2:
                    self.__controlador_local_armazenamento.abre_menu()
                case 3:
                    self.__controlador_item.abre_menu()
                case 4:
                    self.__controlador_realocacao.abre_menu()
                case 5:
                    self.__controlador_venda.abre_menu()
                case 0:
                    return
                case _:
                    self.__tela_sistema.mostra_mensagem("Erro")