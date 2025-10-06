# MAP RETORNA UMA NOVA LISTA A PARTIR DE UMA ORDEM

# Dobrar valores

# Dada a lista abaixo, use map para dobrar cada número:

numeros = [2, 5, 10, 50, 100]

def dobrar(dobro):
    return dobro * 2

nova_lista = list(map(dobrar, numeros))

print(nova_lista)

# 2. Converter para maiúsculas

# Transforme todas as palavras em maiúsculas

nomes = ["python", "lucas", "estudar"]

def maiuscula(n):
    return n.upper()

novo = list(map(maiuscula, nomes))

print(novo)

# 3. Comprimento das palavras

# Use map para descobrir o tamanho de cada palavra:

frutas = ["uva", "abacaxi", "melancia"]

def comprimento(x):
    return len(x)

nova_fruta = list(map(comprimento, frutas))

print(nova_fruta)

# 4. Somar elementos de duas listas

# Use map para somar os itens correspondentes:

a = [1, 2, 3]
b = [4, 5, 6]

def soma(x, y):
    return x + y

somando = list(map(soma, a, b))

print(somando)