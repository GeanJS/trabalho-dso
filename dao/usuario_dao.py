from models.usuario import Usuario
import json

class UsuarioDAO:
    def __init__(self, caminho_arquivo ="usuarios.json") -> None:
        self.__caminho = caminho_arquivo
        self.__usuarios = self.__carregar()
        
        
    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                usuarios = []
                for dado in dados:
                    usuario = Usuario(
                        nome=dado["nome"],
                        senha=dado["senha"],
                        tipo=dado["tipo"]
                    )
                    usuarios.append(usuario)
                
                if not usuarios:
                    usuarios.append(Usuario("admin", "admin", "administrador"))
                    
                return usuarios
        except FileNotFoundError:
            usuarios = [Usuario("admin", "admin", "administrador")]
            self.__usuarios = usuarios
            self.__salvar()
            return usuarios
        
        
    def __salvar(self):
        dados_serializados = []
        for usuario in self.__usuarios:
            dados = usuario.retorna_dados()
            dados_serializados.append(dados)
            
            
        with open(self.__caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)
            
            
    def adiciona(self, usuario: Usuario):
        self.__usuarios.append(usuario)
        self.__salvar()
        
        
    def remove(self, usuario: Usuario):
        self.__usuarios.remove(usuario)
        self.__salvar()
        
    def atualiza(self):
        self.__salvar()
        
    def lista(self):
        return self.__usuarios