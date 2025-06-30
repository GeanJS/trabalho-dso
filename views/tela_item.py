import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaItem:
    def menu_item(self):
        self.__opcao_escolhida = None
        self.__janela = customtkinter.CTk()
        self.__janela.title("Área de Itens")
        self.__janela.geometry("300x350")

        titulo = customtkinter.CTkLabel(self.__janela, text="--- Área de Itens ---")
        titulo.pack(pady=10)

        botoes = [
            ("Cadastrar Item", 1),
            ("Editar Item", 2),
            ("Remover Item", 3),
            ("Listar Itens", 4),
            ("Retornar ao menu principal", 0)
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


    def pega_dados_item(self, locais_disponiveis: list, dados_antigos = None):
        if not locais_disponiveis:
            caixa_de_mensagem.showwarning("Atenção", "Nenhum local de armazenamento disponível.\nCadastre um local antes de adicionar itens.")
            return None
        
        self.__janela_cadastro = customtkinter.CTk()
        self.__janela_cadastro.title("Cadastro de Item")
        self.__janela_cadastro.geometry("400x500")
        
        titulo = customtkinter.CTkLabel(self.__janela_cadastro, text="Cadastro / Edição de Item", font=("Arial", 16))
        titulo.pack(pady=10)
        
        self.__campo_codigo = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Código do Item")
        self.__campo_codigo.pack(pady=5)
        
        self.__campo_descricao = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Descrição do Item")
        self.__campo_descricao.pack(pady=5)
        
        self.__campo_valor_entrada = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Valor de Entrada")
        self.__campo_valor_entrada.pack(pady=5)
        
        self.__campo_margem_lucro = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Margem de Lucro(%)")
        self.__campo_margem_lucro.pack(pady=5)
        
        self.__campo_quantidade = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Quantidade")
        self.__campo_quantidade.pack(pady=5)
        
        nomes_locais = [local.nome for local in locais_disponiveis]
        self.__campo_local = customtkinter.CTkComboBox(self.__janela_cadastro, values=nomes_locais)
        self.__campo_local.pack(pady=5)
        
        if dados_antigos:
            self.__campo_codigo.insert(0, dados_antigos["codigo"])
            self.__campo_codigo.configure(state="disabled")
            self.__campo_descricao.insert(0, dados_antigos["descricao"])
            self.__campo_valor_entrada.insert(0, str(dados_antigos["valor_entrada"]))
            self.__campo_margem_lucro.insert(0, str(dados_antigos["margem_lucro"]))
            self.__campo_quantidade.insert(0, str(dados_antigos["quantidade_disponivel"]))
            if "nome_local" in dados_antigos:
                self.__campo_local.set(dados_antigos["nome_local"])
            else:
                self.__campo_local.set(nomes_locais[0])
        else:
            self.__campo_local.set(nomes_locais[0])
            
        self.__dados_item = None
        
        botao_confimar = customtkinter.CTkButton(self.__janela_cadastro, text="Confirmar", command=lambda:self.__confirmar(locais_disponiveis))
        botao_confimar.pack(pady=5)
        
        botao_cancelar = customtkinter.CTkButton(self.__janela_cadastro, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=5)
        
        self.__janela_cadastro.mainloop()
        self.__janela_cadastro.destroy()
        return self.__dados_item
    
    def __confirmar(self, locais_disponiveis):
        codigo = self.__campo_codigo.get()
        descricao = self.__campo_descricao.get()
        valor = float(self.__campo_valor_entrada.get())
        margem = float(self.__campo_margem_lucro.get())
        quantidade = int(self.__campo_quantidade.get())
        nome_local = self.__campo_local.get()
        
        indice_local = -1
        for indice in range(len(locais_disponiveis)):
            if locais_disponiveis[indice].nome == nome_local:
                indice_local = indice
                break
        
        if indice_local == -1:
            self.mostra_mensagem("Erro: Local de armazenamento não encontrado.  ")
        
        self.__dados_item = {
            "codigo": codigo,
            "descricao": descricao,
            "valor_entrada": valor,
            "margem_lucro": margem,
            "quantidade": quantidade,
            "indice_local": indice_local
        }
        
        self.__janela.quit()

    def __cancelar(self):
        self.__dados_item = None
        self.__janela_cadastro.quit()
    
    def mostra_itens(self, itens: list):
        if not itens:
            self.mostra_mensagem("Nenhum item cadastrado")
            return

        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Lista de Itens")
        self.__janela_lista.geometry("500x500")

        titulo = customtkinter.CTkLabel(self.__janela_lista, text="--- Lista de Itens ---", font=("Arial", 16))
        titulo.pack(pady=10)

        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=460, height=380)
        quadro_scroll.pack(pady=5)

        for item in itens:
            info = (
                f"Código: {item.codigo}\n"
                f"Descrição: {item.descricao}\n"
                f"Valor de Entrada: R$ {item.valor_entrada:.2f}\n"
                f"Margem de Lucro: {item.margem_lucro}%\n"
                f"Valor Esperado de Venda: R$ {item.valor_esperado_da_venda():.2f}\n"
                f"Quantidade Disponível: {item.quantidade_disponivel}"
            )
            label_item = customtkinter.CTkLabel(quadro_scroll, text=info, anchor="w", justify="left")
            label_item.pack(padx=10, pady=8, fill="x")

        botao_fechar = customtkinter.CTkButton(self.__janela_lista, text="Fechar", command=self.__janela_lista.quit)
        botao_fechar.pack(pady=10)

        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()


    def seleciona_item(self, itens: list):
        if not itens:
            self.mostra_mensagem("Nenhum item disponível.")
            return None

        self.__indice_escolhido = None
        self.__janela_selecao = customtkinter.CTk()
        self.__janela_selecao.title("Selecionar Item")
        self.__janela_selecao.geometry("400x200")

        titulo = customtkinter.CTkLabel(self.__janela_selecao, text="Selecione um Item", font=("Arial", 16))
        titulo.pack(pady=10)

        opcoes = [f"{i} - {item.codigo} | {item.descricao}" for i, item in enumerate(itens)]
        self.__combo_itens = customtkinter.CTkComboBox(self.__janela_selecao, values=opcoes, width=350)
        self.__combo_itens.pack(pady=10)
        self.__combo_itens.set(opcoes[0])

        botoes_frame = customtkinter.CTkFrame(self.__janela_selecao)
        botoes_frame.pack(pady=10)

        btn_confirmar = customtkinter.CTkButton(botoes_frame, text="Confirmar", command=self.__confirmar_item)
        btn_confirmar.pack(side="left", padx=10)

        btn_cancelar = customtkinter.CTkButton(botoes_frame, text="Cancelar", command=self.__cancelar_item)
        btn_cancelar.pack(side="left", padx=10)

        self.__janela_selecao.mainloop()
        self.__janela_selecao.destroy()
        return self.__indice_escolhido

    def __confirmar_item(self):
        valor_selecionado = self.__combo_itens.get()
        try:
            self.__indice_escolhido = int(valor_selecionado.split(" - ")[0])
        except (ValueError, IndexError):
            self.__indice_escolhido = None
        self.__janela_selecao.quit()

    def __cancelar_item(self):
        self.__indice_escolhido = None
        self.__janela_selecao.quit()


    def mostra_mensagem(self, mensagem: str):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)
