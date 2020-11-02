"""
POO - O método super()

super() se refere à super classe
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} faz {som}")


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        #  Animal.__init__(self, nome, especie)
        super().__init__(self, nome, especie)
        self.__raca = raca


felix = Gato("Félix", "Felino", "Angorá")
felix.faz_som("Miau")
