# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multi(*args):
    total = 1
    for num in args:
        total *= num
    return total

resultado = multi(1, 5, 90, 35, 100)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def verificar(a):
    if a % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
verificacao = verificar(10)
print(verificacao)