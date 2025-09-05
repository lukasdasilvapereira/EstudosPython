"""REPETIÇÕES (WHILE) CONTINUE"""

# FAZ REPETIÇÃO ATÉ CERTA AFIRMAÇÃO SER CORRETA

contador = 0

while contador <= 100:
    contador += 1

    if contador == 27:
        print("Não vou mostrar o 27")
        continue

    print(contador)


    if contador == 40:
        print("Não vou mostrar o", contador)
        continue

    print(contador)

    if contador == 23:
        print("Não vou mostrar o", contador)
        break

print("Acabou")