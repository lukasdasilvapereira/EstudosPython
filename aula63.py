# GERADOR DE CPF

import random

nove_digitos = ""

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

print(f"Seu CPF é {nove_digitos}")

# RANDOM É USADO PARA GERAR COISAS ALEATÓRIAS