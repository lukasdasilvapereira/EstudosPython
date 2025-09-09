# SABER O PRIMEIRO DIGITO DO CPF
# 74682489070

cpf = input("Por favor digite os primeiros 9 números do seu CPF: ")

desempacotar = cpf[:9]
contador_regressivo = 10

resultado = 0

for num in desempacotar:
    resultado += int(num) * contador_regressivo
    contador_regressivo -= 1

resto = (resultado * 10) % 11

print(resto)

if resto > 9:
    print("O resultado é 0")
else:
    print(f"O resultado é {resto}")



