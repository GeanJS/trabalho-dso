import json
from datetime import datetime
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self, caminho_arquivo="clientes.json"):
        self.__caminho = caminho_arquivo
        self.__clientes = self.__carregar()
        
        
    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                clientes = []
                for dado in dados:
                    cliente = Cliente(
                        nome=dado["nome"],
                        telefone=dado["telefone"],
                        email=dado["email"],
                        endereco=dado["endereco"],
                        cpf=dado["cpf"],
                        registrador=dado["registrador"],
                        data_cadastro=datetime.strptime(dado["data_cadastro"], "%Y-%m-%d %H:%M")
                    )
                    clientes.append(cliente)
                return clientes
        except FileNotFoundError:
            return []
        
    def __salvar(self):
        dados_serializado = []
        for cliente in self.__clientes:
            dados = cliente.retorna_dados()
            dados["data_cadastro"] = cliente.data_cadastro.strftime("%Y-%m-%d %H:%M")
            dados_serializado.append(dados)
            
        with open(self.__caminho, "w", encoding='utf-8') as arquivo:
            json.dump(dados_serializado, arquivo, indent=4, ensure_ascii=False)
            
            
    def adiciona(self, cliente: Cliente):
        self.__clientes.append(cliente)
        self.__salvar()
        
        
    def remove(self, cliente: Cliente):
        self.__clientes.remove(cliente)
        self.__salvar()
        
    def atualiza(self):
        self.__salvar()
        
    def lista(self):
        return self.__clientes
