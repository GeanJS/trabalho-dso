import json
from models.local_armazenamento import LocalArmazenamento

class LocalArmazenamentoDAO:
    def __init__(self, caminho_arquivo="locais_armazenados.json"):
        self.__caminho = caminho_arquivo
        self.__locais = self.__carregar()
        
    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                locais = []
                for dado in dados:
                    local = LocalArmazenamento(
                        nome=dado["nome"],
                        capacidade=dado["capacidade"]
                    )
                    local.itens = dado.get("itens", {})
                    locais.append(local)
                return locais
        except FileNotFoundError:
            return []
        
    def __salvar(self):
        dados_serializados = []
        for local in self.__locais:
            dados = local.retorna_dados()
            dados_serializados.append(dados)
        with open(self.__caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)

    def adiciona(self, local: LocalArmazenamento):
        self.__locais.append(local)
        self.__salvar()

    def remove(self, local: LocalArmazenamento):
        self.__locais.remove(local)
        self.__salvar()

    def atualiza(self):
        self.__salvar()

    def lista(self):
        return self.__locais