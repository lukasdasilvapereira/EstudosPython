"""
        SPLIT E JOIN

        iteráveis = listas, tuples, strings, dicionários

  split - divide uma string
  join - une uma string
  strip - corta os espaços
  rstrip - espaços da direita
  lstrip - espaços da esquerda
"""

frase = "Olha só que, coisa interessante"

lista_frases = frase.split(", ")
print(lista_frases)

lista_frases_fixed = []

for i, indice in enumerate(lista_frases):
    lista_frases_fixed.append(lista_frases[i].strip())

# JOIN

frases_unidas = '-'.join(lista_frases) # ´SO FUNCIONA COM ITERÁVEL
print(frases_unidas)