import customtkinter
import tkinter.messagebox as caixa_de_mensagem
class TelaUsuario:
    def __init__(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Login - Lojinhainha")
        self.__janela.geometry("300x250")
        
        self.__mensagem = customtkinter.CTkLabel(self.__janela, text='')
        self.__mensagem.pack(pady=10)
        
        self.__campo_nome = customtkinter.CTkEntry(self.__janela, placeholder_text="Nome: ")
        self.__campo_nome.pack(pady=5)
        
        self.__campo_senha = customtkinter.CTkEntry(self.__janela, placeholder_text="Senha: ")
        self.__campo_senha.pack(pady=5)
        
        self.__botao_entrar = customtkinter.CTkButton(self.__janela, text="Entrar", command=self.__entrar)
        self.__botao_entrar.pack(pady=15)
        
        self.__dados_login = None
    
    def __entrar(self):
        nome = self.__campo_nome.get()
        senha = self.__campo_senha.get()
        self.__dados_login = {
            "nome": nome,
            "senha": senha
        }
        self.__janela.quit()
    
    def pega_dados_usuario(self):
        self.__janela.mainloop()
        self.__janela.destroy()
        return self.__dados_login
    
    def menu_usuario(self):
        self.__janela_menu = customtkinter.CTk()
        self.__janela_menu.title("Menu de Usuário")
        self.__janela_menu.geometry("300x300")
        
        titulo = customtkinter.CTkLabel(self.__janela_menu, text="Menu de Usuário", font=("Arial", 18))
        titulo.pack(pady=20)
        
        self.__opcao_escolhida = None
        
        botao_cadastrar = customtkinter.CTkButton(self.__janela_menu, text="Cadastrar novo Usuário", command=self.__cadastrar)
        botao_cadastrar.pack(pady=10)
        
        botao_remover = customtkinter.CTkButton(self.__janela_menu, text="Remover Usuário", command=self.__remover)
        botao_remover.pack(pady=10)
        
        botao_listar = customtkinter.CTkButton(self.__janela_menu, text="Listar Usuários", command=self.__listar)
        botao_listar.pack(pady=10)
        
        botao_voltar = customtkinter.CTkButton(self.__janela_menu, text="Retornar ao menu principal", command=self.__voltar)
        botao_voltar.pack(pady=10)
        
        self.__janela_menu.mainloop()
        self.__janela_menu.destroy()
        return self.__opcao_escolhida
        
    def __cadastrar(self):
        self.__opcao_escolhida = 1
        self.__janela_menu.quit()
    
    def __remover(self):
        self.__opcao_escolhida = 2
    
    def __listar(self):
        self.__opcao_escolhida = 3
        self.__janela_menu.quit()
        
    def __voltar(self):
        self.__opcao_escolhida = 0
        self.__janela_menu.quit()
        
    def pega_dados_cadastro_usuario(self):
        self.__janela_cadastro = customtkinter.CTk()
        self.__janela_cadastro.title("Cadastro Usuário")
        self.__janela_cadastro.geometry("300x350")
        
        titulo = customtkinter.CTkLabel(self.__janela_cadastro, text="Cadastro de Usuário", font=("Arial", 18))
        titulo.pack(pady=10)
        
        self.__campo_nome_cadastro = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Nome")
        self.__campo_nome_cadastro.pack(pady=5)
        
        self.__campo_senha_cadastro = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Senha")
        self.__campo_senha_cadastro.pack(pady=5)
        
        self.__tipo_var = customtkinter.StringVar(value='funcionario')
        
        texto_tipo = customtkinter.CTkLabel(self.__janela_cadastro, text="Tipo de usuário: ")
        texto_tipo.pack(pady=5)
        
        caixa_tipo = customtkinter.CTkOptionMenu(self.__janela_cadastro, variable=self.__tipo_var, values=["funcionario", "administrador"])
        caixa_tipo.pack(pady=5)
        
        self.__dados_cadastro = None
        
        botao_confirmar = customtkinter.CTkButton(self.__janela_cadastro, text="Cadastrar", command=self.__confirmar_cadastro)
        
        botao_confirmar = customtkinter.CTkButton(self.__janela_cadastro, text="Cadastrar", command=self.__confirmar_cadastro)
        botao_confirmar.pack(pady=20)
        
        self.__janela_cadastro.mainloop()
        self.__janela_cadastro.destroy()
        return self.__dados_cadastro
        
    def __confirmar_cadastro(self):
        nome = self.__campo_nome_cadastro.get()
        senha = self.__campo_senha_cadastro.get()
        tipo = self.__tipo_var.get()
        
        self.__dados_cadastro = {
            "nome": nome,
            "senha": senha,
            "tipo": tipo
        }
        
        self.__janela_cadastro.quit()
    
    
    def selecionar_usuario(self, usuarios:list):
        self.__janela_selecao = customtkinter.CTk()
        self.__janela_selecao.title("Remover Usuário: ")
        self.__janela_selecao.geometry("350x400")
        
        self.__indice_selecionado = None
        
        titulo = customtkinter.CTkLabel(self.__janela_selecao, text="Selecione um usuário para remover", font=("Arial", 14))
        titulo.pack(pady=10)
        
        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_selecao, width=300, height=250)
        quadro_scroll.pack(pady=10)
        
        for numero, usuario in enumerate(usuarios):
            texto = f"{numero} - {usuario.nome} | {usuario.tipo}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda n=numero: self.__selecionar(n))
            botao.pack(pady=5, fill='x', padx=10)
            
        botao_cancelar = customtkinter.CTkButton(self.__janela_selecao, text="Cancelar", command=self.__cancelar_selecao)
        botao_cancelar.pack(pady=15)
        
        self.__janela_selecao.mainloop()
        self.__janela_selecao.destroy()
        return self.__indice_selecionado
    
    def __selecionar(self, numero):
        self.__indice_selecionado = numero
        self.__janela_selecao.quit()
        
    def __cancelar_selecao(self):
        self.__indice_selecionado = None
        self.__janela_selecao.quit()

    def listar_usuarios(self, usuarios: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Lista de Usuários")
        self.__janela_lista.geometry("350x400")
        
        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Usuários Cadastrados", font=("Arial", 16))
        titulo.pack(pady=10)
        
        if not usuarios:
            mensagem = customtkinter.CTkLabel(self.__janela_lista, text="Nenhum usuário cadastrado")
            mensagem.pack(pady=20)
            
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=300, height=250)
            quadro_scroll.pack(pady=10)
            
            for usuario in usuarios:
                texto_usuario = f"Nome: {usuario.nome}| Tipo: {usuario.tipo}"
                item = customtkinter.CTkLabel(quadro_scroll, text=texto_usuario, anchor="w" )
                item.pack(padx=10, pady=5, fill="x")
        
        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Retornar ao menu de usuário", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)
        
        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()
            
    def mostra_mensagem(self, mensagem: str):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)