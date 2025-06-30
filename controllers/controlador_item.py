from views.tela_item import TelaItem
from models.item import Item
from dao.item_dao import ItemDAO

class ControladorItem:
    def __init__(self, controlador_local):
        self.__item_dao = ItemDAO()
        self.__tela_item = TelaItem()
        self.__controlador_local = controlador_local

    def abre_menu(self):
        while True:
            opcao = self.__tela_item.menu_item()
            match opcao:
                case 1:
                    self.cadastrar_item()
                case 2:
                    self.editar_item()
                case 3:
                    self.remover_item()
                case 4:
                    self.listar_itens()
                case 0:
                    break
                case _:
                    self.__tela_item.mostra_mensagem("Opção inválida.")

    def cadastrar_item(self):
        locais = self.__controlador_local.retorna_locais()

        if not locais:
            self.__tela_item.mostra_mensagem("Nenhum local de armazenamento disponível. Cadastre um local antes de adicionar itens.")
            return

        dados = self.__tela_item.pega_dados_item(locais)
        if dados is None:
            return

        item = Item(
            codigo=dados["codigo"],
            descricao=dados["descricao"],
            valor_entrada=dados["valor_entrada"],
            margem_lucro=dados["margem_lucro"],
            quantidade_disponivel=dados["quantidade"]
        )

        local_escolhido = locais[dados["indice_local"]]

        if local_escolhido.total_itens_armazenados + item.quantidade_disponivel > local_escolhido.capacidade:
            self.__tela_item.mostra_mensagem("Capacidade do local excedida. Item não cadastrado.")
            return

        if item.codigo in local_escolhido.itens:
            local_escolhido.itens[item.codigo] += item.quantidade_disponivel
        else:
            local_escolhido.itens[item.codigo] = item.quantidade_disponivel

        self.__controlador_local.atualiza()
        self.__item_dao.adiciona(item)
        
        self.__tela_item.mostra_mensagem("Item cadastrado com sucesso.")

    def editar_item(self):
        itens = self.__item_dao.lista()
        if not itens:
            self.__tela_item.mostra_mensagem("Nenhum item cadastrado.")
            return

        indice = self.__tela_item.seleciona_item(itens)
        if indice is not None and 0 <= indice < len(itens):
            item = itens[indice]
            novos_dados = self.__tela_item.pega_dados_item(self.__controlador_local.retorna_locais())
            if novos_dados:
                item.descricao = novos_dados["descricao"]
                item.valor_entrada = novos_dados["valor_entrada"]
                item.margem_lucro = novos_dados["margem_lucro"]
                item.quantidade_disponivel = novos_dados["quantidade"]
                self.__item_dao.atualiza()
                self.__tela_item.mostra_mensagem("Item editado com sucesso.")
        else:
            self.__tela_item.mostra_mensagem("Índice inválido.")

    def remover_item(self):
        itens = self.__item_dao.lista()
        if not itens:
            self.__tela_item.mostra_mensagem("Nenhum item cadastrado.")
            return

        indice = self.__tela_item.seleciona_item(itens)
        if indice is not None and 0 <= indice < len(itens):
            item = itens[indice]

            # Remove o item também de todos os locais de armazenamento
            for local in self.__controlador_local.retorna_locais():
                if item.codigo in local.itens:
                    del local.itens[item.codigo]
                    
            
            self.__controlador_local.atualiza()
            self.__item_dao.remove(item)
            self.__tela_item.mostra_mensagem("Item removido com sucesso.")
        else:
            self.__tela_item.mostra_mensagem("Índice inválido.")

    def listar_itens(self):
        itens = self.__item_dao.lista()
        self.__tela_item.mostra_itens(itens)

    def retorna_itens(self):
        return self.__item_dao.lista()

    def atualiza(self):
        self.__item_dao.atualiza()

    def busca_por_codigo(self, codigo: str):
        itens = self.__item_dao.lista()
        for item in itens:
            if item.codigo == codigo:
                return item
        return None
    
    def remover_item_por_codigo(self, codigo: str):
        item = self.busca_por_codigo(codigo)
        if item:
            for local in self.__controlador_local.retorna_locais():
                if item.codigo in local.itens:
                    del local.itens[item.codigo]
            self.__controlador_local.atualiza()
            self.__item_dao.remove(item)

