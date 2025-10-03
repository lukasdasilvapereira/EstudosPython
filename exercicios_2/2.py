# COUNT EXERCÍCIOS
# É uma função geradora infinita que vai criando números automaticamente, como se fosse um contador.
# Você escolhe de onde começa e quanto aumenta a cada passo.

from itertools import count

# Use itertools.count para imprimir os números de 1 a 10 (lembre-se que ele é infinito, então use um if ou break para parar).
c1 = count(1)

for contador in c1:
    if contador > 10:
        break

    print(contador)

# Gere uma sequência que começa em 100 e vai de 5 em 5.
# → Mostre apenas até o número 130.    


for c in count(100, 5):
    if c > 130:
        break

    print(c)

# Crie uma lista ["maçã", "banana", "laranja"] e use zip com itertools.count para numerar os elementos, assim:


lista = ['Maçã', "Banana", "Laranja"]

for n, f in zip(count(1), lista):
    if n > len(lista):
        break

    print(f'{n} {f}')


# Use itertools.count para gerar números pares começando em 2.
# → Mostre apenas os 6 primeiros.

for n in count(0, 2):

    if n > 6:
        break

    print(n)

# Faça um programa que use itertools.count para numerar frases de um texto.

frases = ["Python é legal", "Estou aprendendo", "Itertools é útil"]

for n, f in zip(count(1), frases):
    if n > len(frases):
        break

    print(f'{n}: {f}')