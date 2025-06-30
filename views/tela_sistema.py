import customtkinter
import tkinter.messagebox as caixa_de_mensagem
class TelaSistema:
    def menu_funcionario(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Menu Funcionário")
        self.__janela.geometry("300x350")
        
        titulo = customtkinter.CTkLabel(self.__janela, text="----- Lojinhainha -----")
        titulo.pack(pady=10)
        
        self.__opcao_escolhida = None
        
        botoes = [
            ("Área do Cliente", 1),
            ("Área de Armazenamento", 2),
            ("Área de Item", 3),
            ("Área de Realocação", 4),
            ("Área de Vendas", 5),
            ("Retornar a tela de login", 0)
        ]
        
        for texto, valor in botoes:
            botao = customtkinter.CTkButton(self.__janela, text=texto, command=lambda v=valor: self.__escolher(v))
            botao.pack(pady=8, fill='x', padx=20)
        
        self.__janela.mainloop()
        self.__janela.destroy()
        return self.__opcao_escolhida
    
    def menu_administrador(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Menu Administrador")
        self.__janela.geometry("300x400")
        
        titulo = customtkinter.CTkLabel(self.__janela, text="---- Lojinhainha ----")
        titulo.pack(pady=10)
        
        self.__opcao_escolhida = None
        
        botoes = [
            ("Área do cliente", 1),
            ("Área do Funcionário", 2),
            ("Área de Armazenamento", 3),
            ("Área de Item", 4),
            ("Área de Realocação", 5),
            ("Área de Vendas", 6),
            ("Área do Usuário", 7),
            ("Retornar a tela de login", 0)
            
        ]

        for texto, valor in botoes:
            botao = customtkinter.CTkButton(self.__janela, text=texto, command=lambda v=valor: self.__escolher(v))
            botao.pack(pady=8, fill='x', padx=20)
            
        self.__janela.mainloop()
        self.__janela.destroy()
        
        return self.__opcao_escolhida
    
    def __escolher(self, valor):
        self.__opcao_escolhida = valor
        self.__janela.quit()
    
    def mostra_mensagem(self, mensagem):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)