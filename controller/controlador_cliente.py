from models.cliente import Cliente
from view.tela_cliente import TelaCliente
from utils.validacao import confirma_acao

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
                case 3:
                    self.editar_cliente()
                case 4:
                    self.remover_cliente()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")
    
    
    def cadastrar_cliente(self):
        dados = self.__tela_cliente.pega_dados_cliente()
        if dados is None:
            self.__tela_cliente.mostra_mensagem("Cadastro cancelado")
            return
        
        usuario_logado = self.__controlador_sistema.usuario_logado
        
        cliente = Cliente(
            nome=dados["nome"],
            telefone=dados["telefone"],
            endereco=dados["endereco"],
            email=dados["email"],
            cpf=dados["cpf"],
            registrador=usuario_logado.nome,
            data_cadastro=dados["data"]
        )
        
        self.__clientes.append(cliente)
        self.__tela_cliente.mostra_mensagem("Cliente Cadastrado com Sucesso!!")
    
    def editar_cliente(self):
        if not self.__clientes:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado para editar")
            return
        
        indice = self.__tela_cliente.seleciona_cliente(self.__clientes)
        
        if 0 <= indice < len(self.__clientes):
            cliente = self.__clientes[indice]
            novos_dados = self.__tela_cliente.pega_dados_cliente()
            if novos_dados is None:
                self.__tela_cliente.mostra_mensagem("Edicao cancelada")
                return
            
            cliente.nome = novos_dados["nome"]
            cliente.telefone = novos_dados["telefone"]
            cliente.endereco = novos_dados["endereco"]
            cliente.email = novos_dados["email"]
            cliente.cpf = novos_dados["cpf"]
            
            self.__tela_cliente.mostra_mensagem("Cliente editado com sucesso")
        else:
            self.__tela_cliente.mostra_mensagem("Indice invalido")
            
    def remover_cliente(self):
        if not self.__clientes:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado para remover")
            return

        indice = self.__tela_cliente.seleciona_cliente(self.__clientes)
        
        if 0<= indice < len(self.__clientes):
            cliente = self.__clientes[indice]
            
            if confirma_acao(f"Tem certeza que deseja remover o cliente {cliente.nome}?"):
                self.__clientes.pop(indice)
                self.__tela_cliente.mostra_mensagem(f"Cliente {cliente.nome} removido com sucesso")
            else:
                self.__tela_cliente.mostra_mensagem("Remocao cancelada")
        else:
            self.__tela_cliente.mostra_mensagem("Indice invalido")
    
    def listar_clientes(self):
        self.__tela_cliente.mostra_clientes(self.__clientes)
                
    def retornar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()