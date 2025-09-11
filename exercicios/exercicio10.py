# Exercício 2: Conversor de Idade para Dias
# 1. Crie uma variável 'minha_idade' com a sua idade em anos.
# 2. Calcule quantos dias você viveu, considerando 365 dias por ano (ignore anos bissextos por simplicidade).
# 3. Imprima o resultado (ex: "Você viveu aproximadamente X dias.").

idade = int(input("Digite sua idade: "))
conversao = idade * 365

print(f"Você viveu {conversao} dias")