"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""

x = 1 # ESCOPO GLOBAL

def escopo(): # ESCOPO INTERNO
    global x # DECLARA O X GLOBAL, ENTÃO O VALOR INTERNO VIRA GLOBAL
    x = 10

    def outra_funcao():
        y = 2
        print(y)
    print(x)

    outra_funcao()

escopo()
print(x)