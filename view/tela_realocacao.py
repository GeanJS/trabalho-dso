from datetime import datetime

class TelaRealocacao:
    def menu_realocacao(self):
        print("\n--- Menu Realocação ---")
        print("1 - Realocar itens")
        print("2 - Listar todas as realocações")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção entre 1, 2 e 0!"))
        except ValueError:
            return -1
    
    def pega_dados_realocacao(self):
        return {
            "codigo_item": input("Código do item: "),
            "local_origem": input("Local de origem: "),
            "local_destino": input("Local de destino: "),
            "quantidade": int(input("Quantidade: "))
        }
        
    def mostra_realocacoes(self, realocacoes):
        if not realocacoes:
            print("Nenhuma realocação registrada!")
            return
            
        for r in realocacoes:
            print(f"\n[{r['data'].strftime('%d/%m/%Y %H:%M')}] {r['quantidade']}x {r['item'].descricao}")
            print(f"De: {r['origem']} | Para: {r['destino']}")
            print(f"Responsável: {r['funcionario'].nome}")
            
    def mostra_mensagem(self, mensagem):
        print(mensagem)