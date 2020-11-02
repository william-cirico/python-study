"""
Factory Method

É um padrão de criação que permite definir uma interface para criar objetos, mas
deixa as subclasses decidirem quais objetos criar. O Factory Method permite adiar
a instanciação para as subclasses, garantindo o baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo: str):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        raise ValueError('Veículo não existe')


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        raise ValueError('Veículo não existe')


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro_zona_norte = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro_zona_norte.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro_zona_sul = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro_zona_sul.buscar_cliente()



