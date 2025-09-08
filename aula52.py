"""TUPLAS => TIPO DE LISTA IMUTÁVEL"""

nomes = ("Lucas", "Olá", "José")

print(nomes[0])

itens = ["Pão", "Queijo", "Mortadela"]

mudando_lista_para_tuplas = tuple(itens)

print(type(mudando_lista_para_tuplas))

mudando_tuplas_para_lista = list(mudando_lista_para_tuplas)