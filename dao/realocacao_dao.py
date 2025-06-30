import json
from datetime import datetime
from models.realocacao import Realocacao

class RealocacaoDAO:
    def __init__(self,controlador_item, controlador_funcionario, controlador_local, caminho_arquivo="realocacoes.json"):
        self.__caminho = caminho_arquivo
        self.__controlador_item = controlador_item
        self.__controlador_funcionario = controlador_funcionario
        self.__controlador_local = controlador_local
        self.__realocacoes = self.__carregar()

    def __carregar(self):
        try:
            with open(self.__caminho, 'r', encoding='utf-8') as arquivo:
                dados_json = json.load(arquivo)
                realocacoes = []
                for dado in dados_json:
                    item = self.__controlador_item.busca_por_codigo(dado["item_codigo"])
                    funcionario = self.__controlador_funcionario.busca_por_nome(dado["funcionario_nome"])
                    origem = self.__controlador_local.busca_por_nome(dado["local_origem"])
                    destino = self.__controlador_local.busca_por_nome(dado["local_destino"])

                    if item and funcionario and origem and destino:
                        realocacao = Realocacao(
                            data=datetime.strptime(dado["data"], "%Y-%m-%d %H:%M"),
                            quantidade=dado["quantidade"],
                            item=item,
                            funcionario=funcionario,
                            local_origem=origem,
                            local_destino=destino
                        )
                        realocacoes.append(realocacao)
                return realocacoes
        except FileNotFoundError:
            return []

    def __salvar(self):
        dados_serializados = []
        for realocacao in self.__realocacoes:
            dados = {
                "data": realocacao.data.strftime("%Y-%m-%d %H:%M"),
                "quantidade": realocacao.quantidade,
                "item_codigo": realocacao.item.codigo,
                "funcionario_nome": realocacao.funcionario.nome,
                "local_origem": realocacao.local_origem.nome,
                "local_destino": realocacao.local_destino.nome
            }
            dados_serializados.append(dados)

        with open(self.__caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_serializados, arquivo, indent=4, ensure_ascii=False)

    def adiciona(self, realocacao: Realocacao):
        self.__realocacoes.append(realocacao)
        self.__salvar()

    def lista(self):
        return self.__realocacoes
