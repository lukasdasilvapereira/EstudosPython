# FUNÇÕES DECORADORAS E DECORADORES COM MÉTODOS

def my_rep(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adicionar_rep(cls):
    cls.__repr__ = my_rep
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if "Terra" in resultado:
            print("Você está em casa")
        return resultado
    return interno


@adicionar_rep
class Time:
    def __init__(self, nome):
        self.nome = nome

@adicionar_rep
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time("Flamengo")
inglaterra = Time("Manchester United")

mercurio =  Planeta("Mercúrio")
terra = Planeta("Terra")

print(terra.falar_nome())

print(brasil)
print(inglaterra)
print(mercurio)

