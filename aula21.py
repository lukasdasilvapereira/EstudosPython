"""OPERADOR LÓGICO NOT"""

# REVERTE AS EXPRESSÕES, SE FOR TRUE VIRA FALSE, SE FOR FALSE VIRA TRUE

senha = input("Senha: ")

if senha != '123456':
    print("Senha incorreta")


if not senha: # QUANDO NÃO TEM NADA DIGITADO
    print("Nada digitado")

print(not True) # FALSE
print(not False) # TRUE