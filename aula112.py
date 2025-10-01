l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

lista_soma = []

for a, b in zip(l1, l2):
    lista_soma.append(a + b)

print(lista_soma)

