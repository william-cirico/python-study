"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo > valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("O valor deve ser positivo")

    def transferencia(self, conta_destino, valor):
        # 1 - Remover o valor da conta de origem
        self.saldo -= valor
        self.saldo -= 10  # Taxa de transferência

        # 2 - Adicionar o valor na conta de destino
        conta_destino.saldo += valor


# Testando (Atributos Públicos)
conta1 = Conta("William", 150, 1500)
conta2 = Conta("Ane", 300, 2500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 99999999
conta1.limite = 99999999999999999

print(conta1.__dict__)

conta1.transferencia(conta2, 2000)
conta1.extrato()
conta2.extrato()