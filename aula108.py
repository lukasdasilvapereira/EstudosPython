# VÁRIAVEIS LIVRES + NONLOCAL

def fora(x):
    a = x # variavel livre

    def dentro():
        print(locals())
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

def concatenar(string_inicial):
    valor = string_inicial

    def valor_final(concatenando=""):
        nonlocal valor # NONLOCAL DEIXA A VARIAVEL SER USADA EM QUALQUER LUGAR DO CÓDIGO
        valor += concatenando
        return valor
    return valor_final

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
