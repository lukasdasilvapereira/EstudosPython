#1. Divisão segura

#Peça dois números ao usuário e faça a divisão.

try:
    print("VAMOS DIVIDIR")
    n1 = float(input("Digite um número: "))
    n2 =float(input("Digite outro número: "))
    n3 = n1/n2
    print(f"{n3:.1f}")
except Exception as error:
    print(error)
finally:
    print("Operação finalizada")