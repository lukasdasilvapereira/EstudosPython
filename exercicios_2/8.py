arquivo_novo = 'notas.txt'

with open(arquivo_novo, 'w+') as arquivo:
    arquivo.write('8.5\n')
    arquivo.write('7.0\n')
    arquivo.write('9.0\n')
    arquivo.seek(0)
    for linha in arquivo:
        print("Nota:", linha.strip())



# 2° Exercício

arquivo_copia = 'copia.txt'

with open(arquivo_novo, 'r') as original:
    conteudo = original.read()


with open(arquivo_copia, 'w') as copia:
    copia.write(conteudo)

with open(arquivo_copia, 'r') as ver:
    print(ver.read())

