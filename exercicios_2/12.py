# ASSOCIAÇÃO

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
class Curso:
    def __init__(self, nome):
        self.nome = nome

    def matricular(self, aluno):
        print(f"{aluno.nome} se matriculou em {self.nome}")


a1 = Aluno("Lucas")
c1 = Curso("TI")

c1.matricular(a1)

# AGREGAÇÃO

class Departamento:
    def __init__(self, nome):
        self.nome = nome

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamentos(self, *departamentos):
        for d in departamentos:
            self.departamentos.append(d)

    def listar_dps(self):
        for n in self.departamentos:
            print(n.nome)


d1 = Departamento("DP1")
e1 = Empresa("Coca cola")

e1.adicionar_departamentos(d1)
e1.listar_dps()

# COMPOSIÇÃO

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [
            Livro("A Revolução dos Bichos", "George Orwell"),
            Livro("Dom Casmurro", "Machado de Assis")
        ]

    def adicionar_livros(self):
        for l in self.livros:
            print(f"{l.titulo}, {l.autor}")

b1 = Biblioteca("Biblioteca Central")
b1.adicionar_livros()