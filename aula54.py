lista_de_compras = [" "]
indice = 0

while True:
    indice += 1
    nomes = input("Adicione um item a lista, Caso queira parar digite [s]air: ")
    lista_de_compras = nomes

    if nomes == "s":
     break

    print(f"{indice} {nomes}")




    

