from models.item import Item
from view.tela_itens import TelaItens

class ControladorItem:
    def __init__(self, controlador_sistema):
        self.__itens = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_itens = TelaItens()
    
    def abre_menu(self):
        while True:
            opcao = self.__tela_itens.menu_itens()
            match opcao:
                case 1:
                    self.cadastrar_item()
                case 2:
                    self.listar_itens()
                case 3:
                    self.remover_item()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")

    def cadastrar_item(self):
        dados = self.__tela_itens.pega_dados_itens()
        item_existente = self.buscar_item_por_codigo_e_descricao(dados["codigo"], dados["descricao"])
        
        if item_existente:
            item_existente.quantidade += dados["quantidade"]
            self.__tela_itens.mostra_mensagem("Item já existente!, Para atualizar a quantidade, movimente pelo menu de armazenamento")
        else:
            novo_item = Item(
                dados["codigo"],
                dados["descricao"],
                dados["valor_entrada"],
                dados["margem_lucro"],
                dados["data_cadastro"],
                dados["quantidade_disponivel"]
            )
            self.__itens.append(novo_item)
            self.__tela_itens.mostra_mensagem("Item adicionado com sucesso!")

    def remover_item(self):
        pass


    def listar_itens(self):
        self.__tela_itens.mostra_itens(self.__itens)

    def buscar_item_por_codigo(self, codigo: str):
        for item in self.__itens:
            if item.codigo == codigo:
                return item
        return None
    
    def buscar_item_por_codigo_e_descricao(self, codigo:str, descricao: str):
        for item in self.__itens:
            if item.codigo == codigo and item.descricao == descricao:
                return item
        return None
        
    def retornar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()