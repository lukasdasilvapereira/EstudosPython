"""CONTINUAÇÃO DE LISTAS"""

# CRIAR, LER, ALTERAR, APAGAR (CRUD)

lista2 = [10, 20, 30, 40, 2500]

del lista2[4] # DELETA O ELEMENTO

numero = lista2[2]

print(numero)
print(lista2)

lista2.append("Lucas") # VAI ADICIONAR UM ELEMENTO AO FINAL DA LISTA

ultimo_valor = lista2.pop() # REMOVE O ÚLTIMO ELEMENTO

print(lista2, f"Removido {ultimo_valor}")