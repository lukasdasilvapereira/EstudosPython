# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(n):
    if n == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True

def deve_ser_int_ou_float(d):
    tipo_n = type(d)
    if not isinstance(d, (int, float)):
        raise TypeError (
            f"{d} deve ser float ou int"
            f'"{tipo_n} enviado"'
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n/d

print(divide(8, 2))