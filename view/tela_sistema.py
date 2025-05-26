class TelaSistema:
    def tela_opcoes_funcionario(self):
        print("-------- Lojinhainha ---------")
        print("Escolha sua opcao")
        print("1 - Cliente")
        print("2 - Itens")
        print("3 - Loca de Armazenamento")
        print("4 - Realocacao")
        print("5 - Venda")
        print("4 - Retornar a tela de inicial")
        print("0 - Finalizar sistema")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def tela_opcoes_administrador(self):
        print("-------- Lojinhainha ---------")
        print("Escolha sua opcao")
        print("1 - Cliente")
        print("2 - Funcionario")
        print("3 - Itens")
        print("4 - Local de Armazenamento")
        print("5 - Realocacao")
        print("6 - Venda")
        print("7 - Usuario")
        print("8 - Retornar a tela de inicial")
        print("0 - Finalizar sistema")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")