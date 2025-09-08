# Exercício 6: Listas
# 1. Crie uma lista de frutas com pelo menos 5 frutas diferentes.
# 2. Imprima a lista inteira.
# 3. Imprima a primeira fruta da lista.
# 4. Imprima a última fruta da lista.
# 5. Adicione uma nova fruta à lista e imprima a lista atualizada.
# 6. Remova uma fruta da lista e imprima a lista novamente.

frutas = ["Goiaba", "Melão", "Melância", "Maçã", "Banana"]

print(frutas)
print(frutas[0])
print(frutas[4])

frutas.append("Limão")
print(frutas)

frutas.pop()

print(frutas)