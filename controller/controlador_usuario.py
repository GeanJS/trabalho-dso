from models.usuario import Usuario
from view.tela_usuario import TelaUsuario
from utils.validacao import confirma_acao

class ControladorUsuario:
    def __init__(self, controlador_sistema_administrador, lista_usuarios: list):
        self.__usuarios = lista_usuarios
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema_administrador = controlador_sistema_administrador
        
    def iniciar(self):
        while True:
            dados = self.__tela_usuario.pegar_dados_usuario()
            if dados is None:
                self.__tela_usuario.mostrar_mensagem("Login cancelado")
                return
                
            usuario = self.__validar_login(dados["nome"], dados["senha"])
            if usuario:
                self.__tela_usuario.mostrar_mensagem(f"\nLogin Bem-Sucedido! Bem-vindo, {usuario.nome}.")
                return usuario
            else:
                self.__tela_usuario.mostrar_mensagem("Nome ou senha incorretos. Tente novamente.")
                
    def __validar_login(self, nome, senha):
        for usuario in self.__usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return usuario
        return None
    
    def abre_menu(self):
        while True:
            opcao = self.__tela_usuario.menu_usuario()
            match opcao:
                case 1:
                    self.cadastrar_usuario()
                case 2:
                    self.excluir_usuario()
                case 3:
                    self.listar_usuarios()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                
                case _:
                    self.__tela_usuario.mostrar_mensagem("Opcao invalida.")
                    
    def cadastrar_usuario(self):
        dados = self.__tela_usuario.pegar_dados_cadastro_usuario()
        if dados is None:
            self.__tela_usuario.mostrar_mensagem("Cadastro cancelado")
            return
        try:
            for usuario in self.__usuarios:
                if usuario.nome == dados["nome"]:
                    self.__tela_usuario.mostrar_mensagem("Usuario ja existe")
                    return
                
            novo_usuario = Usuario(dados["nome"], dados["senha"], dados["tipo"])
            self.__usuarios.append(novo_usuario)
            self.__tela_usuario.mostrar_mensagem("Usuario cadastrado com sucesso.")
            
        except ValueError as e:
            self.__tela_usuario.mostrar_mensagem(f"Erro: {str(e)}")
            
    def excluir_usuario(self):
        usuarios_excluiveis = []
        for usuario in self.__usuarios:
            if usuario.nome != "admin":
                usuarios_excluiveis.append(usuario)
                
        if not usuarios_excluiveis:
            self.__tela_usuario.mostrar_mensagem("Nao tem usuarios disponiveis para exclusao")
            return
        
        indice = self.__tela_usuario.selecionar_usuario(usuarios_excluiveis)
        if 0 <= indice < len(usuarios_excluiveis):
            usuario_selecionado = usuarios_excluiveis[indice]
            try:
                if confirma_acao(f"Tem certeza que deseja excluir o usuario {usuario_selecionado.nome}?"):
                    self.__usuarios.remove(usuario_selecionado)
                    self.__tela_usuario.mostrar_mensagem(f"Usuario {usuario_selecionado.nome} removido!")
                else:
                    self.__tela_usuario.mostrar_mensagem("Exclusao cancelada")
            except KeyboardInterrupt:
                print("\nExclusao interrompida")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
            
    def listar_usuarios(self):
        self.__tela_usuario.listar_usuarios(self.__usuarios)

    def retornar(self):
        self.__controlador_sistema_administrador.inicializa_sistema_administrador()