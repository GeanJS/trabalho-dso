import json
from datetime import datetime
from models.venda import Venda
from models.item import Item
from models.funcionario import Funcionario
from models.cliente import Cliente

class VendaDAO:
    def __init__(self, controlador_item, controlador_funcionario, controlador_cliente, caminho_arquivo="vendas.json"):
        self.__caminho = caminho_arquivo
        self.__controlador_item = controlador_item
        self.__controlador_funcionario = controlador_funcionario
        self.__controlador_cliente = controlador_cliente
        self.__vendas = self.__carregar()

    def __carregar(self):
        try:
            with open(self.__caminho, "r", encoding="utf-8") as arquivo:
                dados_json = json.load(arquivo)
                vendas = []
                for dado in dados_json:
                    itens_venda = []
                    for item_dict in dado["itens"]:
                        item = self.__controlador_item.busca_por_codigo(item_dict["codigo"])
                        if item is None:
                            continue
                        quantidade = item_dict["quantidade"]
                        itens_venda.append((item, quantidade))

                    funcionario = self.__controlador_funcionario.busca_por_nome(dado["funcionario"])
                    cliente = self.__controlador_cliente.busca_por_nome(dado["cliente"])

                    if funcionario is None or cliente is None:
                        continue

                    data = datetime.strptime(dado["data"], "%Y-%m-%d %H:%M")

                    venda = Venda(
                        data=data,
                        itens=itens_venda,
                        funcionario=funcionario,
                        cliente=cliente
                    )
                    vendas.append(venda)
                return vendas
        except FileNotFoundError:
            return []

    def __salvar(self):
        dados_serializados = []
        for venda in self.__vendas:
            dados_serializados.append(venda.retorna_dados())

        with open(self.__caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)

    def adiciona(self, venda: Venda):
        self.__vendas.append(venda)
        self.__salvar()

    def lista(self):
        return self.__vendas
