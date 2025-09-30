# TABUADA

n1 = int(input(("Digite um número e faremos a tabuada até 10: ")))

for n in range(10):
    n += 1
    resultado = n1 * n
    print(f'{n1} * {n} = {resultado}')