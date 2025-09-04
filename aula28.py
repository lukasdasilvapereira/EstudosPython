"""FLAGS, ID, IS, IS NOT E NONE"""

# id = identidade

v1 = 'a' # IDENTIDADE

print(id(v1))

# NONE = SEM VALOR

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")

print(passou_no_if, passou_no_if is None) # CHECA PARA VER SE É NONE
print(passou_no_if, passou_no_if is not None) #CHECA PRA VER SE NÃO É NONE


condicao_2 = None

if condicao_2 is None:
    print("Olá")

if condicao_2 is not None:
    print("Oi")