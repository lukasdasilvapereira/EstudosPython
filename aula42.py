frase = "O Python é uma linguagem de programação"\
        "Multiparadigma."\
        "Python foi criado por Guido Van Rossum"


i = 0

apareceu = 0
letrass = ""

while i < len(frase):
    letra_atual = frase[i]

    quantas = frase.count(letra_atual)

    if letra_atual == " ":
        i += 1
        continue

    if apareceu < quantas:
        apareceu = quantas
        letrass = letra_atual

        
    i += 1


print(f'A letra que apareceu mais vezes foi "{letrass}" {apareceu}x')