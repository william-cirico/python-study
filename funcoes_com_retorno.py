"""
Funções com retorno

Obs.: Em Python, quando uma função não retorna nenhum valor,
o retorno é None

- Funções Python que retornam valores, devem retornar estes valores
com a palavra reservada return

Obs. Return:
- Finaliza a função;
- Uma função pode possuir diferentes returns;
"""

numeros = [1, 2, 3]
ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')


# Exemplo função sem retorno
def quaadrado_de_7():
    print(7 * 7)


# Exemplo de função com retorno
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(ret)


# Refatorando a primeira função
def diz_oi():
    return 'Oi '


alguem = 'Pedro!'
print(diz_oi() + alguem)


# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)  # Desempacotando
print(outra_funcao())


# Exemplo 3
# Gera um número pseudo-randômico entre 0 e 1
from random import random


def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


# Erros comuns na utilização do retorno
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:  # Desnecessauro
        return False


print(eh_impar())









