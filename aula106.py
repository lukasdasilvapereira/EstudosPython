import copy

from aula105 import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

print(produtos)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

print(*novos_produtos, sep="\n")

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

print(*produtos_por_nome, sep="\n")

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_por_reverso = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print(*produtos_por_reverso, sep="\n")

# PREÇO DO MENOR PARA O MAIOR

produtos_por_preco_crescente = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print(*produtos_por_preco_crescente, sep="\n")
