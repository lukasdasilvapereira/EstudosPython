# GROUPBY
# Serve para agrupar elementos consecutivos iguais de um iterável (lista, string, etc).
# Importante: ele só agrupa valores consecutivos, então geralmente é usado em listas ordenadas.

# Use groupby para mostrar cada letra e quantas vezes ela aparece consecutivamente.

from itertools import groupby


letras = ["a", "a", "b", "b", "b", "c", "a", "a"]

for n, i in groupby(letras):
    print(n, len(list(i)))

# Agrupe as palavras pela primeira letra usando groupby.

palavras = ["gato", "galinha", "cachorro", "cavalo", "girafa", "ganso"]


palavras_agrupadas = sorted(palavras)

for chave, nome in groupby(palavras_agrupadas, key=lambda x: x[0]):
    print(chave, list(nome))

# Conte quantas vezes cada caractere aparece seguido (sequência de caracteres repetidos).

texto = "aaabbccccdaa"

texto_agrupado = sorted(texto)

for c, qtd in groupby(texto_agrupado):
    print(c, len(list(qtd)))