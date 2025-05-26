class Item:
    def __init__(self, codigo: str, descricao: str, local):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__local = local
        
    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, novo_local):
        self.__local = novo_local

    def retorna_dados(self) -> dict:
        return {
            "codigo": self.codigo,
            "descricao": self.descricao,
            "local": self.local
        }
