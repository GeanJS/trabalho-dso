from models.item import Item

class LocalArmazenamento:
    def __init__(self, nome: str, descricao: str, capacidade: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__capacidade = capacidade
        self.__itens = {}
        
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def itens(self):
        return self.__itens
    
    def adiciona_item(self, item: Item, quantidade: int) -> bool:
        if quantidade <= 0:
            raise ValueError("quantidade deve ser um positivo maior que 0")
        
        if not isinstance(item, Item):
            raise ValueError("item deve ser instancia da classe Item")
        
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade
            
        item.quantidade_disponivel += quantidade
        return True
        
    def remove_item(self, item: Item, quantidade: int) -> bool:
        if item not in self.__itens:
            raise ValueError("Item nao esta na cadastrado")
        
        if not isinstance(item, Item):
            raise ValueError("item deve ser instancia da classe Item")

        self.__itens[item] -= quantidade        
        item.quantidade_disponivel -= quantidade
        return True
        
        
    def retorna_itens(self) -> list:
        resultado = []
        for item, quantidade in self._itens.items():
            resultado.append((item.nome, quantidade))
        return resultado
