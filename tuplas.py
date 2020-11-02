"""
Tuplas (tuple)

Tuplas são similares as listas;
Existem 2 diferenças básicas:
1 - AS tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis, ou seja, ela não muda.
Toda operação em uma tupla, gera uma nova tupla.
"""

# Cuidado 1: As tuplas são representadas por (), mas há excessões
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla4 = (4, )  # Isso é uma tupla!
tupla5 = (4)  # Isso não é uma tupla!

# Podemos gerar uma tupla dinâmicamento com range(inicio, fim e passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python Essencial')
escola, curso = tupla
print(escola)
print(curso)

# Obs.: Gera erro (ValueError) se colocarmos um número diferente de elementos

# Métodos para adição e remoção de elementos nas tuplas não existem

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))  # Só funciona em Inteiros ou Reais
print(max(tupla))  # Só funciona em Inteiros ou Reais
print(min(tupla))  # Só funciona em Inteiros ou Reais
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tuplares = tupla1 + tupla2
print(tuplares)

# Verificar se determinado elemento está contido na tupla
print(3 in tupla1)

# Iterando sobre uma tupla
for n in tupla:
    print(n)

# Com indice
for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = "a, b, c, d, a, b"
print(tupla.count('a'))

# Dicas na utilização de tuplas:
# 1 - Usar quando não precisamos modificar os dados de uma coleção
# a)
meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
print(meses)

# O acesso a elementos de uma tupla é semlhante ao da lista
print(meses[3])

# Iterar com o while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual índice um elemento está na tupla
print(meses.index('Jan'))

# Slicing
print(meses[3::2])

# Por quê utilizar tuplas?
# - Tuplas são mais rápidas que listas;
# - Tuplas deixam seu código mais seguro.

# Copiando uma tupla
tupla = (1, 2, 3)
nova = tupla  # Na tupla não temos o problemas de Shallow Copy
outra = (4, 5, 6)
print(nova)
print(tupla)



