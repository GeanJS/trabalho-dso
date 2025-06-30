from views.tela_usuario import TelaUsuario
from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO

class ControladorUsuario:
    def __init__(self):
        self.__usuario_dao = UsuarioDAO()
        self.__usuario_logado = None
        
    def abre_menu(self):
        while True:
            tela_usuario = TelaUsuario()
            opcao = tela_usuario.menu_usuario()
            match opcao:
                case 1:
                    self.cadastrar_usuario()
                case 2:
                    self.remover_usuario()
                case 3:
                    self.listar_usuarios()
                case 0:
                    return
                case _:
                    tela_usuario.mostra_mensagem("Opção Inválida")
        
        
    def login(self):
        tela_usuario = TelaUsuario()
        dados = tela_usuario.pega_dados_usuario()
        if dados is None:
            return None
        
        usuario = self.__validar_login(dados["nome"], dados["senha"])
        if usuario:
            self.__usuario_logado = usuario
            return usuario
    
    def __validar_login(self, nome:str, senha:str):
        usuarios = self.__usuario_dao.lista()
        for usuario in usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return usuario
        return None
    
    def cadastrar_usuario(self):
        tela_usuario = TelaUsuario()
        dados = tela_usuario.pega_dados_cadastro_usuario()
        if dados is None:
            return
        
        usuario = Usuario(
            nome=dados["nome"],
            senha=dados["senha"],
            tipo=dados["tipo"]
        )
        self.__usuario_dao.adiciona(usuario)
        tela_usuario.mostra_mensagem("Usuário cadastrado com sucesso")
    
    
    def remover_usuario(self):
        tela_usuario = TelaUsuario()
        usuarios_disponiveis = self.__usuario_dao.lista()[1::]
        
        if not usuarios_disponiveis:
            tela_usuario.mostra_mensagem("Nenhum usuário disponivel para remoção")
        
        indice = tela_usuario.selecionar_usuario(usuarios_disponiveis)
        if indice is not None and 0 <= indice < len(usuarios_disponiveis):
            usuario = usuarios_disponiveis[indice]
            self.__usuario_dao.remove(usuario)
            tela_usuario.mostra_mensagem(f"Usuário {usuario.nome} removido com sucesso")
        else:
            tela_usuario.mostra_mensagem("Remoção cancelado ou indice inválido")
            
    def listar_usuarios(self):
        tela_usuario = TelaUsuario()
        usuarios = self.__usuario_dao.lista()
        tela_usuario.listar_usuarios(usuarios)
    
    def retorna_usuario_logado(self):
        return self.__usuario_logado