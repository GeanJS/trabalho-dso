from utils.validacao import validacao_input, nao_vazio

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
        try:
            codigo = validacao_input("Código do Item: ", nao_vazio, "Codigo nao pode ser vazio")
            descricao = validacao_input("Descricao do Item: ", nao_vazio, "descricao nao pode ser vazio")
            local = validacao_input("Local de armazenamento: ", nao_vazio, "Local nao pode ser vazio")

            
            return {
                "codigo": codigo,
                "descricao": descricao,
                "local": local
            }
        except KeyboardInterrupt:
            print("\nOperação cancelada")
        except Exception as e:
            print("\nOcorreu um erro inesperado!")
    
    def mostra_itens(self, itens):
        if not itens:
            print("Nenhum item cadastrado.")
        else:
            for item in itens:
                print("\n==============================")
                print(f"Código: {item.codigo}")
                print(f"Descrição: {item.descricao}")
                print(f"Local de armazenamento: {item.local}")
                print("==============================")
    
    def seleciona_item(self, itens):
        print("\nClientes disponíveis:")
        for i, item in enumerate(itens):
            print(f"{i} - {item.descricao}")

        try:
            return int(input("Digite o número do item que deseja: "))
        except ValueError:
            return -1

    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
