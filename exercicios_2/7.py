# REDUCE FAZ UMA REDUÇÃO DE UM VALOR TIPO MAP E FILTER

from functools import reduce

# 1. Somar todos os números

# Dada a lista abaixo, use reduce para somar todos os elementos:

numeros = [2, 5, 7, 3]

resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)


# 2. Multiplicar todos os números

# Use reduce para multiplicar todos os elementos:

numero = [1, 4, 3, 2]
result = reduce(lambda x, y: x * y, numero)

print(result)

#3. Encontrar o maior número

#Use reduce para descobrir o maior número da lista:

numbers = [5, 12, 7, 9]

results = reduce(lambda x, y: x if x > y else y, numbers)

print(results)


