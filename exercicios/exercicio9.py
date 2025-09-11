# Exercício 5: Tabuada Simples (Até 10)
# 1. Escolha um número inteiro (ex: 7) e armazene-o em uma variável 'numero_tabuada'.
# 2. Use um loop `for` para imprimir a tabuada desse número de 1 a 10.
#    Ex:
#    7 x 1 = 7
#    7 x 2 = 14
#    ...
#    7 x 10 = 70

numero = int(input("Digite um número: "))
multiplicador = 0

for resultado in range(10):
    multiplicador += 1

    resultado = numero * multiplicador

    print(f"{numero} x {multiplicador} = {resultado}")
