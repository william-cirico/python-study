"""
Strategy é um padrão de projeto comportamental que tem a intenção de definir
uma família de algoritmos, encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algortimo varie independentemente dos clientes que o
utilizam.

Princípio:
Entidades devem ser abertas para extensão, mas fechadas para modificação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self.__total = total
        self.__discount = discount

    @property
    def total(self):
        return self.__total

    @property
    def total_with_discount(self):
        return self.__discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * .2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * .5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.__discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.__discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order1 = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)
    order3 = Order(1000, no_discount)
    order4 = Order(1000, five_percent)

    print(order1.total, order1.total_with_discount)
    print(order2.total, order2.total_with_discount)
    print(order3.total, order3.total_with_discount)
    print(order4.total, order4.total_with_discount)





