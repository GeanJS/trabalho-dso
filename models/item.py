class Item:
    def __init__(self, nome: str, descricao: str, valor_entrada: float, margem_lucro: float, quantidade_disponivel: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor_entrada = valor_entrada
        self.__margem_lucro = margem_lucro
        self.__quantidade_disponivel = quantidade_disponivel
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        
    @property
    def valor_entrada(self):
        return self.__valor_entrada
    
    @valor_entrada.setter
    def valor_entrada(self, valor_entrada: float):
        if valor_entrada < 0:
            raise ValueError("Valor nao pode ser negativo!")
        self.__valor_entrada = valor_entrada
        
    
    @property
    def margem_lucro(self):
        return self.__margem_lucro
    
    @margem_lucro.setter
    def margem_lucro(self, margem_lucro: float):
        self.__margem_lucro = margem_lucro
        
    @property
    def quantidade_disponivel(self):
        return self.__quantidade_disponivel
    
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade_disponivel: int):
        if quantidade_disponivel < 0:
            raise ValueError("Quantidade disponivel nao pode ser negativa!")
        
        self.__quantidade_disponivel = quantidade_disponivel
        
    def valor_esperado_venda(self):
        return self.__valor_entrada * (1 + self.__margem_lucro / 100) 