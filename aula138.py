# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    def ferramenta(self, valor):
        self._ferramenta = valor

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        print(f"{self.nome} está escrevendo")


e1 = Escritor('Lucas')
print(e1.nome)
caneta = FerramentaDeEscrever("Caneta Bic")
caneta.escrever()
# ASSOCIAÇÃO

e1.ferramenta = caneta
e1.ferramenta.escrever()

maquina_de_escrever = FerramentaDeEscrever("Máquina")

e1.ferramenta = maquina_de_escrever
e1.ferramenta.escrever()
    