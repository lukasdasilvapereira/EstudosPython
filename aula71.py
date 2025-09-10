"""
    ARGS - ARGUMENTOS NÃO NOMEADOS
    *args (empacotamento e desempacotamento)

"""

x, y, *resto = [1, 2, 3, 5, 7]
print(x, y, resto)

def argumento(*args):
    total = 0
    for num in args:
        total += num
    print(total)

argumento(5, 21, 10, 16)

numeros = 1, 2, 3, 4, 5, 6, 7

print(*numeros)

outra_soma = argumento(*numeros)

print(sum(numeros))