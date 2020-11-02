from abc import ABC, abstractmethod


class Banco:

    def __init__(self, nome):
        self.__nome = nome
        self.__agencia = [1111, 1112, 1113]
        self.__cliente = []
        self.__conta = []

    def inserir_cliente(self, cliente):
        self.__cliente.append(cliente)

    def inser_conta(self, conta):
        self.__conta.append(conta)

    def autenticar(self, cliente):
        if cliente.conta.agencia not in self.__agencia:
            return False

        if cliente not in self.__cliente:
            return False

        if cliente.conta not in self.__conta:
            return False

        return True


class Pessoa(ABC):

    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf


class Cliente(Pessoa):

    def __init__(self, nome, idade, cpf, conta):
        super().__init__(nome, idade, cpf)
        self.__conta = conta

    @property
    def conta(self):
        return self.__conta


class Conta(ABC):

    def __init__(self, agencia, num_conta, saldo):
        self.__agencia = agencia
        self.__num_conta = num_conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise TypeError("Valor de depósito precisa ser numérico")
        self.__saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Agência: {self.__agencia}\n"
              f"Número da Conta: {self.__num_conta}\n"
              f"Saldo: {self.__saldo}\n")

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            return print("Valor de saque precisa ser númerico")

        if self.saldo < valor:
            return print("Saldo Insuficiente")

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):

    def __init__(self, agencia, num_conta, saldo, limite=200):
        super().__init__(agencia, num_conta, saldo)
        self.__limite = limite

    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            return print("Valor de saque precisa ser numérico")

        if (self.saldo + self.__limite) < valor:
            return print("Saldo Insuficiente")

        self.saldo -= valor
        self.detalhes()


def main():
    # Criando o banco
    banco = Banco("Santander")

    # Criando as contas
    conta1 = ContaCorrente(1111, 1102341, 1000)
    conta2 = ContaPoupanca(1112, 323143, 0)
    conta3 = ContaPoupanca(1110, 123122, 0)  # Agência Inválida

    # Criando os clientes
    cliente1 = Cliente("William", 20, "110.814.329-69", conta1)
    cliente2 = Cliente("Valdete", 49, "018.149.059-52", conta2)
    cliente3 = Cliente("José", 33, "829.123.123-32", conta3)

    # Inserindo dados na classe banco
    banco.inser_conta(conta1)
    banco.inser_conta(conta2)
    banco.inser_conta(conta3)

    banco.inserir_cliente(cliente1)
    banco.inserir_cliente(cliente2)
    banco.inserir_cliente(cliente3)

    # Validando operações

    # Cliente 1
    if banco.autenticar(cliente1):
        cliente1.conta.sacar(1100)
        cliente1.conta.depositar(2000)
    else:
        print("Cliente não autenticado")

    # Cliente 2
    if banco.autenticar(cliente2):
        cliente2.conta.sacar(1100)
        cliente2.conta.depositar(2000)
    else:
        print("Cliente não autenticado")

    # Cliente 3
    if banco.autenticar(cliente3):
        cliente3.conta.sacar(1100)
        cliente3.conta.depositar(2000)
    else:
        print("Cliente não autenticado")


if __name__ == "__main__":
    main()




