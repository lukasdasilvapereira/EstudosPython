"""CALCULADORA COM WHILE"""

while True:
    try:
        n1 = input("Digite um número: ")
        n2 = input("Digite outro número: ")
        n1_float = float(n1)
        n2_float = float(n2)
        operador = input("Digite um operador (+, -, /, *): ")
    except:
        print("Digite um número válido")

 
    if operador == "+":
         print(n1_float + n2_float)
    elif operador == "-":
        print(n1_float - n2_float)
    elif operador == "*":
        print(n1_float * n2_float)
    elif operador == "/":
         print(n1_float / n2_float)
    else:
        print("Digite um operador válido")

    sair = input("Quer sair? [s]im ").lower().startswith("s")

    if sair is True:
        break