from models.venda import Venda
from view.tela_venda import TelaVenda
from datetime import datetime

class ControladorVenda:
    def __init__(self, controlador_sistema):
        self.__vendas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()

    def abre_menu(self):
        pass
    
    def realizar_venda(self):
        try:
            dados = self.__tela_venda.pega_dados_venda()
            if dados is None:
                self.__tela_venda.mostra_mensagem("Venda cancelada")
                return

            item = self.__controlador_sistema.controlador_itens.buscar_item_por_codigo(dados["codigo_item"])
            cliente = self.__controlador_sistema.controlador_itens.buscar_item_por_codigo(dados["cpf_cliente"])
            funcionario = self.__controlador_sistema.usuario_logado
            
            if not item:
                self.__tela_venda.mostra_mensagem("Item não encontrado!")
                return
                
            if not cliente:
                self.__tela_venda.mostra_mensagem("Cliente não cadastrado!")
                return

            if item.quantidade_disponivel < dados["quantidade"]:
                self.__tela_venda.mostra_mensagem("Estoque insuficiente!")
                return

            item.quantidade_disponivel -= dados["quantidade"]
            
            nova_venda = Venda(
                data=datetime.now(),
                quantidade=dados["quantidade"],
                item=item,
                funcionario=funcionario,
                cliente=cliente
            )
            self.__vendas.append(nova_venda)
            self.__tela_venda.mostra_venda_concluida(nova_venda)
        except KeyboardInterrupt:
            print("\nVenda cancelada")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado {e} ")

    def retonar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()