class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_tudo(self):
        print(self.nome, self.idade, self.matricula)

a1 = Aluno("Lucas", 19, '12344')

a1.exibir_tudo()


# 2° exercicio

class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        print(f"{self.nome} está se movendo")

class Carro(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

    def mover(self):
        print(f"{self.nome} está se movendo")

class Bicicleta(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

    def mover(self):
        print(f"{self.nome} está se movendo")

c1 = Carro("Fiat")
c1.mover()

b1 = Bicicleta("ARO")

b1.mover()

# 3° desafio

class Zoologico:
    def __init__(self, animal, idade, som):
        self.animal = animal
        self.idade = idade
        self.som = som

    def fazer_som(self):
        print(f"{self.animal} de {self.idade} anos de idade, faz esse som {self.som}")

class Leao(Zoologico):

    def __init__(self, animal, idade, som):
        super().__init__(animal, idade, som)
        self.animal = animal
        self.idade = idade
        self.som = som

    def fazer_som(self):
        print(f"{self.animal}, de {self.idade} anos de idade, faz esse som: {self.som}")

class Elefante(Zoologico):

    def __init__(self, animal, idade, som):
        super().__init__(animal, idade, som)
        self.animal = animal
        self.idade = idade
        self.som = som

    def fazer_som(self):
        print(f"{self.animal}, de {self.idade} anos de idade, faz esse som: {self.som}")

class Macaco(Zoologico):

    def __init__(self, animal, idade, som):
        super().__init__(animal, idade, som)
        self.animal = animal
        self.idade = idade
        self.som = som

    def fazer_som(self):
        print(f"{self.animal}, de {self.idade} anos de idade, faz esse som: {self.som}")

l1 = Leao("Leão", 2, "RRRRRRRR🦁")
l1.fazer_som()
e1 = Elefante("Elefante", 50, "UUUUUUU🐘")
e1.fazer_som()
m1 = Macaco("Macaco", 5, "HAHAHAHAHAH🐒")
m1.fazer_som()
