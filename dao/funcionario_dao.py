import json
from datetime import datetime
from models.funcionario import Funcionario
from models.cargo import Cargo

class FuncionarioDAO:
    def __init__(self, caminho_arquivo="funcionarios.json"):
        self.__caminho = caminho_arquivo
        self.__funcionarios = self.__carregar()
        
    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                funcionarios = []
                for dado in dados:
                    funcionario = Funcionario(
                        nome=dado["nome"],
                        telefone=dado["telefone"],
                        email=dado["email"],
                        endereco=dado["endereco"],
                        cpf=dado["cpf"],
                        cargo=Cargo(dado["funcao"], dado["salario"]),
                        registrador=dado["registrador"],
                        data_cadastro=datetime.strptime(dado["data_cadastro"], "%Y-%m-%d %H:%M")
                    )
                    funcionarios.append(funcionario)
                return funcionarios
        except FileNotFoundError:
            return []
        
    def __salvar(self):
        dados_serializados = []
        for funcionario in self.__funcionarios:
            dados = funcionario.retorna_dados()
            dados["data_cadastro"] = funcionario.data_cadastro.strftime("%Y-%m-%d %H:%M")
            dados_serializados.append(dados)
            
        with open(self.__caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)
            
    def adiciona(self, funcionario: Funcionario):
        self.__funcionarios.append(funcionario)
        self.__salvar()
        
        
    def remove(self, funcionario: Funcionario):
        self.__funcionarios.remove(funcionario)
        self.__salvar()
        
    def atualiza(self):
        self.__salvar()
        
    def lista(self):
        return self.__funcionarios
    
