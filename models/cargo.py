class Cargo:
    def __init__(self, funcao: str, salario: float):
        self.__funcao = funcao
        self.__salario = salario
        
    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao: str):
        self.__funcao = funcao
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario