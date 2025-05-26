def validacao_input(mensagem, funcao_validacao, mensagem_erro):
    while True:
        valor = input(mensagem).strip()
        if funcao_validacao(valor):
            return valor
        print(mensagem_erro)
        
def nao_vazio(valor):
    return bool(valor.strip())

def confirma_acao(mensagem: str) -> bool:
    while True:
        resposta = input(f"{mensagem} (sim/nao): ").strip().lower()
        if resposta in ("sim", "nao"):
            return resposta == "sim"
        print("Por favor, responda com sim ou nao.")