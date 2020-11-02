"""
Higher Order Functions - HOF

- Quando uma linguagem de programação suport HOF, indica que podemos ter funções que retornam outras funções
como resultado, ou mesmo, que podemos passar funções como argumentos para outras funções.
"""


# Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Divisão por zero"


def calcula(num1, num2, funcao):
    return funcao(num1, num2)


print(calcula(10, 2, somar))
print(calcula(10, 2, diminuir))
print(calcula(10, 2, multiplicar))
print(calcula(10, 2, dividir))

# Nested Functions - Funções Aninhadas
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(("E aí ", "Suma daqui ", "Gosto muito de você "))
    return humor() + pessoa


print(cumprimento("Dominique"))


# Retornando funções de outras funções
def faz_me_rir():
    def rir():
        return choice(("hahahaha", "kkkkkkkkk", "yayayayaya"))
    return rir


rindo = faz_me_rir()
print(rindo())


# Acessando escopo das funções externas
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(("hahahaha", "lolololololo", "kkkkkkkkkkk"))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente("Maria")
print(rindo())
