"""OPERADOR LÓGICO OR"""

# PARA OR PRINTAR, UMA PRECISA SER VERDADEIRA

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = '123456'

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

print(True or False or False)

senha = input("Senha: ") or "Sem senha"

print(senha)