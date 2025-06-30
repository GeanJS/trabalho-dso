import json
from models.item import Item

class ItemDAO:
    def __init__(self, caminho_arquivo="itens.json"):
        self.__caminho = caminho_arquivo
        self.__itens = self.__carregar()

    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                itens = []
                for dado in dados:
                    item = Item(
                        codigo=int(dado["codigo"]),
                        descricao=dado["descricao"],
                        valor_entrada=dado["valor_entrada"],
                        margem_lucro=dado["margem_lucro"],
                        quantidade_disponivel=dado["quantidade_disponivel"]
                    )
                    itens.append(item)
                return itens
        except FileNotFoundError:
            return []

    def __salvar(self):
        dados_serializados = []
        for item in self.__itens:
            dados_serializados.append(item.retorna_dados())
        with open(self.__caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)

    def adiciona(self, item: Item):
        self.__itens.append(item)
        self.__salvar()

    def remove(self, item: Item):
        self.__itens.remove(item)
        self.__salvar()

    def atualiza(self):
        self.__salvar()

    def lista(self):
        return self.__itens

