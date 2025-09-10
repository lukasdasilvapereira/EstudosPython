"""
CLOSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES
"""

def criar_saudacao(texto, nome):
    def saudar():
        return f'{texto}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao("Bom dia", "Lucas")
falar_boa_noite = criar_saudacao("Boa noite", "Eduardo")

print(falar_bom_dia()) # ISSO É CLOSURE
print(falar_boa_noite())