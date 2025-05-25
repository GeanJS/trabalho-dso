from models.cliente import Cliente
from view.tela_cliente import TelaCliente

class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
    
    def abre_menu(self):
        while True:
            opcao = self.__tela_cliente.menu_cliente()
            match opcao:
                case 1:
                    self.cadastrar_cliente()
                case 2:
                    self.listar_clientes()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")
    
    
    def cadastrar_cliente(self):
        dados = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados["nome"], dados["telefone"], dados["endereco"], dados["email"], dados["cpf"], dados["data"])
        self.__clientes.append(cliente)
        self.__tela_cliente.mostra_mensagem("Cliente cadastrado com sucesso!!")
    
    def listar_clientes(self):
        self.__tela_cliente.mostra_clientes(self.__clientes)
                
    def retornar(self):
        self.__controlador_sistema.inicia_sistema()