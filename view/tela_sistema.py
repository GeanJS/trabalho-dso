class TelaSistema:
    def tela_opcoes(self):
        print("-------- Lojinhainha ---------")
        print("Escolha sua opcao")
        print("1 - Cliente")
        print("0 - Finalizar sistema")
        try: 
            return int(input("Escolha uma opcao: "))
        except ValueError:
            return -1
    
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")