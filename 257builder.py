"""
Builder é um padrão de criação que tem a intenção de separar a construção de um
objeto  complexo  da  sua  representação, de  modo  que  o  mesmo  processo  de
construção possa criar diferentes representações.

Builder  te  dá a possibilidade de criar objetos  passo-a-passo  e  isso  já  é
possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos (method chaining).
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Usuario(StringReprMixin):
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.idade = None
        self.telefones = []
        self.enderecos = []


class IUsuarioBuilder(ABC):
    @property
    @abstractmethod
    def resultado(self):
        pass

    @abstractmethod
    def adicionar_nome(self, nome):
        pass

    @abstractmethod
    def adicionar_sobrenome(self, sobrenome):
        pass

    @abstractmethod
    def adicionar_idade(self, idade):
        pass

    @abstractmethod
    def adicionar_telefone(self, telefone):
        pass

    @abstractmethod
    def adicionar_endereco(self, endereco):
        pass


class UsuarioBuilder(IUsuarioBuilder):
    def __init__(self):
        self.resetar()

    def resetar(self):
        self._resultado = Usuario()

    @property
    def resultado(self):
        return_data = self._resultado
        self.resetar()
        return return_data

    def adicionar_nome(self, nome):
        self._resultado.nome = nome
        return self  # Method Chaining

    def adicionar_sobrenome(self, sobrenome):
        self._resultado.sobrenome = sobrenome
        return self

    def adicionar_idade(self, idade):
        self._resultado.idade = idade
        return self

    def adicionar_telefone(self, telefone):
        self._resultado.telefones.append(telefone)
        return self

    def adicionar_endereco(self, endereco):
        self._resultado.enderecos.append(endereco)
        return self


class UsuarioDiretor:
    def __init__(self, builder: UsuarioBuilder):
        self._builder = builder

    def com_idade(self, nome, sobrenome, idade):
        self._builder.adicionar_nome(nome)
        self._builder.adicionar_sobrenome(sobrenome)
        self._builder.adicionar_idade(idade)

        return self._builder.resultado

    def com_endereco(self, nome, sobrenome, endereco):
        self._builder.adicionar_nome(nome)
        self._builder.adicionar_sobrenome(sobrenome)
        self._builder.adicionar_endereco(endereco)

        return self._builder.resultado


if __name__ == '__main__':
    builder_usuario = UsuarioBuilder()
    diretor_usuario = UsuarioDiretor(builder_usuario)
    usuario1 = diretor_usuario.com_idade('William', 'Círico', 20)
    print(usuario1)



