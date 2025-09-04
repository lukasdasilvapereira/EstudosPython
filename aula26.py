"""INTRODUÇÃO A TRY/EXCEPT"""

numero = input("Vou dobrar o número que você digitar: ")

numero_float = float(numero)
print(f"{numero.isdigit()}") # CHECA SE SÓ FOI DIGITADO NÚMEROS

print(f"O dobro de {numero} é {numero_float * 2:.1f}")

try:
    print(10 == 10)
except:
   print("Isso não tá certo")