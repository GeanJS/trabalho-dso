from models.funcionario import Funcionario
from view.tela_funcionario import TelaFuncionario

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_funcionario = TelaFuncionario()
    
    def abre_menu(self):
        while True:
            opcao = self.__tela_funcionario.menu_funcionario()
            match opcao:
                case 1:
                    self.cadastrar_funcionario()
                case 2:
                    self.listar_funcionarios()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")
    
    
    def cadastrar_funcionario(self):
        dados = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = Funcionario(dados["nome"], dados["telefone"], dados["endereco"], dados["email"], dados["cpf"],dados ["funcao"], dados["salario"], dados["data_contratacao"])
        self.__funcionarios.append(funcionario)
        self.__tela_funcionario.mostra_mensagem("Funcionario cadastrado com sucesso!!")
    
    def listar_funcionarios(self):
        self.__tela_funcionario.mostra_funcionarios(self.__funcionarios)
                
    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()