from models.item import Item
from view.tela_itens import TelaItens
from utils.validacao import confirma_acao

class ControladorItem:
    def __init__(self, controlador_sistema, itens: list):
        self.__itens = itens
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
        if dados is None:
            self.__tela_itens.mostra_mensagem("Cadastro Cancelado")
            return
        item_existente = self.buscar_item_por_codigo_e_descricao(dados["codigo"], dados["descricao"])
        
        if item_existente:
            item_existente.quantidade += dados["quantidade"]
            self.__tela_itens.mostra_mensagem("Item já existente!, Para atualizar a quantidade, movimente pelo menu de armazenamento")
        else:
            novo_item = Item(
                dados["codigo"],
                dados["descricao"],
                dados["local"],
            )
            self.__itens.append(novo_item)
            self.__tela_itens.mostra_mensagem("Item adicionado com sucesso!")

    def remover_item(self):
        if not self.__itens:
            self.__tela_itens.mostra_mensagem("Nenhum cliente cadastrado para remover")
            return

        indice = self.__tela_itens.seleciona_item(self.__itens)
        
        if 0<= indice < len(self.__itens):
            item = self.__itens[indice]
            
            try:
                if confirma_acao(f"Tem certeza que deseja remover o cliente {item.descricao}?"):
                    self.__itens.pop(indice)
                    self.__tela_itens.mostra_mensagem(f"Item {item.descricao} removido com sucesso")
                else:
                    self.__tela_itens.mostra_mensagem("Remocao cancelada")
                    
            except KeyboardInterrupt:
                print("\nEdicao Interrompida\n")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                
        else:
            self.__tela_itens.mostra_mensagem("Indice invalido")

    def editar_item(self):
        if not self.__itens:
            self.__tela_itens.mostra_mensagem("Nenhum cliente cadastrado para editar")
            return
        
        indice = self.__tela_itens.seleciona_item(self.__itens)
        
        if 0 <= indice < len(self.__itens):
            item = self.__itens[indice]
            novos_dados = self.__tela_itens.pega_dados_itens()
            if novos_dados is None:
                self.__tela_itens.mostra_mensagem("Edicao cancelada")
                return
            try:
                if confirma_acao(f"Tem certeza que deseja editar o item {item.descricao}?"):
                    item.codigo = novos_dados["codigo"]
                    item.descricao = novos_dados["descricao"]
                    item.local = novos_dados["local"]
                    
                    self.__tela_itens.mostra_mensagem("Cliente editado com sucesso")
                    
            except KeyboardInterrupt:
                print("\nEdicao Interrompida\n")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")   
                
        else:
            self.__tela_itens.mostra_mensagem("Indice invalido")

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