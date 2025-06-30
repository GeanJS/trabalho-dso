import customtkinter
import tkinter.messagebox as caixa_de_mensagem

class TelaVenda:
    def menu_venda(self):
        self.__janela = customtkinter.CTk()
        self.__janela.title("Menu Venda")
        self.__janela.geometry("300x250")

        self.__opcao_escolhida = None

        titulo = customtkinter.CTkLabel(self.__janela, text="Menu Venda", font=("Arial", 18))
        titulo.pack(pady=20)

        botoes = [
            ("Nova Venda", 1),
            ("Listar Vendas", 2),
            ("Voltar", 0)
        ]

        for texto, valor in botoes:
            botao = customtkinter.CTkButton(self.__janela, text=texto, command=lambda v=valor: self.__escolher(v))
            botao.pack(pady=10, fill="x", padx=30)

        self.__janela.mainloop()
        self.__janela.destroy()

        return self.__opcao_escolhida

    def __escolher(self, valor):
        self.__opcao_escolhida = valor
        self.__janela.quit()
    
    def seleciona_funcionario(self, funcionarios: list):
        self.__indice_selecionado = None

        self.__janela = customtkinter.CTk()
        self.__janela.title("Selecione um Funcionário")
        self.__janela.geometry("400x400")

        titulo = customtkinter.CTkLabel(self.__janela, text="Funcionários disponíveis", font=("Arial", 16))
        titulo.pack(pady=10)

        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela, width=350, height=300)
        quadro_scroll.pack(pady=10)

        for i, f in enumerate(funcionarios):
            texto = f"{i} - {f.nome} | {f.cargo.funcao}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda idx=i: self.__selecionar(idx))
            botao.pack(pady=5, fill="x", padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=15)

        self.__janela.mainloop()
        self.__janela.destroy()
        return self.__indice_selecionado
    
    def seleciona_cliente(self, clientes: list):
        self.__indice_selecionado = None

        self.__janela = customtkinter.CTk()
        self.__janela.title("Selecione um Cliente")
        self.__janela.geometry("400x400")

        titulo = customtkinter.CTkLabel(self.__janela, text="Clientes disponíveis", font=("Arial", 16))
        titulo.pack(pady=10)

        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela, width=350, height=300)
        quadro_scroll.pack(pady=10)

        for indice, cliente in enumerate(clientes):
            texto = f"{indice} - {cliente.nome}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda idx=indice: self.__selecionar(idx))
            botao.pack(pady=5, fill="x", padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=15)

        self.__janela.mainloop()
        self.__janela.destroy()
        return self.__indice_selecionado
    
    def seleciona_item(self, itens: list):
        self.__indice_selecionado = None

        self.__janela = customtkinter.CTk()
        self.__janela.title("Selecione um Item")
        self.__janela.geometry("400x400")

        titulo = customtkinter.CTkLabel(self.__janela, text="Itens disponíveis", font=("Arial", 16))
        titulo.pack(pady=10)

        quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela, width=350, height=300)
        quadro_scroll.pack(pady=10)

        for indice, item in enumerate(itens):
            texto = f"{indice} - {item.descricao} | R$ {item.valor_esperado_da_venda():.2f} | Estoque: {item.quantidade_disponivel}"
            botao = customtkinter.CTkButton(quadro_scroll, text=texto, command=lambda idx=indice: self.__selecionar(idx))
            botao.pack(pady=5, fill="x", padx=10)

        botao_cancelar = customtkinter.CTkButton(self.__janela, text="Cancelar", command=self.__cancelar)
        botao_cancelar.pack(pady=15)

        self.__janela.mainloop()
        self.__janela.destroy()
        return self.__indice_selecionado
    
    def pega_quantidade(self, max_disponivel: int):
        self.__quantidade = None

        self.__janela = customtkinter.CTk()
        self.__janela.title("Quantidade")
        self.__janela.geometry("300x200")

        titulo = customtkinter.CTkLabel(self.__janela, text=f"Informe a quantidade (max {max_disponivel})", font=("Arial", 14))
        titulo.pack(pady=20)

        self.__campo_quantidade = customtkinter.CTkEntry(self.__janela)
        self.__campo_quantidade.pack(pady=10, padx=50)

        btn_confirmar = customtkinter.CTkButton(self.__janela, text="Confirmar", command=self.__confirma_quantidade)
        btn_confirmar.pack(pady=10)

        self.__janela.mainloop()

        return self.__quantidade
    
    def mostra_vendas(self, vendas: list):
        self.__janela_lista = customtkinter.CTk()
        self.__janela_lista.title("Histórico de Vendas")
        self.__janela_lista.geometry("600x600")

        titulo = customtkinter.CTkLabel(self.__janela_lista, text="Histórico de Vendas", font=("Arial", 16))
        titulo.pack(pady=10)

        if not vendas:
            label = customtkinter.CTkLabel(self.__janela_lista, text="Nenhuma venda registrada.")
            label.pack(pady=20)
        else:
            quadro_scroll = customtkinter.CTkScrollableFrame(self.__janela_lista, width=550, height=450)
            quadro_scroll.pack(pady=10)

            for venda in vendas:
                texto = f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}\nCliente: {venda.cliente.nome}\n" \
                        f"Funcionário: {venda.funcionario.nome}\nItens:\n"

                for item, qtd in venda.itens:
                    texto += f"  - {item.descricao} (Código: {item.codigo})\n" \
                            f"    Quantidade: {qtd}\n" \
                            f"    Valor Unitário: R$ {item.valor_esperado_da_venda():.2f}\n" \
                            f"    Subtotal: R$ {item.valor_esperado_da_venda() * qtd:.2f}\n"

                texto += f"Valor Total da Venda: R$ {venda.valor_total():.2f}\n------------------------"

                label = customtkinter.CTkLabel(quadro_scroll, text=texto, justify="left", anchor="w")
                label.pack(padx=10, pady=10, fill="x")

        botao_voltar = customtkinter.CTkButton(self.__janela_lista, text="Retornar ao menu", command=self.__janela_lista.quit)
        botao_voltar.pack(pady=15)

        self.__janela_lista.mainloop()
        self.__janela_lista.destroy()

    def pergunta_continuar(self):
        self.__resposta = None

        self.__janela = customtkinter.CTk()
        self.__janela.title("Continuar venda?")
        self.__janela.geometry("300x150")

        label = customtkinter.CTkLabel(self.__janela, text="Deseja adicionar outro item?", font=("Arial", 14))
        label.pack(pady=20)

        def sim():
            self.__resposta = 's'
            self.__janela.quit()

        def nao():
            self.__resposta = 'n'
            self.__janela.quit()

        botao_sim = customtkinter.CTkButton(self.__janela, text="Sim", command=sim)
        botao_sim.pack(side="left", expand=True, padx=30, pady=10)

        botao_nao = customtkinter.CTkButton(self.__janela, text="Não", command=nao)
        botao_nao.pack(side="right", expand=True, padx=30, pady=10)

        self.__janela.mainloop()
        self.__janela.destroy()

        return self.__resposta

    def __selecionar(self, indice):
        self.__indice_selecionado = indice
        self.__janela.quit()

    def __cancelar(self):
        self.__indice_selecionado = None
        self.__janela.quit()
    
    def __confirma_quantidade(self):
        quantidade = int(self.__campo_quantidade.get())
        if quantidade <= 0:
            self.mostra_mensagem("Quantidade deve ser maior que zero")
            return
        self.__quantidade = quantidade
        self.__janela.destroy()
            
    def mostra_mensagem(self, mensagem: str):
        caixa_de_mensagem.showinfo("Mensagem", mensagem)