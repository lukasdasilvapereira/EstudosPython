"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.

"""

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

soma(10, 20, 50)
soma(2, 5, 0)

# USAMOS ESSE NONE PRA CASO A PESSOA DIGITAR QUALQUER OUTRO VALOR QUE NÃO SEJA NONE