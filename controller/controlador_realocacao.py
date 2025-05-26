from datetime import datetime
from models.realocacao import Realocacao
from models.item import Item
from view.tela_realocacao import TelaRealocacao

class ControladorRealocacao:
    def __init__(self, controlador_sistema):
        self.__realocacoes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_realocacao = TelaRealocacao()

    def abre_menu(self):
        while True:
            opcao = self.__tela_realocacao.menu_realocacao()
            match opcao:
                case 1:
                    self.realizar_realocacao()
                case 2:
                    self.listar_realocacoes()
                case 0:
                    self.retorna()
                case _:
                    print("Opção inválida!")
    
    
    def realizar_realocacao(self):
        try:
            dados = self.__tela_realocacao.pega_dados_realocacao()
            item = self.__controlador_sistema.controlador_item.buscar_item_por_codigo(dados["codigo_item"])
            if not item:
                raise ValueError("Item nao encontrado")
            
            local_origem = self.__controlador_sistema.controlador_local_armazenamento.buscar_local_por_nome([dados["local_origem"]])
            local_destino = self.__controlador_sistema.controlador_local_armazenamento.buscar_local_por_nome([dados["local_destino"]])
            
            if not local_origem:
                raise ValueError("Local de origem nao encontrado!")
            if not local_destino:
                raise ValueError("Local de destino nao encontrado!")
            
            if local_origem.itens.get(item, 0) < dados["quantidade"]:
                raise ValueError(f"Quantidade insuficiente no local {local_origem.nome}")
            
        except KeyboardInterrupt:
            return None
        except Exception as e:
            print(f"\nOcorreu um erro inesperado {e}")
            
    def listar_realocacoes(self):
        dados = []
        for realocacao in self.__realocacoes:
            dados_da_realocacao = realocacao.retorna_dados()
            dados.append(dados_da_realocacao)
        self.__tela_realocacao.mostra_realocacoes(dados)
    
    def retorna(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()