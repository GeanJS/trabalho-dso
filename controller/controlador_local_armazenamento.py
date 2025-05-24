from models.local_armazenamento import LocalArmazenamento
from view.tela_local_armazenamento import TelaLocalArmazenamento

class ControladorLocalArmazenamento:
    def __init__(self, controlador_sistema):
        self.__locais_armazenamento = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_local_armazenamento = TelaLocalArmazenamento()

    def abre_menu(self):
        while True:
            opcao = self.__tela_local_armazenamento.menu_local_armazenamento()
            match opcao:
                case 1:
                    self.cadastrar_local_armazenamento()
                case 2:
                    self.listar_local_armazenamento()
                case 0:
                    self.retornar()
                case _:
                    print("Selecione uma opção entre 1, 2 ou retorne com 0!")

    def cadastrar_local_armazenamento(self):
        dados = self.__tela_local_armazenamento.pega_dados_local_armazenamento()
        local_armazenamento = LocalArmazenamento(dados["nome"], dados["descricao"], dados["capacidade"])
        self.__locais_armazenamento.append(local_armazenamento)
        self.__tela_local_armazenamento.mostra_mensagem("Novo local cadastrado com sucesso!")

    def listar_local_armazenamento(self):
        self.__tela_local_armazenamento.mostra_locais_armazenamento(self.__locais_armazenamento)

    def retornar(self):
        self.__controlador_sistema.inicializad_sistema()