"""
POO - Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de
uma classe como variáveis do tipo definido na classe.
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id


lamp1 = Lampada("Azul", 110, 60)
print(lamp1.checa_lampada())
lamp1.ligar_desligar()
print(lamp1.checa_lampada())
cc1 = ContaCorrente(5000, 20000)
u1 = Usuario("William", "Círico", "contato.williamc@gmail.com", "123456")
