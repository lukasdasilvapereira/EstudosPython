class Carro:
    def __init__(self):
        pass

    def mover(self):
        print("O carro está se movendo")

class Bicicleta(Carro):
    def __init__(self):
        pass

    def mover(self):
        print("A bike está se movendo")

carro = Carro()
bike = Bicicleta()

Carro.mover(carro)
Bicicleta.mover(bike)


class Funcionario:
    def __init__(self):
        pass

    def calcularPagamento(self):
        ...

class FuncionarioHora(Funcionario):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def calcularPagamento(self):
        pagamento = self.horas * self.valor_hora
        print(pagamento)


class FuncionarioMensal(Funcionario):
    def __init__(self, valor_mensal):
       self.valor_mensal = valor_mensal

    def calcularPagamento(self):
        pagamento = self.valor_mensal
        print(pagamento)

funcionarioHora = FuncionarioHora(50, 10)
funcionarioMensal = FuncionarioMensal(500)

FuncionarioHora.calcularPagamento(funcionarioHora)
FuncionarioMensal.calcularPagamento(funcionarioMensal)