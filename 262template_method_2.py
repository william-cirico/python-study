from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        """Template method"""
        self.hook_before_ingredients()
        self.add_ingredients()  # Abstrato
        self.cook()  # Abstrato
        self.cut()  # Concretos
        self.serve()  # Concretos

    def cut(self):
        print(f'{self.__class__.__name__} está cortando a pizza')

    def serve(self):
        print(f'{self.__class__.__name__} está servindo a pizza')

    def hook_before_ingredients(self):
        pass

    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass


class StylishPizza(Pizza):
    def add_ingredients(self):
        print('AModa: presunto, queijo, goiabada')

    def cook(self):
        print('AModa: cozinhando por 45min no forno')


class VegPizza(Pizza):
    def hook_before_ingredients(self):
        print('Veg: Lavando ingredientes')

    def add_ingredients(self):
        print('Veg: Ingredientes Veganos')

    def cook(self):
        print('Veg: Cozinhando por 5min no forno')


if __name__ == '__main__':
    a_moda = StylishPizza()
    a_moda.prepare()

    print()

    veg = VegPizza()
    veg.prepare()
