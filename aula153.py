# FUNÇÕES DECORADORAS E DECORADORES COM CLASSES

def my_rep(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adicionar_rep(cls):
    cls.__repr__ = my_rep
    return cls

@adicionar_rep
class Time:
    def __init__(self, nome):
        self.nome = nome

@adicionar_rep
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time("Flamengo")
inglaterra = Time("Manchester United")

mercurio =  Planeta("Mercúrio")

print(brasil)
print(inglaterra)
print(mercurio)

