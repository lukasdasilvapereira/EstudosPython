def banco(saldo_inicial):
    saldo = saldo_inicial

    def depositar(valor):
        nonlocal saldo
        saldo += valor
        return saldo

    def sacar(valor):
        nonlocal saldo
        if valor <= saldo:
            saldo -= valor
            return saldo
        else:
            return "Saldo insuficiente"

    return depositar, sacar


depositar, sacar = banco(100)

print(depositar(10))
print(sacar(50))



        