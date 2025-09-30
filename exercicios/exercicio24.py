def decorador(func):

    def criar_funcao(*args, **kwargs):
        print("Sua função foi copiada")
        resultado = func(*args, **kwargs)
        return resultado
    return criar_funcao


@decorador
def soma(x, y):
    return x + y

somando = soma(5, 5)
print(somando)