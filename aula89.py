"""MAIS DE UM FOR EM LIST COMPREHENSION"""

lista_1 = []

for x in range(3):
    for y in range(3):
        lista_1.append((x, y))

print(lista_1)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)