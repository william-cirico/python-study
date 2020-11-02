"""
Doctests

Doctests são teste que colocamos na docstring das funções/métodos Pyhton

Para rodar um teste em docstring:
# python -m doctest -v doctests.py

Obs.: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.
"""


def soma(a, b):
    """Soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


print(soma(3, 4))


# Outro exemplo (Aplicando TDD)


def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar([True, None])
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


# Erro inesperado...
def fala_oi():
    """Fala oi

    >>> fala_oi()
    "oi"
    """
    return "oi"


# Sem o erro...
def fala_oi2():
    """Fala oi

    >>> fala_oi2()
    'oi'
    """
    return "oi"
