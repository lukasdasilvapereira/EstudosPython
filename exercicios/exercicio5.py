# Exercício 5: Condicionais (if/else)
# 1. Peça ao usuário para digitar um número inteiro.
# 2. Verifique se o número é par ou ímpar e imprima a mensagem correspondente.
#    Dica: Use o operador de módulo (%).

inteiro = int(input("Digite um número inteiro: "))

if inteiro % 2 == 0:
    print(f"{inteiro} é par")
else:
    print(f'{inteiro} é ímpar')