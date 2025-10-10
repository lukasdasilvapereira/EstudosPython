class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Olá, Meu nome é {self.nome}. Eu tenho {self.idade} anos!")

p1 = Pessoa("Lucas", 19)
p1.apresentacao()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        print(f"O produto é {self.nome} e custa {self.preco} reais")

    def desconto(self, porcentagem):
        porcentagem = 15
        valor = self.preco * (porcentagem / 100)
        print(f"O desconto de 15% é: {valor:.2f} reais")

p2 = Produto("Camisa de time", 150)

p2.desconto(15)
p2.mostrar_preco()

class Carro:
    def __init__(self, modelo, ano, ligado=False):
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado

    def ligar(self):
        self.ligado = True
        print("Carro ligado")

    def estado(self):
        print(f"O carro está ligado?", self.ligado)

    def carro_completo(self):
        if self.ligar == True:
            print(f"O carro é um {self.modelo}, que foi feito em {self.ano}, ele nesse momento está ligado")
        else:
            print(f"O carro é um {self.modelo}, que foi feito em {self.ano}, ele nesse momento está desligado")


c1 = Carro("Celta", 2010)

c1.ligar()
c1.estado()
c1.carro_completo()
