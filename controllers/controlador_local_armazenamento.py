from views.tela_local_armazenamento import TelaLocalArmazenamento
from models.local_armazenamento import LocalArmazenamento
from dao.local_armazenamento_dao import LocalArmazenamentoDAO

class ControladorLocalArmazenamento:
    def __init__(self):
        self.__tela_local = TelaLocalArmazenamento()
        self.__local_dao = LocalArmazenamentoDAO()
        
    def abre_menu(self):
        while True:
            opcao = self.__tela_local.menu_local()
            match opcao:
                case 1:
                    self.cadastrar_local()
                case 2:
                    self.editar_local()
                case 3:
                    self.remover_local()
                case 4:
                    self.listar_locais()
                case 0:
                    break
                case _:
                    self.__tela_local.mostra_mensagem("Opção inválida!")
                    
    def cadastrar_local(self):
        dados = self.__tela_local.pega_dados_local()
        if dados is None:
            self.__tela_local.mostra_mensagem("Cadastro Cancelado")
            return
        
        novo_local = LocalArmazenamento(
            nome=dados["nome"],
            capacidade=dados["capacidade"]
        )
        self.__local_dao.adiciona(novo_local)
        self.__tela_local.mostra_mensagem("Local cadastrado com sucesso!") 
        
        
    def editar_local(self):
        locais = self.__local_dao.lista()
        if not locais:
            self.__tela_local.mostra_mensagem("Nenhum local cadastrado.")
            return
        
        indice = self.__tela_local.seleciona_local(locais)
        if indice is not None and 0 <= indice < len(locais):
            local = locais[indice]
            dados_atuais = local.retorna_dados()
            
            novos_dados = self.__tela_local.pega_dados_local(dados_atuais)
            if novos_dados is None:
                self.__tela_local.mostra_mensagem("Edição cancelada")
                return
            
            local.nome = novos_dados["nome"]
            local._LocalArmazenamento__capacidade = novos_dados["capacidade"]  # setter opcional
            self.__local_dao.atualiza()
            self.__tela_local.mostra_mensagem("Local editado com sucesso.")
        else:
            self.__tela_local.mostra_mensagem("Índice inválido.")
            
            
    def remover_local(self):
        locais = self.__local_dao.lista()
        if not locais:
            self.__tela_local.mostra_mensagem("Nenhum local cadastrado.")
            return
        
        indice = self.__tela_local.seleciona_local(locais)
        if indice is not None and 0 <= indice < len(locais):
            local = locais[indice]
            if local.total_itens_armazenados > 0:
                self.__tela_local.mostra_mensagem("Não é possível remover um local com itens armazenados.")
                return
            self.__local_dao.remove(local)
            self.__tela_local.mostra_mensagem("Local removido com sucesso.")
        else:
            self.__tela_local.mostra_mensagem("Índice inválido.")
            
    
    def listar_locais(self):
        locais = self.__local_dao.lista()
        self.__tela_local.mostra_locais(locais)
        
    def retorna_locais(self):
        return self.__local_dao.objetos_internos()
    
    def atualiza(self):
        self.__local_dao.atualiza()
    
    def busca_por_nome(self, nome):
        locais = self.__local_dao.lista()
        for local in locais:
            if local.nome == nome:
                return local
        return None