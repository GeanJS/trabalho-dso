from datetime import datetime
from models.venda import Venda
from views.tela_venda import TelaVenda
from dao.venda_dao import VendaDAO

class ControladorVenda:
    def __init__(self, controlador_cliente, controlador_item, controlador_funcionario, controlador_local):
        self.__tela_venda = TelaVenda()
        self.__controlador_cliente = controlador_cliente
        self.__controlador_item = controlador_item
        self.__controlador_funcionario = controlador_funcionario
        self.__controlador_local = controlador_local
        self.__venda_dao = VendaDAO(self.__controlador_item, self.__controlador_funcionario, self.__controlador_cliente)

    def abre_menu(self):
        while True:
            opcao = self.__tela_venda.menu_venda()
            if opcao == 1:
                self.nova_venda()
            elif opcao == 2:
                self.listar_vendas()
            elif opcao == 0:
                return
            else:
                self.__tela_venda.mostra_mensagem("Opção inválida!")

    def nova_venda(self):
        clientes = self.__controlador_cliente.retorna_clientes()
        if not clientes:
            self.__tela_venda.mostra_mensagem("Nenhum cliente cadastrado.")
            return

        cliente_indice = self.__tela_venda.seleciona_cliente(clientes)
        if cliente_indice is None or cliente_indice < 0 or cliente_indice >= len(clientes):
            self.__tela_venda.mostra_mensagem("Cliente inválido.")
            return
        cliente = clientes[cliente_indice]

        funcionarios = self.__controlador_funcionario.retorna_funcionarios()
        if not funcionarios:
            self.__tela_venda.mostra_mensagem("Nenhum funcionário cadastrado")
            return

        funcionario_indice = self.__tela_venda.seleciona_funcionario(funcionarios)
        if funcionario_indice is None or funcionario_indice < 0 or funcionario_indice >= len(funcionarios):
            self.__tela_venda.mostra_mensagem("Funcionário inválido")
            return
        funcionario = funcionarios[funcionario_indice]
        
        itens = self.__controlador_item.retorna_itens()
        if not itens:
            self.__tela_venda.mostra_mensagem("Nenhum item cadastrado.")
            return
        
        itens_venda = []
        
        while True:
            item_indice = self.__tela_venda.seleciona_item(itens)
            if item_indice is None or item_indice < 0 or item_indice >= len(itens):
                self.__tela_venda.mostra_mensagem("Item inválido")
                continue
            item = itens[item_indice]
            
            quantidade_maxima = item.quantidade_disponivel
            if quantidade_maxima == 0:
                self.__tela_venda.mostra_mensagem("Item sem estoque disponivel")
                continue
            
            quantidade = self.__tela_venda.pega_quantidade(quantidade_maxima)
            
            item.quantidade_disponivel -= quantidade
            locais = self.__controlador_local.retorna_locais()
            for local in locais:
                if item.codigo in local.itens and local.itens[item.codigo] >= quantidade:
                    local.itens[item.codigo] -= quantidade
                    if local.itens[item.codigo] <= 0:
                        del local.itens[item.codigo]
                    break
            
            itens_venda.append((item, quantidade))
            
            resposta = self.__tela_venda.pergunta_continuar()
            if resposta != 's':
                break
        
        if not itens_venda:
            self.__tela_venda.mostra_mensagem("Nenhum item adicionado a venda")
            return
        
        venda = Venda(
            data=datetime.now(),
            itens=itens_venda,
            funcionario=funcionario,
            cliente=cliente
        )
        
        self.__venda_dao.adiciona(venda)
        self.__controlador_item.atualiza()
        self.__controlador_local.atualiza()
        
        for item, _ in itens_venda:
            if item.quantidade_disponivel == 0:
                self.__controlador_item.remover_item_por_codigo(item.codigo)
        
        self.__tela_venda.mostra_mensagem("Venda realizada com sucesso")
        
    def listar_vendas(self):
        vendas = self.__venda_dao.lista()
        if not vendas:
            self.__tela_venda.mostra_mensagem("Nenhuma venda cadastrada.")
            return
        self.__tela_venda.mostra_vendas(vendas)
