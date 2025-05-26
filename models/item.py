from datetime import datetime

class Item:
    def __init__(self, codigo: str, descricao: str, valor_entrada: float, margem_lucro: float, data_cadastro: datetime, quantidade_disponivel: int):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor_entrada = valor_entrada
        self.__margem_lucro = margem_lucro
        self.__data_cadastro = data_cadastro
        self.__quantidade_disponivel = quantidade_disponivel
        
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
    def valor_entrada(self):
        return self.__valor_entrada
    
    @valor_entrada.setter
    def valor_entrada(self, novo_valor: float):
        if novo_valor < 0:
            raise ValueError("Valor nao pode ser negativo!")
        self.__valor_entrada = novo_valor
        
    @property
    def margem_lucro(self):
        return self.__margem_lucro
    
    @margem_lucro.setter
    def margem_lucro(self, nova_margem: float):
        if nova_margem < 0:
            raise ValueError("A margem de lucro deve ser positiva")
        self.__margem_lucro = nova_margem
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro
    
    @property
    def quantidade_disponivel(self):
        return self.__quantidade_disponivel

    @quantidade_disponivel.setter
    def quantidade_disponivel(self, valor: int):
        if valor < 0:
            raise ValueError("Quantidade não pode ser negativa")
        self.__quantidade_disponivel = valor
    
    def valor_esperado_venda(self):
        return self.__valor_entrada * (1 + self.__margem_lucro / 100) 
    
    def retorna_dados(self) -> dict:
        return {
            "codigo": self.codigo,
            "descricao": self.descricao,
            "valor_entrada": self.valor_entrada,
            "margem_lucro": self.margem_lucro,
            "valor_esperado_venda": self.valor_esperado_venda(),
            "data_cadastro": self.data_cadastro,
            "quantidade_disponivel": self.quantidade_disponivel
        }
