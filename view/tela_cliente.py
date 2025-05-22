from datetime import datetime

class TelaCliente:
    def menu_cliente(self):
        print("\n--- Menu Cliente ---")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Editar cliente")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_cliente(self):
        nome = input("Nome do Cliente: ")
        telefone = input("Telefone do Cliente: ")
        endereco = input("Endereco do Cliente: ")
        email = input("Email do Cliente: ")
        cpf = input("CPF do cliente: ")
        data_cadastro = datetime.now()
        
        return {"nome": nome, "telefone": telefone, "endereco": endereco, "email": email, "cpf": cpf, "data": data_cadastro}
    
    def mostra_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print("\n==============================")
                print(f"Nome: {cliente.nome}")
                print(f"Telefone: {cliente.telefone}")
                print(f"Endereço: {cliente.endereco}")
                print(f"Email: {cliente.email}")
                print(f"CPF: {cliente.cpf}")
                print(f"Data de Cadastro: {cliente.data_cadastro.strftime('%d/%m/%Y %H:%M:%S')}")
                print("==============================")
    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")