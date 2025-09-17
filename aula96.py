# Introdução as generator functions em python

def generator(n=0):
    yield 1 # PAUSAR
    print("Continuando...")
    yield 2
    print("Mais uma...")
    yield 3
    return "Acabou"


gen = generator(n=0)
for n in gen:
    print(n)


def loop(n=0, maximum=10):
    while True:
        yield n

        n += 1

        if n >= maximum:
            return 


geni = loop()
for n in geni:
    print(n)

    