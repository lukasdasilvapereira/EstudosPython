nomes = ["Ana", "Lucas", "Bruno"]
idades = [21, 19, 22]

print(list(zip(nomes, idades)))

#from intertools import zip_longest

alunos = ["Lucas", "Anderson", "Gabriele", "Fernando"]
notas = [8.5, 9.0, 5.0]

print(list(zip(alunos, notas)))

# SOMA

a = [1, 2, 3]
b = [10, 20, 30]
nova_lista = []

for n, c in zip(a, b):
    nova_lista.append(n + c)

print(nova_lista)

# Times
from itertools import zip_longest

estados = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

times = ["Palmeiras", "Flamengo"]

print(list(zip_longest(estados, times, fillvalue="N/A")))

