class TelaSistema:
    def tela_opcoes_funcionario(self):
        print("-------- Lojinhainha ---------")
        print("Escolha sua opcao")
        print("1 - Cliente")
        print("2 - Itens")
        print("3 - Loca de Armazenamento")
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
        print("5 - Usuario")
        print("0 - Finalizar sistema")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")