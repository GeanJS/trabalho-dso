from utils.validacao import validacao_input, nao_vazio

class TelaUsuario:
    def menu_usuario(self):
        print("\n--- Gerenciamento de Usuários ---")
        print("1 - Cadastrar novo usuário")
        print("2 - Excluir usuário")
        print("3 - Listar usuários")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    
    def pegar_dados_usuario(self):
        print("\n-- Login na Lojinhainha --")
        try:
            nome = input("Nome de Usuario: ")
            senha = input("Senha: ")
            return {"nome": nome, "senha": senha}
        except KeyboardInterrupt:
            print("\nPrograma Finalizado Forçadamente")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
    
    def pegar_dados_cadastro_usuario(self):
        print("\n-- Cadastro na Lojinhainha --")
        try:
            nome = validacao_input("Nome de usuario:",
                                nao_vazio,
                                "Nome de usuario nao pode ser vazio")
            
            senha = validacao_input("Senha: ",
                                    nao_vazio,
                                    "Senha do usuario nao pode ser vazio")
            
            print("\nQual o tipo do usuário?\n1 - Funcionário\n2 - Administrador")
            while True:
                try:
                    tipo_usuario = int(input().strip())
                    if tipo_usuario == 1:
                        tipo = "funcionario"
                        break
                    elif tipo_usuario == 2:
                        tipo = "administrador"
                        break
                    else:
                        print("Escolha uma opção entre 1 e 2!")
                except ValueError:
                    print("Digite um número válido!")
                    
            return {"nome": nome,
                    "senha": senha,
                    "tipo": tipo}
        except KeyboardInterrupt:
            return None
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")         

    
    def selecionar_usuario(self, usuarios):
        print("\nUsuários disponíveis:")
        for i, usuario in enumerate(usuarios):
            print(f"{i} - {usuario.nome} ({usuario.tipo})")

        try:
            return int(input("Digite o número do usuário que deseja excluir: "))
        except ValueError:
            return -1

    
    def listar_usuarios(self, usuarios):
        print("\nUsuarios cadastrados")
        for usuario in usuarios:
            print(f"- {usuario.nome} | {usuario.tipo}")
    
    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)