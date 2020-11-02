"""
POO - Herança Múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar
de múltiplas classes, fazendo com que a classe filha herde todos os
atributos e métodos de todas as classes herdadas.

# Obs.: A herança múltipla pode ser feita de duas maneiras:
    - Multiderivação direta;
    - Multiderivação indireta;
"""


# Exemplo Multiderivação Direta:
class Base1:
    pass


class Base2:
    pass


class MultiDerivadaDireta(Base1, Base2):
    pass


# Exemplo Multiderivação Indireta:

class Base1:
    pass


class Base2(Base1):
    pass


class MultiderivadaIndireta(Base2):
    pass


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


# Testando
baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim("Tux")
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Method Resolution Order (MRO)

print(f"Tux é instância de Animal? {isinstance(tux, Animal)}")
print(f"Tux é instância de Aquático? {isinstance(tux, Aquatico)}")
print(f"Tux é instância de Terrestre? {isinstance(tux, Terrestre)}")
print(f"Tux é instância de Pinguim? {isinstance(tux, Pinguim)}")
