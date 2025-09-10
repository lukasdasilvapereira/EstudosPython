# Exercício 8: Funções Simples
# 1. Crie uma função chamada 'saudacao' que recebe um nome como argumento e imprime "Olá, [nome]!".
# 2. Chame a função 'saudacao' com seu nome.
# 3. Crie uma função chamada 'soma' que recebe dois números como argumentos e retorna a soma deles.
# 4. Chame a função 'soma' com dois números e imprima o resultado.

def saudacao(nome):
    print(f"Olá {nome}, Seja bem vindo(a)")

saudacao("Lucas Pereira")


def soma(a, b, c):
    print(a + b + c)

soma(5, 20, 500)