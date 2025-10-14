# Sua tarefa:
# 1. Toda vez que um novo carro for criado, aumente o contador.
# 2. Crie um método de classe que mostre o total de carros criados.

class Carro:
    total_carros = 0

    def __init__(self, carros):
        self.carros = carros
        Carro.total_carros += 1

    @classmethod
    def contador(cls):
        return cls.total_carros


c1 = Carro("Celta")
c2 = Carro("Ferrrari")
c3 = Carro("Mercedes")
c4 = Carro("HB20")

print(c1.carros, c2.carros, c3.carros, c4.carros, Carro.contador())

# Crie uma classe Pessoa com um método de classe criar_bebe que retorne uma nova pessoa com idade 0.

class Pessoa:
    def __init__(self):
        pass

    @classmethod

    def criar_bebe(cls, nome, idade=0):
        novo = cls()
        novo.nome = nome
        novo.idade = idade
        return novo

p1 = Pessoa.criar_bebe("Ana")
p2 = Pessoa.criar_bebe("Lucas")
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)


class Funcionario:
    def __init__(self):
       pass

    @classmethod

    def criar_funcionario(cls, nome, cargo):
        novo_funcionario = cls()
        novo_funcionario.nome = nome
        novo_funcionario.cargo = cargo
        return novo_funcionario

f1 = Funcionario.criar_funcionario("Lucas", "Estágiário")
f2 = Funcionario.criar_funcionario("Rogério", "Dono")
print(f1.nome, f1.cargo)
print(f2.nome, f2.cargo)