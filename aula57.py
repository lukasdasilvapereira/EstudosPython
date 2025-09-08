"""LISTAS DENTRO DE LISTAS"""

salas = [
    ["Elaine", "Gustavo", "Jonas"],
    ["Lucas"],
    ["Paulo", "Alexandre", "Pedro", (0, 10, 20, 30, 40)],
]

print(salas[1][0])  # EU PEGO O LUCAS AQUI
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3]) # TUPLA DENTRO DA LISTA


for sala in salas:
    for aluno in sala:
        print(aluno)
