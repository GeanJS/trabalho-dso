class TelaLocalArmazenamento:
    def menu_local_armazenamento(self):
        print("\n--- Menu Local Armazenamento ---")
        print("1 - Cadastrar local de armazenamento")
        print("2 - Listar locais de armazenamento")
        print("3 - Editar local de armazenamento")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_local_armazenamento(self):
        nome = input("Nome do local de armazenamento: ")
        descricao = input("Descrição do local de armazenamento: ")
        capacidade = int(input("Capacidade do local de armazenamento: "))
        
        return {"nome": nome, "descricao": descricao, "capacidade": capacidade}
    
    def mostra_locais_armazenamento(self, locais_armazenamento):
        if not locais_armazenamento:
            print("Nenhum local de armazenamento cadastrado.")
        else:
            for local in locais_armazenamento:
                print("\n==============================")
                print(f"Nome: {local.nome}")
                print(f"Descrição: {local.descricao}")
                print(f"Capacidade: {local.capacidade}")
                print("==============================")

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")