from sys import path

print(*path)

from aula104_package import modulo # MELHOR FORMA
import aula104_package.modulo

print(modulo.soma_do_modulo(1,2))
print(aula104_package.modulo.soma_do_modulo(3, 5))

from aula104_package import fala_oi, soma_do_modulo
