# CONTADOR

def contador():
    valor = 0

    def incrementar():
        nonlocal valor
        valor += 1
        return valor
    return incrementar


c = contador()
print(c())
print(c())
print(c())
print(c())
