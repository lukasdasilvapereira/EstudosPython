# ATRIBUTOS DE CLASSE

class Pessoa:
    ano_atual = 2025 # ATRIBUTO

    def __init__(self, pessoa, idade):
        self.pessoa = pessoa
        self.idade = idade

    def ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa("Lucas", 19)
p2 = Pessoa("Carlos", 25)
print(p1.ano_de_nascimento())
print(p2.ano_de_nascimento())
print(Pessoa.ano_atual)