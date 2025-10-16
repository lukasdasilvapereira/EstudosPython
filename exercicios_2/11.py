class Produto:
    def __init__(self, preco):
        self.preco = preco

    @property
    def retornar_preco(self):
        return self.preco

    @retornar_preco.setter
    def retornar_preco(self, valor):
        if self_preco < 0:
            raise ValueError("Valor não pode ser negativo")
        self.preco = valor

p1 = Produto(25)
print(p1.preco)

p1.preco = 40
print(p1.preco)