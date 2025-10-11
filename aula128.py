# ESCOPO DA CLASSE E DE MÉTODOS DA CLASSE

class Animal:
    def __init__(self, nome):
        self.nome = nome

    variavel = 'valor'
    print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal("Leão")
print(leao.nome)
print(leao.comendo("Carne"))
print(leao.executar("Maçã"))