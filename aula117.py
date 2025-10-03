#filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filtrar_preco(produtos):
    return produtos['preco'] > 100

novos_produtos = list(filter(
    lambda x: x['preco'] > 100,
    #filtrar_preco,
    produtos
))

print_iter(produtos)

print(novos_produtos)