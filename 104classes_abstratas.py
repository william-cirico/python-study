from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.agencia

    @property
    def conta(self):
        return self.conta

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico!")
        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Agencia: {self.__agencia}", end=" ")
        print(f"Conta: {self.__conta}", end=" ")
        print(f"Saldo: {self.__saldo}")

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente!")
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo Insuficiente!")
            return

        self.saldo -= valor
        self.detalhes()
