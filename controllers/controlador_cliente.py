from dao.cliente_dao import ClienteDAO
from models.cliente import Cliente
from views.tela_cliente import TelaCliente
from datetime import datetime

class ControladorCliente:
    def __init__(self, controlador_usuario):
        self.__clientes_dao = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_usuario = controlador_usuario
        
    def abre_menu(self):
        while True:
            opcao = self.__tela_cliente.menu_cliente()
            match opcao:
                case 1:
                    self.cadastrar_cliente()
                case 2:
                    self.editar_cliente()
                case 3:
                    self.remover_cliente()
                case 4:
                    self.listar_clientes()
                case 0:
                    return
                case _:
                    self.__tela_cliente.mostra_mensagem("Erro")
                
    
    def cadastrar_cliente(self):
        dados = self.__tela_cliente.pegar_dados_cliente()
        registrador = self.__controlador_usuario.retorna_usuario_logado().nome
        if dados is None:
            self.__tela_cliente.mostra_mensagem("Cadastro Cancelado")
            return
        
        cliente = Cliente(
            nome=dados["nome"],
            telefone=dados["telefone"],
            endereco=dados["endereco"],
            email=dados["email"],
            cpf=dados["cpf"],
            registrador=registrador,
            data_cadastro=datetime.now()
        )
        
        self.__clientes_dao.adiciona(cliente)
        self.__tela_cliente.mostra_mensagem("Cliente cadastrado com sucesso")
    
    def editar_cliente(self):
        clientes = self.__clientes_dao.lista()
        if not clientes:
            self.__tela_cliente.mostra_mensagem("\nNenhum cliente cadastrado\n")
            return
            
        indice = self.__tela_cliente.seleciona_cliente(clientes)
        
        if indice is not None and 0 <= indice < len(clientes):
            cliente = clientes[indice]
            dados_atuais = cliente.retorna_dados()
            
            novos_dados = self.__tela_cliente.pegar_dados_cliente(dados_atuais)
            if novos_dados is None:
                self.__tela_cliente.mostra_mensagem("Edição Cancelada\n")
                return
            
            cliente.nome = novos_dados["nome"]
            cliente.telefone = novos_dados["telefone"]
            cliente.endereco = novos_dados["endereco"]
            cliente.email = novos_dados["email"]
            cliente.cpf = novos_dados["cpf"]
            
            self.__clientes_dao.atualiza()
            self.__tela_cliente.mostra_mensagem("Cliente editado com sucesso")
        else:
            self.__tela_cliente.mostra_mensagem("Índice inválido")
    
    
    def remover_cliente(self):
        clientes = self.__clientes_dao.lista()
        if not clientes:
            self.__tela_cliente.mostra_mensagem("\nNenhum cliente encontrado")
            return
            
        indice = self.__tela_cliente.seleciona_cliente(clientes)
        
        if indice is not None and 0 <= indice < len(clientes):
            cliente = clientes[indice]
            self.__clientes_dao.remove(cliente)
            self.__tela_cliente.mostra_mensagem("Cliente removido com sucesso!!")
            
    def listar_clientes(self):
        clientes = self.__clientes_dao.lista()
        self.__tela_cliente.mostra_clientes(clientes)

    def retorna_clientes(self):
        return self.__clientes_dao.lista()

    def busca_por_nome(self, nome: str):
        clientes = self.__clientes_dao.lista()
        for cliente in clientes:
            if cliente.nome == nome:
                return cliente
        return None