"""IMPRECISÃO DO FLOAT"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

# PARA CONSERTAR ESSE PROBLEMA TEMOS DUAS FORMAS SIMPLES

print(f"{numero_3:.2f}")
print(round(numero_3, 3)) # o 3 é a quantidade de casas decimais que eu quero