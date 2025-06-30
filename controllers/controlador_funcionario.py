from views.tela_funcionario import TelaFuncionario
from models.funcionario import Funcionario
from dao.funcionario_dao import FuncionarioDAO
from models.cargo import Cargo
from datetime import datetime

class ControladorFuncionario:
    def __init__(self, controlador_usuario):
        self.__tela_funcionario = TelaFuncionario()
        self.__funcionario_dao = FuncionarioDAO()
        self.__controlador_usuario = controlador_usuario
    
    
    def abre_menu(self):
        while True:
            opcao = self.__tela_funcionario.menu_funcionario()
            match opcao:
                case 1:
                    self.cadastrar_funcionario()
                case 2:
                    self.editar_funcionario()
                case 3:
                    self.remover_funcionario()
                case 4:
                    self.listar_funcionarios()
                case 0:
                    return
                case _:
                    self.__tela_funcionario.mostra_mensagem("Opção inválida")
                    
                    
    def cadastrar_funcionario(self):
        dados = self.__tela_funcionario.pega_dados_funcionario()
        registrador = self.__controlador_usuario.retorna_usuario_logado().nome
        if dados is None:
            self.__tela_funcionario.mostra_mensagem("")
            return
        
        funcionario = Funcionario(
            nome=dados["nome"],
            telefone=dados["telefone"],
            endereco=dados["endereco"],
            email=dados["email"],
            cpf=dados["cpf"],
            cargo=Cargo(dados["funcao"], float(dados["salario"])),
            registrador=registrador,
            data_cadastro=datetime.now()
        )
        
        self.__funcionario_dao.adiciona(funcionario)
        self.__tela_funcionario.mostra_mensagem("Funcionário cadastrado com sucesso")
    
    def editar_funcionario(self):
        funcionarios = self.__funcionario_dao.lista()
        if not funcionarios:
            self.__tela_funcionario.mostra_mensagem("\nNenhum funcionario cadastrado\n")
            return
            
        indice = self.__tela_funcionario.seleciona_funcionario(funcionarios)
        
        if indice is not None and 0 <= indice < len(funcionarios):
            funcionario = funcionarios[indice]
            dados_atuais = funcionario.retorna_dados()
            
            novos_dados = self.__tela_funcionario.pega_dados_funcionario(dados_atuais)
            
            if novos_dados is None:
                self.__tela_funcionario.mostra_mensagem("Edição Cancelada\n")
                return
            
            funcionario.nome = novos_dados["nome"]
            funcionario.telefone = novos_dados["telefone"]
            funcionario.endereco = novos_dados["endereco"]
            funcionario.email = novos_dados["email"]
            funcionario.cpf = novos_dados["cpf"]
            funcionario.cargo = Cargo(novos_dados["funcao"], float(novos_dados["salario"]))
            
            self.__funcionario_dao.atualiza()
            self.__tela_funcionario.mostra_mensagem("funcionario editado com sucesso")
        else:
            self.__tela_funcionario.mostra_mensagem("Índice inválido")
    
    def remover_funcionario(self):
        funcionarios = self.__funcionario_dao.lista()
        if not funcionarios:
            self.__tela_funcionario.mostra_mensagem("\nNenhum funcionarios encontrado")
            return
        
        indice = self.__tela_funcionario.seleciona_funcionario(funcionarios)
        
        if indice is not None and 0 <= indice < len(funcionarios):
            funcionario = funcionarios[indice]
            self.__funcionario_dao.remove(funcionario)
            self.__tela_funcionario.mostra_mensagem("funcionarios removido com sucesso!!")
            
    
    def listar_funcionarios(self):
        funcionarios = self.__funcionario_dao.lista()
        self.__tela_funcionario.mostra_funcionários(funcionarios)
    
    def retorna_funcionarios(self):
        return self.__funcionario_dao.lista()
        
    def busca_por_nome(self, nome: str):
        funcionarios = self.__funcionario_dao.lista()
        for funcionario in funcionarios:
            if funcionario.nome == nome:
                return funcionario
        return None