from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self):
        pass

    @abstractmethod
    def falar(self):
        pass

class Aluno:
    def falar(self):
        print("Oi, sou Aluno")


a1 = Aluno()
a1.falar()


class Veiculo:
    def __init__(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def mover(self):
        print("O carro está se movendo")


class Bicicleta(Veiculo):
    def __init__(self):
        pass

    def mover(self):
        print("A bicicleta está pedalando")

c1 = Carro()
c1.mover()

b1 = Bicicleta()
b1.mover()


    