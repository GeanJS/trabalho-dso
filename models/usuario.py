class Usuario:
    def __init__(self, nome: str, senha: str, tipo: str):
        self.__nome = nome
        self.__senha = senha
        self.__tipo = tipo
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome

    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self, novo_senha: str):
        if isinstance(novo_senha, str):
            self.__senha = novo_senha
            
    @property
    def tipo(self) -> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, novo_tipo: str):
        if novo_tipo in ("funcionario", "administrador"):
            self.__tipo = novo_tipo
            
    def retorna_dados(self):
        return {
            "nome": self.__nome,
            "senha": self.__senha,
            "tipo": self.__tipo
        }