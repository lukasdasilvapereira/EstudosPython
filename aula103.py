# PODEMOS REPETIR O IMPORT MAS APENAS USANDO O IMPORTLIB, NÃO É UMA BOA PRÁTICA

import importlib

import aula103_m

print(aula103_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula103_m)

print("fim")

