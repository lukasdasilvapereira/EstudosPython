"""OPERADOR LÓGICO AND"""

# PARA AND PRINTAR, TODAS PRECISAM SER VERDADEIRAS

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = '123456'

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

print(True and True and True)