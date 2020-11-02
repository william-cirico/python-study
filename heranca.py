"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

Obs.: Com a herança a partir de uma classe existente, nos extendemos outra
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

A classe Pessoa é conhecida por:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe em
classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobrescrita de Métodos (Overriding)
    def nome_completo(self):
        return f"Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}"


cliente1 = Cliente("William", "Círico", "110.814.329-69", 1500)
print(cliente1.nome_completo())
print(cliente1.__dict__)

funcionario1 = Cliente("Fernanda", "Círico", "110.814.329-69", 1115487)
print(funcionario1.nome_completo())
print(funcionario1.__dict__)


