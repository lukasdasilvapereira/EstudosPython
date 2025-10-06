# FILTER TEM QUASE O MESMA FUNÇÃO QUE MAP

# 1. Filtrar números pares
# Dada a lista abaixo, use filter para manter apenas os números pares:#

numeros = [3, 8, 12, 5, 7, 10]

resultado = list(filter(lambda x: x % 2 == 0, numeros))
print("Par", resultado)
impares = list(filter(lambda y: y % 2 == 1, numeros))
print("Ímpar", impares)

# 2. Palavras com mais de 4 letras

# Filtre apenas as palavras que têm mais de 4 letras:

palavras = ["sol", "chuva", "vento", "ar"]

result = list(filter(lambda x: len(x) > 3, palavras))
print(result)


# 3. Números positivos

# Dada a lista, filtre apenas os números maiores que zero:

valores = [-5, 0, 3, -1, 8, -2]

valor = list(filter(lambda x: x >= 0, valores))

print(valor)
