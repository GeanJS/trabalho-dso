from datetime import datetime
from utils.validacao import validacao_input, nao_vazio

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
        try:
            nome = validacao_input("Nome do Funcionario: ",
                                nao_vazio,
                                "\nNome nao pode ser vazio, Por favor digite o nome corretamente\n")
            telefone = validacao_input("Telefone do Funcionario: ",
                                    nao_vazio,
                                    "\nTelefone nao pode ser vazio, Por favor digite o Telefone corretamente\n")
            endereco = validacao_input("Endereco do Funcionario: ",
                                    nao_vazio,
                                    "\nEndereco nao pode ser vazio, Por favor digite o Email corretamente\n")
            email = validacao_input("Email do Funcionario: ",
                                    nao_vazio,
                                    "\nEmail nao pode ser vazio, Por favor digite o Email corretamente\n")
            cpf = validacao_input("CPF do Funcionario: ",
                                nao_vazio,
                                "\nCPF nao pode ser vazio, Por favor digite o CPF corretamente\n")
            funcao = validacao_input("Função do funcionario: ", nao_vazio, "Funcao nao poe ser vazia, Por favor informe a funcao corretamente")
            salario = float(validacao_input("Salario Inicial do funcionario: ",
                                            nao_vazio,
                                            "\nSalario nao pode ser vazio, Por favor informe o salario do funcionario\n"))
            
            data_cadastro = datetime.now()


            return {"nome": nome,
                    "telefone": telefone,
                    "endereco": endereco,
                    "email": email,
                    "cpf": cpf,
                    "funcao": funcao,
                    "salario": salario,
                    "data_cadastro": data_cadastro}
        except KeyboardInterrupt:
            print("\nCadastro de funcionario interrompido")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            

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
    
    def seleciona_funcionario(self, funcionarios):
        print("\nFuncionarios disponíveis:")
        for i, funcionario in enumerate(funcionarios):
            print(f"{i} - {funcionario.nome} (CPF: {funcionario.cpf})")

        try:
            return int(input("Digite o número do funcionario que deseja: "))
        except ValueError:
            return -1
    
    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")