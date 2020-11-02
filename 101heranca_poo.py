# Objeto é outro objeto


class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__nome_classe = self.__class__.__name__

    def falar(self):
        print(f"{self.__nome_classe} está falando...")

    @property
    def nome_classe(self):
        return self.__nome_classe


class Cliente(Pessoa):

    def comprar(self):
        print(f"{self.nome_classe} está comprando")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome_classe} está estudando")


cliente = Cliente("William", 20)
aluno = Aluno("Amanda", 21)
cliente.comprar()
aluno.estudar()
