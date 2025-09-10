"""
Higher Order Functions
Funções de primeira classe

"""

def saudacao(texto, nome):
    return f'{texto}, {nome}'

def executar(funcao, *args):
    return funcao(*args)

print(executar(saudacao,"Bom dia", "Lucas"))
print(executar(saudacao,"Bom dia", "Flaquito"))