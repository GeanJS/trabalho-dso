from datetime import datetime

class TelaVenda:
    def menu_venda(self):
        print("\n--- Menu Venda ---")
        print("1 - Realizar venda")
        print("2 - Listar todas as vendas")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
 
    # def pega_dados_venda(self):
    #     data_venda = datetime.now()
    #     vendedor = 
    #     cliente =
    #     item =
    #     quantidade = int(imput("Quantidade da venda: "))
   
    def mostra_todas_vendas(self, vendas):
        if not vendas:
            print("Nenhum item cadastrado.")
        else:
            for venda in vendas:
                print("\n==============================")
                print(f"Vendedor: {venda.vendedor.nome}")
                print(f"Cliente: {venda.cliente.nome}")
                print(f"Item: {venda.item.nome}")
                print(f"Quantidade: {venda.quantidade}")
                print(f"Data da venda: {venda.data_venda.strftime('%d/%m/%Y')}")
                print(f"Valor total: {venda.valor_total}")
                print("==============================")

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")