# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    n: v.upper()
    if isinstance(v, str) else v
    for n, v in produto.items()
}

print(dc)

# sets

s1 = {
    i for i in range(10)
}

print(s1)