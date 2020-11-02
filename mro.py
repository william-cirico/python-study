"""
POO - Method Resolution Order

- É a ordem de execução dos métodos.

Em Python, pode-se conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help()
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"

    @property
    def nome(self):
        return self.__nome


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self.nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self.nome} do mar!"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self.nome} está andando"

    def cumprimentar(self):
        return f"Eu sou {self.nome} da Terra!"


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim("Tux")
print(tux.cumprimentar())
