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
        
    def pega_dados_venda(self):
        return {
            "codigo_item": input("Código do item: "),
            "quantidade": int(input("Quantidade: ")),
            "cpf_cliente": input("CPF do cliente: ")
        }
   
    def mostrar_vendas(self, vendas):
        if not vendas:
            print("Nenhuma venda registrada!")
            return
            
        print("\n=== LISTA DE VENDAS ===")
        for venda in vendas:
            print(f"\nData: {venda.data.strftime('%d/%m/%Y %H:%M')}")
            print(f"Item: {venda.item.descricao}")
            print(f"Quantidade: {venda.quantidade}")
            print(f"Cliente: {venda.cliente.nome}")
            print(f"Vendedor: {venda.funcionario.nome}")
            print(f"Total: R${venda.valor_total:.2f}")
            print("----------------------")

    def mostra_venda_concluida(self, venda):
        print("\n=== VENDA CONCLUÍDA ===")
        print(f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}")
        print(f"Vendedor: {venda.funcionario.nome}") 
        print(f"Item: {venda.item.descricao}")
        print(f"Quantidade: {venda.quantidade}")
        print(f"Valor Unitário: R${venda.item.valor_esperado_venda():.2f}")
        print(f"Valor Total: R${venda.valor_total:.2f}")
        print("=======================")
        
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")