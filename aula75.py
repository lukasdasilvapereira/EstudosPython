# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplicador(a):
    return a * 2

def triplicador(b):
    return b * 3

def quadruplicador(c):
    return c * 4

x = duplicador(5)
y = triplicador(7)
z = quadruplicador(10)

print(x, y, z)

# OUTRA MANEIRA

def criando_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criando_multiplicador(2)
triplicar = criando_multiplicador(3)
quadruplicar = criando_multiplicador(4)

print(duplicar(4), triplicar(6), quadruplicar(70))