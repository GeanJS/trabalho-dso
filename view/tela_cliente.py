import datetime

class TelaCliente():
    def menu_cliente(self):
        print("-------- CLIENTE ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def recebe_dados_cliente(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereco: ")
        cpf = input("CPF: ")
        data_cadatro = datetime.now()
    
    
    def mostra_historico_compras(self):
        pass
    
    def mostra_dados_cliente(self):
        pass