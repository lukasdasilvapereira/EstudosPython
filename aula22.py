"""OPERADORES LÓGICOS NOT IN, IN"""

# DENTRO E NÃO DENTRO

nome = "Lucas"
print(nome[2])
print(nome[-1])

print("s" in nome)
print("o" not in nome)
print("cas" not in nome)

nome_2 = input("Seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome_2:
    print(f"{encontrar} está em {nome_2}")
else:
    print(f"{encontrar} não está em {nome_2}")