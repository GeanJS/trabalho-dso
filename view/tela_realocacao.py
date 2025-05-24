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
    
    