# Quando o objeto usa outro objeto

class Escritor:

    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor


class Caneta:

    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print("Caneta está escrevendo!!")


class MaquinaDeEscrever:
    pass

    @staticmethod
    def escrever():
        print("Máquina está escrevendo!!")


escritor1 = Escritor("Alles Blau")
escritor2 = Escritor("São João")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

escritor1.ferramenta = caneta
escritor2.ferramenta = maquina

escritor1.ferramenta.escrever()
escritor2.ferramenta.escrever()
