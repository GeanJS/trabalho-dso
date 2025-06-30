from datetime import datetime
from models.realocacao import Realocacao
from dao.realocacao_dao import RealocacaoDAO
from views.tela_realocacao import TelaRealocacao

class ControladorRealocacao:
    def __init__(self, controlador_item, controlador_local, controlador_usuario):
        self.__tela_realocacao = TelaRealocacao()
        self.__controlador_item = controlador_item
        self.__controlador_local = controlador_local
        self.__controlador_usuario = controlador_usuario
        self.__realocacao_dao = RealocacaoDAO(self.__controlador_item, self.__controlador_local, self.__controlador_usuario)

    def abre_menu(self):
        while True:
            opcao = self.__tela_realocacao.menu_realocacao()
            match opcao:
                case 1:
                    self.realizar_realocacao()
                case 2:
                    self.listar_realocacoes()
                case 0:
                    return
                case _:
                    self.__tela_realocacao.mostra_mensagem("Opção inválida")
    
    def realizar_realocacao(self):
        locais =self.__controlador_local.retorna_locais()
        itens = self.__controlador_item.retorna_itens()
        funcionario = self.__controlador_usuario.retorna_usuario_logado()
        
        if not itens or len(locais) < 2:
            self.__tela_realocacao.mostra_mensagem("É necessário ter ao menos um item e dois locais cadastrados.")
            return
        
        dados = self.__tela_realocacao.pega_dados_realocacao(locais, itens)
        if dados is None:
            return
        
        item_desejado = self.__controlador_item.busca_por_codigo(dados["codigo_item"])
        local_origem = locais[dados["indice_origem"]]
        if item_desejado is None:
            self.__tela_realocacao.mostra_mensagem("Item não encontrado no sistema.")
            return
            
        if item_desejado is None:
            self.__tela_realocacao.mostra_mensagem("Item não encontrado no local de origem.")
            return
            
        local_destino = locais[dados["indice_destino"]]
        quantidade = dados["quantidade"]
        
        if local_origem == local_destino:
            self.__tela_realocacao.mostra_mensagem("O local de origem e destino não podem ser o mesmo.")
            return

        codigo_str = str(item_desejado.codigo)
        if codigo_str not in local_origem.itens or local_origem.itens[codigo_str] < quantidade:
            self.__tela_realocacao.mostra_mensagem("Quantidade insuficiente no local de origem.")
            return

        if local_destino.total_itens_armazenados + quantidade > local_destino.capacidade:
            self.__tela_realocacao.mostra_mensagem("Local de destino não tem capacidade suficiente.")
            return
        
        local_origem.itens[codigo_str] -= quantidade
        if local_origem.itens[codigo_str] == 0:
            del local_origem.itens[codigo_str]
            
        if codigo_str in local_destino.itens:
            local_destino.itens[codigo_str] += quantidade
        else:
            local_destino.itens[codigo_str] = quantidade
            
        self.__controlador_local.atualiza()
            
        realocacao = Realocacao(
            data=datetime.now(),
            quantidade=quantidade,
            item=item_desejado,
            funcionario=funcionario,
            local_origem=local_origem,
            local_destino=local_destino
        )
        
        self.__realocacao_dao.adiciona(realocacao)
        self.__tela_realocacao.mostra_mensagem("Realocação realizada com sucesso")
        
    def listar_realocacoes(self):
        realocacoes = self.__realocacao_dao.lista()
        self.__tela_realocacao.mostra_realocacoes(realocacoes)