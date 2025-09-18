# Divisão segura

def dividir():
    print("Vamos dividir")
    a_str = (input("Digite um número: "))
    b_str = (input("Digite outro número: "))

    try:

        a = float(a_str)
        b = float(b_str)

        if a == 0:
            raise ZeroDivisionError("Você tá dividindo por 0")
        elif b == 0:
            raise ZeroDivisionError("Você tá dividindo por 0")

    except ValueError:
        raise ValueError("Digitou uma letra")

    print(a/b)

dividir()