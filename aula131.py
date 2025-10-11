# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2025 # ATRIBUTO

    def __init__(self, pessoa, idade):
        self.pessoa = pessoa
        self.idade = idade

    def ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa("Lucas", 19)

dados = {'pessoa': 'João', 'idade': 23}
p2 = Pessoa(**dados)

print(p2.__dict__)
print(vars(p2))
# del p2.__dict__['nome']
