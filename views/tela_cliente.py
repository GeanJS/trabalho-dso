import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaCliente:
    def menu_cliente(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Menu Cliente")
        self.__janela.geometry("300x300")
        
        titulo = customtkinter.CTkLabel(self.__janela, text="Menu Cliente", font=("Arial", 18))
        titulo.pack(pady=15)
        
        self.__opcao_escolhida = None
        
        botoes = [
            ("Cadastrar Cliente", 1),
            ("Editar Cliente", 2),
            ("Remover Cliente", 3),
            ("Listar Clientes", 4),
            ("Retornar ao menu principal", 0)
        ]

        for texto, valor in botoes:
            botao = customtkinter.CTkButton(self.__janela, text=texto, command=lambda v=valor: self.__escolher(v))
            botao.pack(pady=8, fill="x", padx=20)
            
        self.__janela.mainloop()
        self.__janela.destroy()
        
        return self.__opcao_escolhida

    def __escolher(self, valor):
        self.__opcao_escolhida = valor
        self.__janela.quit()
        
    def pegar_dados_cliente(self, dados_antigos=None):
        self.__janela_dados = customtkinter.CTk()
        self.__janela_dados.title("Dados do cliente")
        self.__janela_dados.geometry("350x400")
        
        titulo = customtkinter.CTkLabel(self.__janela_dados, text="Informe os dados do cliente")
        titulo.pack(pady=10)
        
        self.__campo_nome = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Nome")
        self.__campo_nome.pack(pady=5, padx=20)

        self.__campo_telefone = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Telefone")
        self.__campo_telefone.pack(pady=5, padx=20)

        self.__campo_endereco = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Endereço")
        self.__campo_endereco.pack(pady=5, padx=20)

        self.__campo_email = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Email")
        self.__campo_email.pack(pady=5, padx=20)

        self.__campo_cpf = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="CPF")
        self.__campo_cpf.pack(pady=5, padx=20)
        
        if dados_antigos:
            self.__campo_nome.insert(0, dados_antigos["nome"])
            self.__campo_telefone.insert(0, dados_antigos["telefone"])
            self.__campo_endereco.insert(0, dados_antigos["endereco"])
            self.__campo_email.insert(0, dados_antigos["email"])
            self.__campo_cpf.insert(0, dados_antigos["cpf"])
        
        self.__dados_cliente = None
        
        botao_confirmar = customtkinter.CTkButton(self.__janela_dados, text="Confirmar", command=self.__confirmar)
        botao_confirmar.pack(pady=15)
        
        self.__janela_dados.mainloop()
        self.__janela_dados.destroy()
        
        return self.__dados_cliente
    
    def __confirmar(self):
        nome = self.__campo_nome.get()
        telefone = self.__campo_telefone.get()
        endereco = self.__campo_endereco.get()
        email = self.__campo_email.get()
        cpf = self.__campo_cpf.get()
        
        self.__dados_cliente = {
            "nome": nome,
            "telefone": telefone,
            "endereco": endereco,
            "email": email,
            "cpf": cpf
        }
        self.__janela_dados.quit()
        
    def mostra_clientes(self, clientes: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Clientes Cadastrados")
        self.__janela_lista.geometry("600x600")
        
        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Clientes Cadastrados", font=("Arial", 16))
        titulo.pack(pady=10)
        
        if not clientes:
            mensagem = customtkinter.CTkLabel(self.__janela_lista, text="Nenhum Cliente cadastrado")
            mensagem.pack(pady=20)
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=350, height=300)
            quadro_scroll.pack(pady=10)
            
            for cliente in clientes:
                texto = (
                    f"Nome: {cliente.nome}\n"
                    f"Telefone: {cliente.telefone}\n"
                    f"Endereço: {cliente.endereco}\n"
                    f"Email: {cliente.email}\n"
                    f"CPF: {cliente.cpf}\n"
                    f"Registrado por: {cliente.registrador}\n"
                    f"Data de cadastro: {cliente.data_cadastro.strftime('%d/%m/%Y %H:%M')}\n"
                    "-----------------------"
                )
                label = customtkinter.CTkLabel(quadro_scroll, text=texto, justify="left", anchor="w")
                label.pack(padx=10, pady=5, fill="x")
                
        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Retornar ao menu de cliente", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)
        
        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()
        
    def seleciona_cliente(self, clientes: list):
        self.__janela_selecao = customtkinter.CTk()
        self.__janela_selecao.title("Selecione um cliente")
        self.__janela_selecao.geometry("350x400")
        
        self.__indice_selecionado = None
        
        titulo = customtkinter.CTkLabel(self.__janela_selecao, text="Clientes disponiveis", font=("Arial", 14))
        titulo.pack(pady=10)
        
        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_selecao, width=320, height=250)
        quadro_scroll.pack(pady=10)

        for numero, cliente in enumerate(clientes):
            texto = f"{numero} - {cliente.nome}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda n=numero: self.__selecionar(n))
            botao.pack(pady=5, fill="x", padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela_selecao, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=15)

        self.__janela_selecao.mainloop()
        self.__janela_selecao.destroy()

        return self.__indice_selecionado
    
    def __selecionar(self, numero):
        self.__indice_selecionado = numero
        self.__janela_selecao.quit()
        
    def __cancelar(self):
        self.__indice_selecionado = None
        self.__janela_selecao.quit()
    
    def mostra_mensagem(self, mensagem):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)