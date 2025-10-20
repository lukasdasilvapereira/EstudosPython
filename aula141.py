# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_sobrenome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_sobrenome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'

    def falar_nome_sobrenome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

a1 = Aluno("Lucas", "Pereira")
c1 = Cliente("Nenel", "Pereira")
print(a1.nome, a1.sobrenome)
print(c1.nome, c1.sobrenome)
a1.falar_nome_sobrenome()
c1.falar_nome_sobrenome()
print(a1.cpf)
