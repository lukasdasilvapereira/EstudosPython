"""LISTAS PART3"""

"""
append = Adiciona um item ao final
insert = Adiciona um item ao índice escolhido
pop = Remove do final ou do índice escolhido
del = apaga um índice
clear = Limpa a lista
extend = Extende a lista
+ = concatena a lista
"""

minha_lista = [1, 2, 3, 4, 5, 6]

minha_lista.append(12334) # ADICIONA UM ITEMAO FINAL DA LISTA

del minha_lista[-1] # VAI SEMPRE REMOVER O ÚLTIMO

minha_lista.insert(0, 5) # ADICIONOU UM ITEM AO ÍNDICE 0

minha_lista.pop(0) # REMOVE UM ELEMENTO, SE EU N POR O ÍNDICE, ELE VAI REMOVER O ÚLTIMO

print(minha_lista)

# CONCATENAR E EXTEND

lista1 = [0, 1, 2, 3] 
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# COPY

lista_a = [1, 2, 3, 6]

lista_b = lista_a.copy()

print(lista_b)

# FOR IN

lista50 = ["Lucas", "Pereira", "Manoel"]

for name in lista50:
    print(name, type(name))