numero_int = input("Digite um número inteiro: ")

try:
    numero = int(numero_int)
    if numero % 2 == 0:
        print(f"{numero_int} é par")
    else:
        print(f"{numero_int} é ímpar")
except:
    print("Digite um número válido")