"""Formatação de strings"""

nome = "Lucas Pereira"
altura = 1.70
peso = 85
imc = peso / altura ** 2

linha_1 = f'Olá meu peso é {peso}, Minha altura é {altura:.2f}'

print(linha_1)

print(f"Seu imc é: {imc:.2f}")
print(f"Seu imc é: {imc:,.2f}")
print(f"Seu imc é: {int(imc)}")

#:.,2f => Para colocar virgulas em números grandes

# :.2f => NÚMERO DE CASAS DECIMAIS AO COLOCAR ISSO

# PODE COLOCAR f'' nas variaveis tbm