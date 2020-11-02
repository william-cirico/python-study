"""
Por que testar nosso código?

Testes Automatizados!

TDD - Test Driven Development (Desenvolvimento Guiado por Teste)
Estágios do TDD
    - Você escreve seu teste primeiro;
    - Escrever o codigo mínimo para passar no teste;
    - Refatoração do código;

Estágios são:
    - Red;
    - Green;
    - Refactor;
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f"{self.__nome} está miando...")


felix = Gato("Felix")
felix.miar()
