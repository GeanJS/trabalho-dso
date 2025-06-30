class Item:
    def __init__(self, codigo: int, descricao: str, valor_entrada: float, margem_lucro: float, quantidade_disponivel: int):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor_entrada = valor_entrada
        self.__margem_lucro = margem_lucro
        self.__quantidade_disponivel = quantidade_disponivel

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        if isinstance(nova_descricao, str):
            self.__descricao = nova_descricao

    @property
    def valor_entrada(self) -> float:
        return self.__valor_entrada

    @valor_entrada.setter
    def valor_entrada(self, novo_valor: float):
        if isinstance(novo_valor, (float, int)):
            self.__valor_entrada = float(novo_valor)

    @property
    def margem_lucro(self) -> float:
        return self.__margem_lucro

    @margem_lucro.setter
    def margem_lucro(self, nova_margem: float):
        if isinstance(nova_margem, (float, int)):
            self.__margem_lucro = float(nova_margem)

    @property
    def quantidade_disponivel(self) -> int:
        return self.__quantidade_disponivel

    @quantidade_disponivel.setter
    def quantidade_disponivel(self, nova_quantidade: int):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade_disponivel = nova_quantidade

    def valor_esperado_da_venda(self) -> float:
        return self.__valor_entrada * (1 + self.__margem_lucro / 100)

    def retorna_dados(self) -> dict:
        return {
            "codigo": self.__codigo,
            "descricao": self.__descricao,
            "valor_entrada": self.__valor_entrada,
            "margem_lucro": self.__margem_lucro,
            "quantidade_disponivel": self.__quantidade_disponivel
        }

