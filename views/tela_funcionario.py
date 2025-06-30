import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaFuncionario:
    def menu_funcionario(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Área do funcionário")
        self.__janela.geometry("400x350")
        
        self.__opcao_escolhida =None
        titulo = customtkinter.CTkLabel(self.__janela, text="Menu Funcionário", font=("Arial", 16))
        titulo.pack(pady=10)

        botoes = [
            ("Cadastrar Funcionário", 1),
            ("Editar Funcionário", 2),
            ("Remover Funcionário", 3),
            ("Listar Funcionários", 4),
            ("Retornar ao menu principal", 0)
        ]

        for texto, valor in botoes:
            botao = customtkinter.CTkButton(self.__janela, text=texto, command=lambda v=valor: self.__escolher(v))
            botao.pack(pady=5, fill="x", padx=20)

        self.__janela.mainloop()
        self.__janela.destroy()

        return self.__opcao_escolhida
    
    def __escolher(self, valor):
        self.__opcao_escolhida = valor
        self.__janela.quit()
    
    def pega_dados_funcionario(self, dados_antigos=None):
        self.__janela_dados = customtkinter.CTk()
        self.__janela_dados.title("Cadastro / Edição de Funcionário")
        self.__janela_dados.geometry("320x400")

        titulo = customtkinter.CTkLabel(self.__janela_dados, text="Dados do Funcionário", font=("Arial", 18))
        titulo.pack(pady=10)

        self.__campo_nome = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Nome")
        self.__campo_nome.pack(pady=5)

        self.__campo_telefone = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Telefone")
        self.__campo_telefone.pack(pady=5)

        self.__campo_endereco = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Endereço")
        self.__campo_endereco.pack(pady=5)

        self.__campo_email = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Email")
        self.__campo_email.pack(pady=5)

        self.__campo_cpf = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="CPF")
        self.__campo_cpf.pack(pady=5)

        self.__campo_funcao = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Função")
        self.__campo_funcao.pack(pady=5)

        self.__campo_salario = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Salário")
        self.__campo_salario.pack(pady=5)

        if dados_antigos:
            self.__campo_nome.insert(0, dados_antigos["nome"])
            self.__campo_telefone.insert(0, dados_antigos["telefone"])
            self.__campo_endereco.insert(0, dados_antigos["endereco"])
            self.__campo_email.insert(0, dados_antigos["email"])
            self.__campo_cpf.insert(0, dados_antigos["cpf"])
            self.__campo_funcao.insert(0, dados_antigos["funcao"])
            self.__campo_salario.insert(0, str(dados_antigos["salario"]))
        
        self.__dados_funcionario = None

        botao_confirmar = customtkinter.CTkButton(self.__janela_dados, text="Confirmar", command=self.__confirmar_dados)
        botao_confirmar.pack(pady=20)
        
        botao_cancelar = customtkinter.CTkButton(self.__janela_dados, text="Cancelar", command=self.__cancelar_dados)
        botao_cancelar.pack(pady=10)

        self.__janela_dados.mainloop()
        self.__janela_dados.destroy()
        return self.__dados_funcionario

    def __confirmar_dados(self):
        self.__dados_funcionario = {
            "nome": self.__campo_nome.get(),
            "telefone": self.__campo_telefone.get(),
            "endereco": self.__campo_endereco.get(),
            "email": self.__campo_email.get(),
            "cpf": self.__campo_cpf.get(),
            "funcao": self.__campo_funcao.get(),
            "salario": self.__campo_salario.get()
        }
        self.__janela_dados.quit()
    
    def __cancelar_dados(self):
        self.__dados_funcionario = None
        self.__janela_dados.quit()
        
    def mostra_funcionários(self, funcionarios: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Funcionários Cadastrados")
        self.__janela_lista.geometry("500x600")

        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Funcionários Cadastrados", font=("Arial", 16))
        titulo.pack(pady=10)

        if not funcionarios:
            mensagem = customtkinter.CTkLabel(self.__janela_lista, text="Nenhum funcionário cadastrado")
            mensagem.pack(pady=20)
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=350, height=400)
            quadro_scroll.pack(pady=10)

            for funcionario in funcionarios:
                texto = (
                    f"Nome: {funcionario.nome}\n"
                    f"Telefone: {funcionario.telefone}\n"
                    f"Endereço: {funcionario.endereco}\n"
                    f"Email: {funcionario.email}\n"
                    f"CPF: {funcionario.cpf}\n"
                    f"Registrado Por: {funcionario.registrador}\n"
                    f"Data de Cadastro: {funcionario.data_cadastro.strftime('%d/%m/%Y %H:%M')}\n"
                    f"Função: {funcionario.cargo.funcao}\n"
                    f"Salário: {funcionario.cargo.salario}\n"
                )
                rotulo = customtkinter.CTkLabel(quadro_scroll, text=texto, anchor="w", justify="left")
                rotulo.pack(padx=10, pady=10, fill="x")

        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Retornar ao menu", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)

        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()

    
    def seleciona_funcionario(self, funcionarios: list):
        self.__janela_selecao = customtkinter.CTk()
        self.__janela_selecao.title("Selecionar Funcionário")
        self.__janela_selecao.geometry("400x500")

        titulo = customtkinter.CTkLabel(self.__janela_selecao, text="Selecione um Funcionário", font=("Arial", 16))
        titulo.pack(pady=10)

        self.__indice_selecionado = None

        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_selecao, width=350, height=400)
        quadro_scroll.pack(pady=10)

        for indice, funcionario in enumerate(funcionarios):
            texto = f"{indice} - {funcionario.nome} | {funcionario.cargo.funcao}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda i=indice: self.__selecionar(i))
            botao.pack(pady=5, fill='x', padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela_selecao, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=15)

        self.__janela_selecao.mainloop()
        self.__janela_selecao.destroy()

        return self.__indice_selecionado

    
    def __selecionar(self, indice):
        self.__indice_selecionado = indice
        self.__janela_selecao.quit()

    def __cancelar(self):
        self.__indice_selecionado = None
        self.__janela_selecao.quit()

            
    def mostra_mensagem(self, mensagem):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)