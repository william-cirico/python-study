"""
Abstract Factory é uma padrão de criação que fornece uma interface  para  criar
famílias de objetos relacionados ou dependentes sem  especificar  suas  classes
concretas. Geralmente Abstract Factory conta com um  ou  mais  Factory  Methods
para criar seus objetos.

Uma  diferença  importante  entre  Factory  Method  e  Abstract Factory é que o
Factory Method usa herança enquanto Abstract Factory usa a composição.

Princípio: Programe para interfaces, não para implementações.
"""

from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da Zona Norte está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro da Zona Norte popular está buscando o cliente...')


class MotoZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto da Zona Norte está buscando o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da Zona Sul está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular da Zona Sul está buscando o cliente...')


class MotoZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto da Zona Sul está buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto() -> VeiculoPopular:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZS()


class Cliente:
    @staticmethod
    def busca_clientes():
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto = factory.get_moto()
            moto.buscar_cliente()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()