"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever códigos 
[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou
variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 3

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
*Separar funções e classes com duas linhas em branco;
*Métodos dentro de uma classe devem ser separados com uma linha em branco;


class Clase:
    pass


class Outra:
    pass

[5] - Imports
*Imports devem ser sempre feitos em linhas separadas;

#Import Errado
import sys, os

#Import Certo
import sys
import os

#Não há problemas em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer
comentários ou docstrings e antes de constantes ou variavéis globais

[6] - Espaços em expressões e instruções
#Não faça:
funcao( algo[ 1 ], { outro: 2 } )

#Faça:
funcao(algo[1], {outro: 2})

[7] - Termine sempre uma instrução com uma nova linha
"""










