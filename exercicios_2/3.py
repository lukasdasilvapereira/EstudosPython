# COMBINATIONS, PERMUTATIONS, PRODUCT
# FORMAS DE FAZER COMBINAÇÕES

from itertools import combinations, permutations, product

# combinations(iterável, r)

# Cria combinações sem repetição.

# A ordem não importa.

lista1 = [1, 2, 3, 4, 5]

c = list(combinations(lista1, 2))
print(c)
print(len(c))

# permutations(iterável, r)

# Cria permutações sem repetição.

# A ordem importa.

lista2 = ['A', 'B', 'C']

p = list(permutations(lista2, 2))
print(p)

# product(iterável, repeat=n)

# Faz o produto cartesiano.

# Permite repetição de elementos.

lista3 = [0, 1]

pr = list(product(lista3, repeat=3))
print(pr)