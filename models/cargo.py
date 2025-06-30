class Cargo:
    def __init__(self, funcao: str, salario: float):
        self.__funcao = funcao
        self.__salario = salario
        
    @property
    def funcao(self) -> str:
        return self.__funcao
    
    @funcao.setter
    def funcao(self, nova_funcao: str):
        if isinstance(nova_funcao, str):
            self.__funcao = nova_funcao
    
    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario: float):
        if isinstance(novo_salario, float):
            self.__salario = novo_salario
        