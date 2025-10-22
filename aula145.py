# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = None
        self.name = nome

    @property
    def name(self):
        return self._nome

    @name.setter
    @abstractmethod
    def name(self, nome):...

class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @AbstractFoo.name.setter
    def name(self, nome):
        self._nome = nome

foo = Foo("Cachorro")
print(foo.name)