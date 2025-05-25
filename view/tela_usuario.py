class TelaUsuario:
    def menu_usuario(self):
        print("\n--- Gerenciamento de Usuários ---")
        print("1 - Cadastrar novo usuário")
        print("2 - Excluir usuário")
        print("3 - Listar usuários")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção entre 1, 2 e 3!"))
        except ValueError:
            return -1
    
    def pegar_dados_usuario(self):
        print("\n-- Login na Lojinhainha --")
        nome = input("Nome de Usuario: ")
        senha = input("Senha: ")
        return {"nome": nome, "senha": senha}
    
    def selecionar_usuario(self):
        return input("Digite o nome do usuario a ser removido: ")
    
    def listar_usuarios(self, usuarios):
        print("\nUsuarios cadastrados")
        for usuario in usuarios:
            print(f"- {usuario.nome} | {usuario.tipo}")
    
    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)