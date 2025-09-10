"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y):
    print(x + y)

soma(10, 10) # ARGUMENTO POSICIONAL


def valores(x, y):
    print(f"{x=} {y=} | x + y é igual a {x + y} ")

valores(5, 2)


def dias(a, b):
    print(f"Hoje é {a} e amanhã é {b}")

dias(a="Sábado", b="Domingo") # ARGUMENTO NOMEADO