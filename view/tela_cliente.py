from datetime import datetime
from utils.validacao import validacao_input, nao_vazio

class TelaCliente:
    def menu_cliente(self):
        print("\n--- Menu Cliente ---")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Editar cliente")
        print("4 - Remover cliente")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_cliente(self):
        try:
            nome = validacao_input("Nome do Cliente: ",
                                nao_vazio,
                                "Nome nao pode ficar vazio" )
            
            telefone = validacao_input("Telefone do Cliente: ",
                                    nao_vazio,
                                    "Telefone nao pode ficar vazio" )
            
            endereco = validacao_input("Endereco do Cliente: ",
                                    nao_vazio,
                                    "Endereco nao pode ficar vazio" )
            
            email = validacao_input("Email do Cliente: ",
                                    nao_vazio,
                                    "Email nao pode ficar vazio" )
            
            cpf = validacao_input("CPF do Cliente: ",
                                nao_vazio,
                                "CPF nao pode ficar vazio" )
                        
            data_cadastro = datetime.now()
        
        
            return {
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco,
                "email": email,
                "cpf": cpf,
                "data": data_cadastro
            }
            
        except KeyboardInterrupt:
            print("\nCadastro interrompido pelo usuario")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")

    
    def seleciona_cliente(self, clientes):
        print("\nClientes disponíveis:")
        for i, cliente in enumerate(clientes):
            print(f"{i} - {cliente.nome} (CPF: {cliente.cpf})")

        try:
            return int(input("Digite o número do cliente que deseja: "))
        except ValueError:
            return -1
    
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
                print(f"Registrado Por: {cliente.registrador}")
                print(f"Data de Cadastro: {cliente.data_cadastro.strftime('%d/%m/%Y %H:%M:%S')}")
                print("==============================")
    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")