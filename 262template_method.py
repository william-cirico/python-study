"""
Template Method (comportamental tem a intenção de definir um algoritmo em um
método, postergando alguns passos para as subclasses por herança. Template
method permite que subclasses redefinam certos passos de um algoritmo sem mudar
a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso necessário

The Hollywood principle: 'Don't call us, we'll call you'.
(IoC - Inversão de Controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def hook(self): pass


class ConcreteClass(Abstract):
    def hook(self):
        print('Eu utilizo o hook')

    def operation1(self):
        print('Operação 1 concluída')

    def operation2(self):
        print('Operação 2 concluída')


if __name__ == '__main__':
    c1 = ConcreteClass()
    c1.template_method()

