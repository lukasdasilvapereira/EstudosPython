# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))

    def listar_endereco(self):
        for n in self.endereco:
            print(n.rua, n.numero)


class Endereco:

    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Ceramica", 330)
cliente1.inserir_endereco("Miguel couto", 550)
cliente1.listar_endereco()