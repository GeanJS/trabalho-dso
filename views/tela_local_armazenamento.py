import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaLocalArmazenamento:
    def menu_local(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Área de locais de Armazenamento")
        self.__janela.geometry("350x400")
        
        titulo = customtkinter.CTkLabel(self.__janela, text="Locais de Armazenamento", font=("Arial", 18))
        titulo.pack(pady=15)
        
        self.__opcao_escolhida = None
        
        botoes = [
            ("Cadastrar Local", 1),
            ("Editar Local", 2),
            ("Remover Local", 3),
            ("Listar Local", 4),
            ("Retornar ao menu princiapl",0)
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
        
    def pega_dados_local(self, dados_antigos=None):
        self.__janela_cadastro = customtkinter.CTk()
        self.__janela_cadastro.title("Cadastro / Edição de Local")
        self.__janela_cadastro.geometry("300x250")
        
        titulo = customtkinter.CTkLabel(self.__janela_cadastro, text="Informe os dados do local", font=("Arial", 16))
        titulo.pack(pady=15)
        
        self.__campo_nome = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Nome do Local")
        self.__campo_nome.pack(pady=10, padx=20, fill='x')
        
        self.__campo_capacidade = customtkinter.CTkEntry(self.__janela_cadastro, placeholder_text="Capacidade máxima")
        self.__campo_capacidade.pack(pady=10, padx=20, fill='x')
        
        if dados_antigos:
            self.__campo_nome.insert(0, dados_antigos.get("nome", ""))
            self.__campo_capacidade.insert(0, str(dados_antigos.get("capacidade", "")))
        
        self.__dados_local = None
        
        botao_confirmar = customtkinter.CTkButton(self.__janela_cadastro, text="Confirmar", command=self.__confirmar)
        botao_confirmar.pack(pady=20)
        
        botao_cancelar = customtkinter.CTkButton(self.__janela_cadastro, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=10)
        
        self.__janela_cadastro.mainloop()
        self.__janela_cadastro.destroy()
        
        return self.__dados_local
    
    def __confirmar(self):
        nome = self.__campo_nome.get().strip()
        capacidade_str = self.__campo_capacidade.get().strip()
        
        if not nome:
            self.mostra_mensagem("O Nome do local não pode ficar vazio")
            return
        
        if not capacidade_str.isdigit():
            self.mostra_mensagem("Capacidade deve ser um número inteiro positivo.")
            return

        capacidade = int(capacidade_str)
        if capacidade <= 0:
            self.mostra_mensagem("Capacidade deve ser maior que zero.")
            return
        
        self.__dados_local = {
            "nome": nome,
            "capacidade": capacidade
        }
        
        self.__janela_cadastro.quit()
    
    def __cancelar(self):
        self.__dados_local = None
        self.__janela_cadastro.quit()
        
    def seleciona_local(self, locais: list) -> int | None:
        self.__janela_selecao = customtkinter.CTk()
        self.__janela_selecao.title("Selecionar Local de Armazenamento")
        self.__janela_selecao.geometry("400x400")

        self.__indice_selecionado = None

        label = customtkinter.CTkLabel(self.__janela_selecao, text="Selecione um local:")
        label.pack(pady=10)

        # Frame com botões para cada local
        frame_botoes = customtkinter.CTkScrollableFrame(self.__janela_selecao, width=380, height=300)
        frame_botoes.pack(pady=10)

        for idx, local in enumerate(locais):
            texto = f"{idx} - Nome: {local.nome} | Capacidade: {local.capacidade} | Ocupado: {local.total_itens_armazenados}"
            botao = customtkinter.CTkButton(frame_botoes, text=texto, command=lambda i=idx: self.__selecionar(i))
            botao.pack(pady=5, fill='x', padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela_selecao, text="Cancelar", command=self.__cancelar_selecao)
        botao_cancelar.pack(pady=15)

        self.__janela_selecao.mainloop()
        self.__janela_selecao.destroy()

        return self.__indice_selecionado

    def __selecionar(self, indice):
        self.__indice_selecionado = indice
        self.__janela_selecao.quit()

    def __cancelar_selecao(self):
        self.__indice_selecionado = None
        self.__janela_selecao.quit()
    
    def mostra_locais(self, locais: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Lista de Locais de Armazenamento")
        self.__janela_lista.geometry("400x450")

        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Locais Cadastrados", font=("Arial", 18))
        titulo.pack(pady=10)

        if not locais:
            mensagem = customtkinter.CTkLabel(self.__janela_lista, text="Nenhum local de armazenamento cadastrado.")
            mensagem.pack(pady=20)
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=380, height=330)
            quadro_scroll.pack(pady=10, padx=10)

            for local in locais:
                texto = (f"Nome: {local.nome}\n"
                        f"Capacidade Máxima: {local.capacidade}\n"
                        f"Itens Armazenados: {local.total_itens_armazenados}\n")

                if local.itens:
                    texto += "Itens:\n"
                    for codigo, quantidade in local.itens.items():
                        texto += f"  - Código: {codigo}, Quantidade: {quantidade}\n"
                else:
                    texto += "Nenhum item armazenado.\n"

                label_local = customtkinter.CTkLabel(quadro_scroll, text=texto, anchor="w", justify="left")
                label_local.pack(pady=5, padx=10, fill="x")

        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Fechar", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)

        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()

                
    def mostra_mensagem(self, mensagem: str):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)