import re
from exceptions.validation_exceptions import ValidationException

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

class ValidacaoDados:
    
    @staticmethod
    def valida_nome(nome):
        if not nome or nome.strip():
            raise ValidationException
        
        if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome.strip()):
            raise ValidationException("nome", "O Nome deve ter apenas letras!")
    
        return nome.strip().title()

    @staticmethod
    def valida_telefone(telefone):
        if not telefone or not telefone.strip():
            raise ValidationException("telefone", "O Telefone é obrigatório")
        
        telefone_limpo = re.sub(r'[^\d]', '', telefone)

        #Aqui tem que colocar no texto do telefone que tem que por ddd
        if len(telefone_limpo) == 10:
            return f"({telefone[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
        else:
            return f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"
        
    @staticmethod
    def validar_tudo(dados):
        dados_validados = {}
        #testando se precisa trazer validação de erros
        erros = []

        campos_validacao = [
            ('nome', ValidacaoDados.valida_nome),
            ('telefone', ValidacaoDados.valida_telefone)
        ]

        for campo, validacao in campos_validacao:
            try:
                if campo in dados:
                    dados_validados[campo] = validacao(dados[campo])
            except ValidationException as e:
                erros.append(e.mensagem)

        for campo, valor in dados.items():
            if campo not in dados_validados:
                dados_validados[campo] = valor

        return dados_validados