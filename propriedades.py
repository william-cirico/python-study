"""
POO - Properties

São como os métodos getters e setters do Java
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Cliente: {self.__titular} | Saldo: {self.__saldo}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta("William", 1_000_000, 2_000_000)
conta2 = Conta("Valdete", 500_000, 1_000_000)

conta1.depositar(100)
print(conta1.extrato())

conta1.sacar(1000)
print(conta1.extrato())

conta1.transferir(conta2, 100_000)
print(conta1.extrato())
print(conta2.extrato())

conta1.set_limite(3_000_000)
print(conta1.__dict__)


# Utilizando propriedades
class ContaRefatorada:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extrato(self):
        return f"Cliente: {self.__titular} | Saldo: {self.__saldo}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor):
        self.__saldo -= valor
        conta_destino.__saldo += valor


conta3 = ContaRefatorada("William", 1_000_000, 2_000_000)
print(conta3.saldo)
conta3.limite = 3_500_000
print(conta3.limite)
print(conta3.valor_total)

