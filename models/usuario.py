class Usuario:
    def __init__(self, nome: str, senha: str, tipo: str):
        self.__nome = nome
        self.__senha = senha
        if tipo not in ('funcionario', 'administrador'):
            raise ValueError("Tipo invalido")
        else:
            self.__tipo = tipo
            
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome
        
    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
        
    @property
    def tipo(self):
        return self.__tipo