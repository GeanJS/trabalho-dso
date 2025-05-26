from models.funcionario import Funcionario
from models.cargo import Cargo
from view.tela_funcionario import TelaFuncionario
from utils.validacao import confirma_acao

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
                case 3:
                    self.editar_funcionario()
                case 4:
                    self.remover_funcionario()
                case 0:
                    print("\nRetornando ao menu principal!!\n")
                    self.retornar()
                case _:
                    print("Opcao Invalida")
    
    
    def cadastrar_funcionario(self):
        dados = self.__tela_funcionario.pega_dados_funcionario()
        usuario_logado = self.__controlador_sistema.usuario_logado
        if dados is None:
            self.__tela_funcionario.mostra_mensagem("Cadastro cancelado")
            return
        
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

    def editar_funcionario(self):
        if not self.__funcionarios:
            self.__tela_funcionario.mostra_mensagem("Nenhum cliente cadastrado para editar")
            return
        
        indice = self.__tela_funcionario.seleciona_funcionario(self.__funcionarios)
        
        if 0 <= indice < len(self.__funcionarios):
            funcionario = self.__funcionarios[indice]
            novos_dados = self.__tela_funcionario.pega_dados_funcionario()
            
            if novos_dados is None:
                self.__tela_funcionario.mostra_mensagem("Edicao cancelada")
                return
            
            try:
                if confirma_acao(f"Tem certeza que deseja editar o funcionario {funcionario.nome}"):
                    funcionario.nome = novos_dados["nome"]
                    funcionario.telefone = novos_dados["telefone"]
                    funcionario.endereco = novos_dados["endereco"]
                    funcionario.email = novos_dados["email"]
                    funcionario.cpf = novos_dados["cpf"]
                    
                    self.__tela_funcionario.mostra_mensagem("Cliente editado com sucesso")
                else:
                    self.__tela_funcionario.mostra_mensagem(f"A Edicao dos dados do funcionario {funcionario.nome} foi cancelada")
                    
            except KeyboardInterrupt:
                print("\nEdicao Interrompida\n")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                
        else:
            self.__tela_funcionario.mostra_mensagem("Indice invalido")

    def remover_funcionario(self):
        if not self.__funcionarios:
            self.__tela_funcionario.mostra_mensagem("Nenhum funcionario cadastrado")
            
        indice = self.__tela_funcionario.seleciona_funcionario(self.__funcionarios)
        
        if 0 <= indice < len(self.__funcionarios):
            funcionario = self.__funcionarios[indice]
            try:
                if confirma_acao(f"Tem certeza que deseja remover o funcionario {funcionario.nome}?"):
                    self.__funcionarios.pop(indice)
                    self.__tela_funcionario.mostra_mensagem(f"Funcionario {funcionario.nome} removido com sucesso")
                else:
                    self.__tela_funcionario.mostra_mensagem(f"Remocao do funcionario {funcionario.nome} cancelada")
            except KeyboardInterrupt:
                print("\nRemocao Interrompida\n")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
        else:
            self.__tela_funcionario.mostra_mensagem("Indice invalido")


    def retornar(self):
        usuario_logado = self.__controlador_sistema.usuario_logado
        if usuario_logado.tipo == 'administrador':
            self.__controlador_sistema.inicializa_sistema_administrador()
        else:
            self.__controlador_sistema.inicializa_sistema_funcionario()