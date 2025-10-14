# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonima(cls, idade):
        return cls("Anonima", idade)



p1 = Pessoa.criar_com_50_anos("Carlos")

print(p1.nome, p1.idade)

p2 = Pessoa.criar_anonima(23)

print(p2.nome, p2.idade)