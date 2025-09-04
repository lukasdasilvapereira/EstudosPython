"""FATIAMENTO DE STRINGS"""

# FATIAMENTO [INICIO:FINAL:PASSO]

variavel = "Olá, Mundo!"

print(variavel[2])
print(variavel[3:]) #PEGA DO 3 E VAI ATÉ O FINAL
print(variavel[0:5]) # DO 0 ATÉ O 4 PQ O ULTIMO NÃO CONTA
print(variavel[:6]) # PEGA DO INICIO ATÉ O NUMERO ESCRITO

print(len(variavel)) # CONTA A QUANTIDADE

print(variavel[0:9:3]) # INICIO, FINAL E PASSO

print(variavel[::-1]) # VAI AO CONTRÁRIO