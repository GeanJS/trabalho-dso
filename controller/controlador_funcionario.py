from models.funcionario import Funcionario
from models.cargo import Cargo
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
        usuario_logado = self.__controlador_sistema.usuario_logado
        
        cargo = Cargo(funcao=dados["funcao"], salario=dados["salario"])
        
        funcionario = Funcionario(
            nome=dados["nome"],
            telefone=dados["telefone"],
            endereco=dados["endereco"],
            email=dados["email"],
            cpf=dados["cpf"],
            registrador=usuario_logado.nome,
            cargo=cargo,
            data_cadastro=dados["data_cadastro"]
            )
           
        self.__funcionarios.append(funcionario)
        self.__tela_funcionario.mostra_mensagem("Funcionario cadastrado com sucesso!!")
    
    def listar_funcionarios(self):
        self.__tela_funcionario.mostra_funcionarios(self.__funcionarios)
                
    def retornar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()