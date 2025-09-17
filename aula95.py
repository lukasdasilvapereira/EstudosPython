# Generator expression, Iterables e Iterators em Python
# GENERATOR ENTREGA UM VALOR POR VEZ, ELE ESPERA VOCÊ PEDIR, É UMA FUNÇÃO QUE PAUSA

import sys

lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(lista)
print(generator)
print(next(generator))

for n in generator:
    print(n)



