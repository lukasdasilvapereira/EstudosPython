#Crie uma list comprehension que gere uma lista com os quadrados dos números de 1 a 10.

lista = [
    numero
    for numero in range(10)
]

print(lista)

# Crie uma list comprehension que gere uma lista apenas com os números pares de 1 a 20.


lista_2 = [
    numero * 2
    for numero in range(11)
]

print(lista_2)

# Dada a mesma lista de palavras do Exercício 3, crie uma list comprehension que converta todas as palavras para letras maiúsculas

filtrando = ["banana", "maçã", "laranja", "uva", "abacaxi", "morango", "goio"]

resultado = [p for p in filtrando if "a" in p]

print(resultado)

# Crie uma list comprehension que gere uma lista com os números de 1 a 100 que são divisíveis por 3 e também por 5.


lista_3 = [
    lista for lista in range(100) if lista % 3 == 0 and lista % 5 == 0
]

print(lista_3)

# Dada a seguinte lista de números, crie uma list comprehension que retorne apenas os números maiores que 10 e que, para esses números, adicione 5 a eles.

lista_de_numero = [2, 15, 7, 22, 10, 30, 8]

pronto = [lista + 5 for lista in lista_de_numero if lista > 10]

print(pronto)

# Crie uma list comprehension que itere de 1 a 10. Se o número for par, coloque "Par", caso contrário, coloque "Ímpar".

par_impar = ["Par" if p % 2 == 0 else "Ímpar" for p in range(10)]

print(par_impar)

# Embora não seja uma list comprehension, é uma conceito similar. Dada uma lista de frutas, crie um dicionário onde as chaves são as frutas e os valores são o comprimento de cada fruta.

frutas = ["maçã", "banana", "cereja", "damasco"]

resultado_frutas = {
    i: p
    for i, p in enumerate(frutas, start=1)
}

print(resultado_frutas)