for i in range(10):
    if i == 2:
        print("O i é 2.. Continuando")
        continue

    if i == 8:
        print("Seu i é 8 e assim seu else não será executado")
        break

    for j in range(1,3):
        print(i, j)

else:
    print("Código concluído sem pausas")