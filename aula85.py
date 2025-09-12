# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista_1 = [4, 1, 6, 8, 0 , 2, 7, 5, 3]

lista_1.sort(reverse=True) # ORDENA AO CONTRÁRIO
print(lista_1)


def exiba(lista):
    for name in lista:
        print(item)

l1 = sorted(lista, key=lambda name: name["nome"])
l2 = sorted(lista, key=lambda name: name["sobrenome"])

print(l1)





