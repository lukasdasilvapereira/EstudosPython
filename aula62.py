# SABER O SEGUNDO DIGITO DO CPF
# 74682489070
import sys

cpf = input("Por favor digite os primeiros 10 números do seu CPF: ")

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print("Você digitou número sequenciais")
    sys.exit()

desempacotar = cpf[:11]
contador_regressivo = 11

resultado = 0

for num in desempacotar:
    resultado += int(num) * contador_regressivo
    contador_regressivo -= 1

resto = (resultado * 10) % 11

if resto > 9:
    print("CPF NÃO VÁLIDO")
else:
    print(f"Seu CPF é {cpf}{resto}, É válido")