def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

duplica = executa(
    lambda m: lambda n: n * m, 2
)

print(duplica(3))

print(executa(lambda x, y: x + y, 2, 3))

print(executa
(
    lambda *args: sum(args), 1, 2, 3, 4, 6
)
)