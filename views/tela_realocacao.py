import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaRealocacao:
    def menu_realocacao(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Menu Realocação")
        self.__janela.geometry("300x300")
        
        self.__opcao_escolhida = None

        titulo = customtkinter.CTkLabel(self.__janela, text="Menu Realocação", font=("Arial", 18))
        titulo.pack(pady=15)
        
        botoes = [
            ("Nova Realocação", 1),
            ("Listar Realocações", 2),
            ("Voltar", 0)
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

    def pega_dados_realocacao(self, locais: list, itens: list):
        self.__janela_dados = customtkinter.CTk()
        self.__janela_dados.title("Realocação de Item")
        self.__janela_dados.geometry("500x600")

        self.__dados = {}
        self.__locais = locais
        self.__itens = itens

        titulo = customtkinter.CTkLabel(self.__janela_dados, text="Realocação de Item", font=("Arial", 16))
        titulo.pack(pady=10)

        # Local de origem
        label_origem = customtkinter.CTkLabel(self.__janela_dados, text="Selecione o Local de Origem:")
        label_origem.pack(pady=5)

        opcoes_origem = [f"{indice} - {local.nome}" for indice, local in enumerate(locais)]
        self.__origem_var = customtkinter.StringVar(value=opcoes_origem[0])
        combo_origem = customtkinter.CTkOptionMenu(self.__janela_dados, values=opcoes_origem, variable=self.__origem_var)
        combo_origem.pack(pady=5)

        botao_proximo = customtkinter.CTkButton(self.__janela_dados, text="Avançar", command=self.__mostrar_itens)
        botao_proximo.pack(pady=15)

        self.__janela_dados.mainloop()
        self.__janela_dados.destroy()

        return self.__dados if self.__dados else None

    def __mostrar_itens(self):
        texto_origem = self.__origem_var.get()
        indice_origem = int(texto_origem.split(" - ")[0])
        local_origem = self.__locais[indice_origem]

        self.__dados = {"indice_origem": indice_origem}

        # Itens do local de origem
        itens_disponiveis = []
        for codigo_str in local_origem.itens:
            for item in self.__itens:
                if item.codigo == int(codigo_str):
                    itens_disponiveis.append(item)
                    break

        if not itens_disponiveis:
            caixa_de_mensagem.showinfo("Aviso", "Este local de origem não possui itens disponíveis.")
            self.__janela_dados.quit()
            return

        # Limpar a tela
        for widget in self.__janela_dados.winfo_children():
            widget.destroy()

        # Seleção do item
        label_item = customtkinter.CTkLabel(self.__janela_dados, text="Selecione o Item:")
        label_item.pack(pady=5)

        opcoes_itens = [f"{item.codigo} - {item.descricao}" for item in itens_disponiveis]
        self.__item_var = customtkinter.StringVar(value=opcoes_itens[0])
        combo_item = customtkinter.CTkOptionMenu(self.__janela_dados, values=opcoes_itens, variable=self.__item_var)
        combo_item.pack(pady=5)

        # Seleção do local de destino (exceto o de origem)
        label_destino = customtkinter.CTkLabel(self.__janela_dados, text="Selecione o Local de Destino:")
        label_destino.pack(pady=10)

        locais_destino = [f"{indice} - {local.nome}" for indice, local in enumerate(self.__locais) if indice != indice_origem]
        self.__destino_var = customtkinter.StringVar(value=locais_destino[0])
        combo_destino = customtkinter.CTkOptionMenu(self.__janela_dados, values=locais_destino, variable=self.__destino_var)
        combo_destino.pack(pady=5)

        # Quantidade
        self.__campo_quantidade = customtkinter.CTkEntry(self.__janela_dados, placeholder_text="Quantidade a realocar")
        self.__campo_quantidade.pack(pady=10)

        botao_confirmar = customtkinter.CTkButton(self.__janela_dados, text="Confirmar", command=self.__confirmar_dados)
        botao_confirmar.pack(pady=20)
        
        botao_cancelar = customtkinter.CTkButton(self.__janela_dados, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=20)

    def __confirmar_dados(self):
        codigo_item = int(self.__item_var.get().split(" - ")[0])
        self.__dados["codigo_item"] = codigo_item

        texto_destino = self.__destino_var.get()
        self.__dados["indice_destino"] = int(texto_destino.split(" - ")[0])

        self.__dados["quantidade"] = int(self.__campo_quantidade.get())

        self.__janela_dados.quit()

    def __cancelar(self):
        self.__dados = None
        self.__janela_dados.quit()

    def mostra_realocacoes(self, realocacoes: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Histórico de Realocações")
        self.__janela_lista.geometry("600x600")

        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Histórico de Realocações", font=("Arial", 16))
        titulo.pack(pady=10)

        if not realocacoes:
            mensagem = customtkinter.CTkLabel(self.__janela_lista, text="Nenhuma realocação registrada.")
            mensagem.pack(pady=20)
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=500, height=400)
            quadro_scroll.pack(pady=10)

            for realocacao in realocacoes:
                texto = (
                    f"Data: {realocacao.data.strftime('%d/%m/%Y %H:%M')}\n"
                    f"Item: {realocacao.item.descricao} (Código: {realocacao.item.codigo})\n"
                    f"Quantidade: {realocacao.quantidade}\n"
                    f"De: {realocacao.local_origem.nome} → Para: {realocacao.local_destino.nome}\n"
                    f"Realizada por: {realocacao.funcionario.nome}\n"
                    "-----------------------------"
                )
                rotulo = customtkinter.CTkLabel(quadro_scroll, text=texto, justify="left", anchor="w")
                rotulo.pack(padx=10, pady=8, fill="x")

        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Voltar", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)

        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()

    def mostra_mensagem(self, mensagem):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)
