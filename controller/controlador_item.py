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
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")

    def cadastrar_item(self):
        dados = self.__tela_itens.pega_dados_itens()
        item = Item(dados["nome"], dados["descricao"], dados["valor_entrada"], dados["margem_lucro"], dados["quantidade_disponivel"])
        self.__itens.append(item)
        self.__tela_itens.mostra_mensagem("Item cadastrado com sucesso!!")

    def listar_itens(self):
        self.__tela_itens.mostra_itens(self.__itens)

    def retornar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()