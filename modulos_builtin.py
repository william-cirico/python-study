"""
Trabalhando com Módulos Built-in (Módulos Integrados)
"""

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando *
from random import *
print(random())

from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())

# Costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice,
    uniform
)

print(random())
print(randint(1, 10))
lista = ["Geek", "University", "Olá"]
print(shuffle(lista))
print(choice("University"))



