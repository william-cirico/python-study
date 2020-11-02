"""
O Singleton tem a intenção de garantir que uma classe tenha somente uma instância
e fornece um ponto global de acesso para a mesma.
"""


# Modo tradicional
class SingletonTradicional:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


# Com decorador
def singleton(classe):
    instances = {}

    def get_class(*args, **kwargs):
        if classe not in instances:
            instances[classe] = classe(*args, **kwargs)
        return instances[classe]

    return get_class()


@singleton
class SingletonDecorator:
    def __init__(self):
        self.tema = 'Dark'
        self.fonte = 'Arial'


# Com o call
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super.__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonCall(metaclass=MetaSingleton):
    def __init__(self):
        self.tema = 'Dark'
        self.fonte = 'Arial'


if __name__ == '__main__':
    as1 = SingletonTradicional()
    as2 = SingletonTradicional()

    print(as1 == as2)