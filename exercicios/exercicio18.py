def contador(n=0):
    for n in range(10):
        yield n
        n += 1

geni = contador(n=0)

for num in geni:
    print(num)


def par_impar(n=0, maximum=20):

    while n <= maximum:
        if n % 2 == 0:
            yield f"{n}:Par"
        else:
            yield f"{n}:Ímpar"
    
        n += 1

geno = par_impar(0, 20)

for numeros in geno:
    print(numeros)