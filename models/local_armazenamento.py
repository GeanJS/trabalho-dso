class LocalArmazenamento:
    def __init__(self, nome: str, capacidade: int):
        self.__nome = nome
        self.__capacidade = capacidade
        self.__itens = {}
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
            
    @property
    def capacidade(self) -> int:
        return self.__capacidade
    
    @property
    def itens(self):
        return self.__itens
    
    @itens.setter
    def itens(self, novo_item):
        self.__itens = novo_item
    
    @property
    def total_itens_armazenados(self) -> int:
        return sum(self.__itens.values())
    
    def retorna_dados(self):
        return {
            "nome": self.__nome,
            "capacidade": self.__capacidade,
            "itens": self.__itens 
        }