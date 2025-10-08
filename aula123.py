# Problema dos parâmetros mutáveis em funções Python

# lista = [] nos parametros padrões não é bom, então coloque none

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes("Lucas")
adiciona_clientes("Joana", cliente1)
adiciona_clientes("Edu", cliente1)
cliente1.append("Luan")
print(cliente1)

cliente2 = adiciona_clientes("Caio")
adiciona_clientes("Gabriel", cliente2)
adiciona_clientes("João", cliente2)
cliente2.append("Pablo")
print(cliente2)