# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        self._cor_tinta = cor

    @property
    def cor(self):
        print("ESTOU NO GETTER")
        return self._cor_tinta

    @cor.setter
    def cor(self, valor):
        print("ESTOU NO SETTER")
        self._cor_tinta = valor
        return self._cor_tinta

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
       self._cor_tampa = valor


caneta = Caneta("Azul")
caneta.cor = "Vermelho"
caneta.cor_tampa = "Amarelo"
print(caneta.cor_tampa)
print(caneta.cor)