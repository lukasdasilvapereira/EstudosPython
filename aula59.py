"""DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES"""

lista = ["Maria", "Andressa", 1, 2, 3, "Eduarda"]

a, b, c, *_, u = lista

print(*lista)
print(a, u)
