"""ENUMERATE = enumera iteráveis (indicies)"""

lista = ["Lucas", "João", "Luiz"]

enumerando = list(enumerate(lista, start=19))

print(enumerando)

for num in enumerando:
    print(num)


itens = ["Pão", "Queijo", "Mortadela"]

for nomes in enumerate(itens):
    print(nomes)

for indice, nome in itens:
    indice, nome = itens
    print(indice, nome)
