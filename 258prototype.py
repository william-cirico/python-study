"""
Prototype

Especificar os tipos de objetos a serem criados usando uma instância-protótipo
e criar novos objetos pela cópia desse protótipo
---
Quais objetos são copiados com o sinal de atribuição?
    Imutáveis (copiados)
        - Bool
        - Int
        - Float
        - Tuple
        - Str
    Mutáveis (passados por referência)
        - List
        - Set
        - Dict
        - Class
"""
from __future__ import annotations
from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Pessoa(StringReprMixin):
    def __init__(self, nome: str, sobrenome: str) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__endereco: List[Endereco] = []

    def adiciona_endereco(self, endereco: Endereco):
        self.__endereco.append(endereco)

    def clone(self) -> Pessoa:
        return deepcopy(self)


class Endereco(StringReprMixin):
    def __init__(self, rua: str, numero: str) -> None:
        self.__rua = rua
        self.__numero = numero


if __name__ == '__main__':
    william = Pessoa('William', 'Círico')
    endereco_william = Endereco('Rua Franz Mueller', '1207')
    william.adiciona_endereco(endereco_william)

    valdete = william.clone()
    valdete.nome = 'Valdete'

    print(william)
    print(valdete)


