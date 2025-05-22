from datetime import datetime

class TelaFuncionario:
    def menu_funcionario(self):
        print("\n--- Menu Funcionario ---")
        print("1 - Cadastrar funcionario")
        print("2 - Listar funcionarios")
        print("3 - Editar funcionario")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_funcionario(self):
        nome = input("Nome do Funcionario: ")
        telefone = input("Telefone do Funcionario: ")
        endereco = input("Endereco do Funcionario: ")
        email = input("Email do Funcionario: ")
        cpf = input("CPF do Funcionario: ")
        data_contratacao = datetime.now()


        return {"nome": nome, "telefone": telefone, "endereco": endereco, "email": email, "cpf": cpf, "data": data_contratacao}

    def mostra_funcionarios(self, funcionarios):
        if not funcionarios:
            print("Nenhum funcionario cadastrado.")
        else:
            for funcionario in funcionarios:
                print("\n==============================")
                print(f"Nome: {funcionario.nome}")
                print(f"Telefone: {funcionario.telefone}")
                print(f"Endereço: {funcionario.endereco}")
                print(f"Email: {funcionario.email}")
                print(f"CPF: {funcionario.cpf}")
                print(f"Data de Cadastro: {funcionario.data_cadastro.strftime('%d/%m/%Y %H:%M:%S')}")
                print("==============================")
    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")