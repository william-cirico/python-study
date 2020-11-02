"""Documentação de uma linha"""

"""Descrição de várias linhas

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed laoreet justo. Aenean sollicitudin elit nec dui 
venenatis, quis maximus metus molestie. Sed tortor mi, dignissim nec magna eget, sodales mollis ante. Duis tellus mi, 
varius quis urna eget, dapibus auctor ex. Sed odio diam, volutpat id pellentesque ut, laoreet ac lorem. Sed volutpat 
porttitor urna, nec laoreet nisl ornare eget. Vestibulum felis massa, pharetra non feugiat quis, bibendum in odio. 
Proin at risus iaculis, vehicula sapien sit amet, scelerisque risus. Donec feugiat ultricies eros nec tempus. Integer 
laoreet mi eleifend arcu mollis, imperdiet aliquam dui faucibus. Praesent vel tellus sed enim auctor tristique id ut 
est. Aenean sed mauris condimentum, suscipit lectus at, tristique urna. Aliquam erat volutpat.
"""


# Documentação de função
def soma1(x, y):
    """Soma x e y"""
    return x + y


help(soma1)


# Documentação de função descritiva
def multiplica(x, y, z=1):
    """Multiplica x, y, z

    O programador pode omitir a variável z caso não tenha necessidade de usá-la."""
    return x * y * z


help(multiplica)


# Documentação de função detalhada
def soma2(x, y):
    """
    Soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y


help(soma2)


# Documentação de classe
class MinhaClasse:
    """Documentação normal

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed laoreet justo. Aenean sollicitudin elit nec dui
    venenatis, quis maximus metus molestie. Sed tortor mi, dignissim nec magna eget, sodales mollis ante. Duis tellus
    mi, varius quis urna eget, dapibus auctor ex. Sed odio diam, volutpat id pellentesque ut, laoreet ac lorem. Sed
    volutpat porttitor urna, nec laoreet nisl ornare eget. Vestibulum felis massa, pharetra non feugiat quis, bibendum
    in odio. Proin at risus iaculis, vehicula sapien sit amet, scelerisque risus. Donec feugiat ultricies eros nec
    tempus. Integer laoreet mi eleifend arcu mollis, imperdiet aliquam dui faucibus. Praesent vel tellus sed enim auctor
    tristique id ut est. Aenean sed mauris condimentum, suscipit lectus at, tristique urna. Aliquam erat volutpat.
    """

    atributo1 = 1
    atributo2 = "Valor"

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """
        self.__texto = texto

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela

        :param texto: um texto de 100 caracteres
        :type texto: str
        :return: o texto de 100 caracteres
        :rtype: str

        :raises ValueError: se o texto tiver mais que 100 caracteres
        :raises TypeError: se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError("Texto precisa ser uma string.")

        if len(texto) > 100:
            raise ValueError("Texto precisa ter 100 caracteres ou menos.")

        return texto


help(MinhaClasse)


# Type Hints
x: int = 10
y: float = 10.2


# Type Hints em função
def funcao1(p1: float, p2: str, p3: dict) -> float:
    return 10.10


# Type Hints em função com mais de um retorno
from typing import Union


def funcao2() -> Union[list, dict]:
    return list





