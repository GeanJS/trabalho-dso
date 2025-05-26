from models.item import Item

class LocalArmazenamento:
    def __init__(self, nome: str, capacidade_maxima: int):
        self.__nome = nome
        self.__capacidade_maxima = capacidade_maxima
        self.__espaco_utilizado = 0
        self.__itens = {} 
        
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def capacidade(self):
        return self.__capacidade_maxima

    @property
    def itens(self):
        return self.__itens
    
    def adiciona_item(self, item: Item, quantidade: int):
        if self.__espaco_utilizado + quantidade > self.__capacidade_maxima:
            raise ValueError("Capacidade excedida")
        
        if not isinstance(item, Item):
            raise ValueError("item deve ser instancia da classe Item")
        
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade
        
        self.__espaco_utilizado += quantidade    
        item.quantidade_disponivel += quantidade
        
    def remove_item(self, item: Item, quantidade: int):
        if item not in self.__itens:
            raise ValueError("Item nao esta na cadastrado")
        
        if not isinstance(item, Item):
            raise ValueError("item deve ser instancia da classe Item")

        self.__espaco_utilizado -= quantidade
        item.quantidade_disponivel -= quantidade
        
    def retorna_itens(self) -> list:
        resultado = []
        for item, quantidade in self.__itens.items():
            resultado.append((item.nome, quantidade))
        return resultado
