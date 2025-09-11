# Métodos úteis dos dicionários em Python

# SHALLOW COPY AND DEEP COPY

import copy

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2]
}

# COPIA RASA = SHALLOW COPY

# PELA COPIA RASE, OS VALORES IMUTÁVEIS NÃO VÃO SER AFETADOS, MAS OS MUTÁVEIS SIM


#d2 = d1.copy()

#d2['l1'][0] = 9999
#d2['c1'] = 12

#print(d1)
#print(d2)

# DEEP COPY

# AQUI OS VALORES NÃO VÃO SER ALTERADOS INDEPENTEMENTE DE NADA, MAS NÃO PODE TER OUTRO COPY NO CÓDIGO

d2 = copy.deepcopy(d1)

d2['l1'][0] = 9999
d2['c1'] = 12

print(d1)
print(d2)



