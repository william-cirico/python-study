"""
Monostate (ou Borg) - É uma variação do Singleton proposto por Alex Martelli
que tem a intenção de garantir que o estado do objeto seja igual para todas as
instâncias.
"""


class StringReprMixin:
    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class MonoStateComplex:
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state

        return obj

    def __init__(self, nome=None, sobrenome=None):

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonoStateSimple()
    m2 = MonoStateSimple('William', 'Círico')
    print(m1, m2)