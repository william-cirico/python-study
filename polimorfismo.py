"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Method Overriding é a essência do polimorfismo (no exemplo o mesmo animal fala de jeito diferentes).
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método")

    def comer(self):
        print(f"{self.__nome} está comendo")

    @property
    def nome(self):
        return self.__nome


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.nome} fala uau uau")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.nome} fala miau")


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testes

pipi = Cachorro("Pipi")
miau = Gato("Miau")
stuart = Rato("Stuart")

pipi.falar()
miau.falar()
stuart.falar()
