"""RETORNO DE VALORES DE FUNÇÕES (RETURN)"""

# AO USAR O RETURN A GENTE PODE USAR ESSES VALORES DEPOIS, COMO VARIÁVEIS POR EXEMPLO

def soma(x, y):
    if x > 10:
        return 20
    return x + y

soma1 = soma(5, 5)
soma2 = soma(2, 13)

print(soma1 + soma2)