from datetime import datetime

class TelaFuncionario:
    def menu_funcionario(self):
        print("\n--- Menu Funcionario ---")
        print("1 - Cadastrar funcionario")
        print("2 - Listar funcionarios")
        print("3 - Editar funcionario")
        print("4 - Remover funcionario")
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
        funcao = input("Função: ")
        salario = float(input("Salario Inicial: "))
        data_cadastro = datetime.now()


        return {"nome": nome, "telefone": telefone, "endereco": endereco, "email": email, "cpf": cpf, "funcao": funcao, "salario": salario, "data_cadastro": data_cadastro}

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
                print(f"Registrado por: {funcionario.registrador}")
                print(f"Funcao: {funcionario.cargo.funcao}")
                print(f"Salario: R${funcionario.cargo.salario:.2f}")
                print(f"Data de Contratacao: {funcionario.data_cadastro.strftime('%d/%m/%Y')}")
                print("==============================")
    
    def selecionar_funcionario(self):
        return input("Digite o nome do funcionario a ser removido: ")
    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")