# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def levantar():
    exception_ = MyError("A mensagem de error")
    exception_.add_note("Nota 1")
    exception_.add_note("Adicionando outra nota")
    raise exception_


try:
    levantar()
except (MyError, AnotherError) as error:
    print(error)
    print(error.__class__.__name__)
    print()
    exception_ = AnotherError("Outro error")
    exception_.add_note("Última nota")
    raise exception_ from error
