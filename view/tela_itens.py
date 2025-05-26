from datetime import datetime

class TelaItens:
    def menu_itens(self):
        print("\n--- Menu Itens ---")
        print("1 - Cadastrar itens")
        print("2 - Listar itens")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_itens(self):
        codigo = input("Codigo do Item: ")
        descricao = input("Descricao do Item: ")
        valor_entrada = float(input("Valor de entrada do Item: "))
        margem_lucro = float(input("Margem de lucro do Item: "))
        quantidade_disponivel = int(input("Quantidade inicial do Item: "))
        if quantidade_disponivel < 0:
            raise ValueError("Quantidade incial tem que ser um valor maior do que zero!")
        data_cadastro = datetime.now()
    
        return {"codigo": codigo,
                "descricao": descricao,
                "valor_entrada": valor_entrada,
                "margem_lucro": margem_lucro,
                "quantidade_disponivel": quantidade_disponivel,
                "data_cadastro": data_cadastro}
    
    def pega_codigo_item(self):
        try:
            return input("Código do Item: ")
        except KeyboardInterrupt:
            return None
    
    def mostra_itens(self, itens):
        if not itens:
            print("Nenhum item cadastrado.")
        else:
            for item in itens:
                print("\n==============================")
                print(f"Codigo: {item.codigo}")
                print(f"Descricao: {item.descricao}")
                print(f"Valor de entrada: {item.valor_entrada}")
                print(f"Margem de lucro: {item.margem_lucro}")
                print(f"Quantidade disponivel: {item.quantidade_disponivel}")
                print("==============================")
            
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")